# -*- coding=utf-8 -*-
import os
import re

import pinyin.cedict
from loguru import logger
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.types import CHAR, INT


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("testTool\\") + len("testTool\\")]

class AutoWrite(object):

    # 创建目录方法
    def mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

    # 分词
    def jieba_cut(self, str):
        import jieba

        seg_list = jieba.lcut(str)
        return seg_list

    # 名字转换为中文拼音首字母拼接(这样比较稳定,但是可读性差,有更好方法再替换)
    def name2pinyin(self, name):
        return (pinyin.get_initial(name)).replace(' ', '')

    # 解析录制脚本生成的定位信息
    def get_local_data(self, file, app_name=None, page_name=None, url_find='driver.get', element_find='driver.find'):
        '''
        主要是根据app和page来区分避免重复, 最好定位代码一行一个元素,多个会出错
        :param file: 录制软件导出的定位文件数据,主要是katalon生成的,但是格式一致的话也能解析
        :param app_name: 数据库获取产品名,这个主要是由文件格式确定的 所以文件夹格式是必须的
        :param page_name: 页面名
        :param url_find: 用来解析文件中url数据的定位参数,默认是driver.get
        :param element_find: 解析其他定位语句的参数, 默认是driver.find
        :return:
        '''
        local_data = {}
        number = 1
        data = None
        # 兼容不输入产品名和页面名的情况
        if app_name and page_name:
            for line in open(file, 'r', encoding='utf-8'):
                # 元素生成唯一名 产品名_页面名_一个自增序号
                element = self.name2pinyin(app_name) + '_' + self.name2pinyin(page_name)\
                          + '_' + 'element' + '_' + str(number)
                # 解析文件中的url数据,根据格式是(driver.get)来定位
                if re.match(url_find, line.strip()):
                    p1 = re.compile(r'''(?<=["]).+?(?=["])''', re.S)  # 正则匹配双引号内的内容不包过双引号 ,也可以按"截断取第二个值
                    local_data[element] = dict(
                        app_name=app_name,
                        # app_id=self.name2pinyin(app_name),
                        page_name=page_name,
                        # page_id=self.name2pinyin(page_name),
                        local_type='url',
                        local_value=re.findall(p1, line)[0]
                    )
                    number += 1
                # 解析文件中其他的定位数据
                if re.match(element_find, line.strip()):
                    p1 = re.compile(r'(?<=[y]).+?(?=[(])', re.S)  # 正则匹配出使用的是哪种定位方法,取y和左小括号的内容,懒匹配
                    local_data[element] = dict(
                        app_name=app_name,
                        # app_id=self.name2pinyin(app_name),
                        page_name=page_name,
                        # page_id=self.name2pinyin(page_name),
                        local_type=str(re.findall(p1, line.split('"')[0])[0])[1:],  # 为了避免匹配到定位错误,先截断取"前的内容再匹配
                        local_value=line.split('"')[1]
                    )
                    number += 1
                # 解析出来的数据是字典的嵌套数据,转换为pandas处理的数据提高效率和统一性
            data = pd.DataFrame(local_data)  # 生成的是2行多列数据,需要转换
            # data = data.drop_duplicates(["local_value"], keep="first")
            # 行列转换下,索引也转换下,变成3列多行
            data = data.stack().unstack(0)
            # 转换成可以存储格式数据,五列多行,产品,页面,元素,定位种类,定位值
            data = data.reset_index()  # 将行索引重置出来
            data.columns = ['element', 'app_name', 'page_name', 'local_type', 'local_value']  # 对列索引重新命名
        elif app_name is None and page_name is None:
            for line in open(file, 'r', encoding='utf-8'):
                # 元素生成唯一名 产品名_页面名_一个自增序号
                element = 'element' + '_' + str(number)
                # 解析文件中的url数据,根据格式是(driver.get)来定位
                if re.match(url_find, line.strip()):
                    p1 = re.compile(r'''(?<=["]).+?(?=["])''', re.S)  # 正则匹配双引号内的内容不包过双引号 ,也可以按"截断取第二个值
                    local_data[element] = dict(
                        local_type='url',
                        local_value=re.findall(p1, line)[0]
                    )
                    number += 1
                # 解析文件中其他的定位数据
                if re.match(element_find, line.strip()):
                    p1 = re.compile(r'(?<=[y]).+?(?=[(])', re.S)  # 正则匹配出使用的是哪种定位方法,取y和左小括号的内容,懒匹配
                    local_data[element] = dict(
                        local_type=str(re.findall(p1, line.split('"')[0])[0])[1:],  # 为了避免匹配到定位错误,先截断取"前的内容再匹配
                        local_value=line.split('"')[1]
                    )
                    number += 1
            # 解析出来的数据是字典的嵌套数据,转换为pandas处理的数据提高效率和统一性
            data = pd.DataFrame(local_data)  # 生成的是2行多列数据,需要转换
            # data = data.drop_duplicates(["local_value"], keep="first")
            # 行列转换下,索引也转换下,变成3列多行
            data = data.stack().unstack(0)
            # 转换成可以存储格式数据,五列多行,产品,页面,元素,定位种类,定位值
            data = data.reset_index()  # 将行索引重置出来
            data.columns = ['element', 'local_type', 'local_value']  # 对列索引重新命名
        # 去除定位值相同的定位元素
        data = data.drop_duplicates(["local_value"], keep="first")
        # data.to_csv('demo.csv')
        return data

    # 创建文件方法
    def create_file(self, path, file_name):
        new_file = path + file_name
        if not os.path.exists(new_file):
            f = open(new_file, 'w')
            f.close()

    # 根据文件名生成类名
    def file_name2class_name(self, file_name):
        class_name = ''
        for i in file_name.split('_'):
            class_name += ''.join(i.capitalize())
        return class_name

    # 根据文件名目录生成包路径名
    def file_name2package_name(self, app_name, page_name, *args):
        package_name = 'from app' + '.' + app_name + '.'
        for i in args:
            package_name += i + '.'
        package_name += page_name + ' import '
        return package_name

    # 根据文件名目录生成步骤文件名
    def file_nem2step_file_name(self, app_name):
        return app_name + '.py'

    # 获取指定文件路径
    def get_path(self, base_name, *args, app_name=None, page_name=None):
        path = rootPath + base_name
        if app_name:
            path += '\\%s' % app_name
            if args:
                for i in args:
                    path += '\\%s' % i
                if page_name:
                    path += '\\%s' % page_name
        return path

    # 创建app文件目录结构
    def create_app_structure(self, app_name, page_name, *args):
        '''
        创建app的文件夹结构
        :param app_name:
        :param page_name:
        :param args: 不定个数的moudle_name
        :return:
        '''
        path = rootPath + 'app\\' + '\\%s' % app_name
        self.mkdir(path)
        self.create_file(path, '\\__init__.py')
        for i in args:
            path += '\\%s' % i
            self.mkdir(path)
            self.create_file(path, '\\__init__.py')
        path += '\\%s' % page_name
        self.mkdir(path)
        self.create_file(path, '\\%s.py' % page_name)

    # 创建feature文件目录结构
    def create_features_structure(self, app_name, page_name, function_name, *args):
        '''
        创建bdd测试文件结构,feature文件和step文件结构
        :param app_name:
        :param page_name:
        :param function_name:
        :param args:
        :return:
        '''
        path_feature = rootPath + 'features' + '\\%s' % app_name
        path_step = rootPath + 'features' + '\\steps'
        step_name = '%s' % app_name + '_%s' % page_name
        for i in args:
            path_feature += '\\%s' % i
        path_feature += '\\%s' % page_name
        self.mkdir(path_feature)
        self.create_file(path_feature, '\\%s.feature' % function_name)
        self.create_file(path_step, '\\%s.py' % step_name)

    ''' 初始化和填充文件内容 '''
    # 初始和写入total文件
    def init_total_page(self, app_name):
        file = self.get_path('app', app_name=app_name) + '\\__init__.py'
        app_class_name = self.file_name2class_name(app_name)
        text = '\nclass %s(object):\n    pass' % (app_class_name+'TotalPage')
        with open(file, 'w') as f:
            f.write(text)

    @logger.catch()
    def write_app_total_page_file(self, app_name, page_name, *args):
        '''
        app中所有的页面都被一个total页面集成
        :return:
        '''
        file = self.get_path('app', app_name=app_name) + '\\__init__.py'
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 判断文件是否要先初始化下
        if len(content) < 1:
            self.init_total_page(app_name)

        # 组装要写入的内容
        page_class_name = self.file_name2class_name(page_name)  # 修改继承的类

        package_name = self.file_name2package_name(app_name, page_name, *args) + page_class_name + '\n\n\nclass'  # 添加导入的包

        # 组装内容
        p1 = re.compile(r"(?<=[(]).+?(?=[)])", re.S)  # 最小匹配()括号中的内容
        old_text = re.findall(p1, content)
        new_text = page_class_name + ', ' + old_text[0]

        content = re.sub(p1, new_text, content)  # 替换类值
        content = content.replace('class', package_name)  # 添加包路径

        # 写回原文档
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

    # 初始和写入page文件
    def init_page(self, app_name, page_name, *args):
        file = self.get_path('app', *args, app_name=app_name, page_name=page_name) + '\\%s.py' % page_name
        page_class = self.file_name2class_name(page_name)
        text = '#coding=utf-8\n' \
               'from poium import Page, PageElement\n\n\n' \
               'class %s(Page):\n' % (page_class)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

    def write_page_file(self, app_name, page_name, element_id, local_type, local_value, element_descript, *args):
        file = self.get_path('app', *args, app_name=app_name, page_name=page_name) + '\\%s.py' % page_name
        text = ':\n\n    ' + element_id + ' = ' + """PageElement(%s="%s", describe=\'%s\')""" \
               % (local_type, local_value, element_descript)
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 判断文件是否要初始化
        if len(content) < 1:
            self.init_page(app_name, page_name, *args)

        content = content.replace(':', text)  # 添加新的元素定位

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

    # 初始化和写入feature文件
    def init_features(self, app_name, page_name, function_name, function_name_zh, *args):
        file = self.get_path('features', *args, app_name=app_name, page_name=page_name) + '//%s.feature' % function_name
        text = '# language: zh-CN\n' \
               '功能: %s' % function_name_zh

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

    def write_features_file(self, app_name, page_name, function_name, function_name_zh, *args):
        file = self.get_path('features', *args, app_name=app_name, page_name=page_name) + '//%s.feature' % function_name
        text = ('\n\n  @1\n'
            '  场景: 测试测试\n'
            '    假如士大夫撒旦\n'
            '    而且士大夫撒旦\n'
            '    当委任为\n'
            '    那么士大夫撒旦')

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 判断文件是否要初始化
        if len(content) < 1:
            self.init_features(app_name, page_name, function_name, function_name_zh, *args)

        with open(file, 'a', encoding='utf-8') as f:
            f.write(text)

    # 初始化和写入step文件
    def init_step(self, app_name):
        step_file_name = self.file_nem2step_file_name(app_name)
        file = self.get_path('features\\steps') + '\\%s' % step_file_name
        text = '#coding=utf-8\n' \
               'from behave import *\n' \
               'from base.webaction import WebAction\n' \
               'from app.cp01_h5_old import Cp01H5OldTotalPage\n\n' \
               'web = WebAction(Cp01H5OldTotalPage)\n\n'

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

    def write_step_file(self, app_name):
        step_file_name = self.file_nem2step_file_name(app_name)
        file = self.get_path('features\\steps') + '\\%s' % step_file_name
        text = "@step(u'测试')\n" \
               "def step_impl(context):\n" \
               "    web.get('123123').input('dfsfsdfs')\n\n\n"

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 判断文件是否要初始化
        if len(content) < 1:
            self.init_step(app_name)

        with open(file, 'a', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':

    autow = AutoWrite()
    # moudle = ['zcmk']
    # autow.create_app_structure('cp01-H5-V1', 'zcy', *moudle)
#     list = autow.jieba_cut('下注模块')
#     print(type(list))
#     for i in list:
#         # print(i)
#         if
#         print(SmallTool.english2chinese(i))
    data = autow.get_local_data('UntitledTestCase.txt', '彩票', '登录页')
    connect_info = 'mysql+pymysql://dajun:heli84327@localhost:3306/webauto?charset=utf8'
    engine = create_engine(connect_info)  # use sqlalchemy to build link-engine

    # sql = "SELECT * FROM test0811"  # SQL query
    # df = pd.read_sql(sql=sql, con=engine)  # read data to DataFrame 'df'

    # write df to table 'test1'
    data.to_sql(name='local_element', con=engine, if_exists='append', index=False)
