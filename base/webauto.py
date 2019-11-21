# coding=utf-8
from base.autowrite import AutoWrite


class WebAuto(object):

    def __init__(self, auto: AutoWrite):
        self.webauto = auto

    def save_local_data(self):
        '''
        解析定位文件,并将定位数据存储到数据库中和防重复文件中
        :return:
        '''
        # 1.解析元素定位文件
        self.webauto.get_local_data(file=, app_name=None, page_name=None, url_find='driver.get', element_find='driver.find')

        # 2.存入数据库中   element_id由产品和页面加参数生成唯一值,定位种类,定位值,元素名



    def save_case_data(self):
        '''
        数据库中获取用例数据,创建文件和写入文件数据
        :return:
        '''
        # 1.获取用例数据并解析

        # 2.获取步骤数据并解析

        # 3.拼凑创建路径要用数据生成路径,路径自动防重复

        # 4.检查写入数据是否重复,拼凑然后将数据写入文件

    def update_case_data(self):
        '''
        更新测试用例数据
        :return:
        '''
        pass


    def run_case(self):
        pass