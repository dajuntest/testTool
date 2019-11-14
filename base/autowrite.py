# -*- coding=utf-8 -*-
import os
import re

from base.small_tool import SmallTool

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

    # 解析录制脚本生成的定位信息
    def get_local_data(self, file):
        local_data = {}
        number = 0
        for line in open(file, 'r', encoding='utf-8'):
            data_number = 'data' + str(number)
            # 解析url数据
            if re.match('driver.get', line.strip()):
                # print(re.match('driver.get', line.strip()))
                p1 = re.compile(r'''(?<=["]).+?(?=["])''', re.S)
                local_data[data_number] = dict(
                    local_type='url',
                    local_value=re.findall(p1, line)[0]
                )
                # print(local_data)
                number += 1
            # 解析定位数据
            if re.match('driver.find', line.strip()):
                p1 = re.compile(r'(?<=[y]).+?(?=[(])', re.S)
                local_data[data_number] = dict(
                    local_type=str(re.findall(p1, line.split('"')[0])[0])[1:],
                    local_value=line.split('"')[1]
                )
                number += 1
        return local_data

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
    def file_nem2step_file_name(self, app_name, page_name):
        return app_name + '_' + page_name + '.py'

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
        step_name = '%s' % app_name + '%s' % page_name
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
    def init_step(self, app_name, page_name):
        step_file_name = self.file_nem2step_file_name(app_name, page_name)
        file = self.get_path('features\\steps') + '\\%s' % step_file_name
        text = '#coding=utf-8\n' \
               'from behave import *\n' \
               'from base.webaction import WebAction\n' \
               'from app.cp01_h5_old import Cp01H5OldTotalPage\n\n' \
               'web = WebAction(Cp01H5OldTotalPage)\n\n'

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

    def write_step_file(self, app_name, page_name):
        step_file_name = self.file_nem2step_file_name(app_name, page_name)
        file = self.get_path('features\\steps') + '\\%s' % step_file_name
        text = "@step(u'测试')\n" \
               "def step_impl(context):\n" \
               "    web.get('123123').input('dfsfsdfs')\n\n\n"

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 判断文件是否要初始化
        if len(content) < 1:
            self.init_step(app_name, page_name)

        with open(file, 'a', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':

    autow = AutoWrite()
    list = autow.jieba_cut('下注模块')
    print(type(list))
    for i in list:
        # print(i)
        if
        print(SmallTool.english2chinese(i))
