# encoding=utf-8
import csv
import pinyin.cedict
from itertools import islice  # 可以忽略首行
from base.autowrite import AutoWrite


with open('case_data.csv', encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in islice(f_csv, 1, None):
        if '功能' in row[0] and '页' in row[0]:
            data = str(row[0]).split('/')
            app_name = (pinyin.get_initial(data[0])).replace(' ', '')
            page_name = ''
            function_name = ''
            function_name_zh = ''
            module_name = []
            for i in data:
                if '模块' in i:
                    module_name.append((pinyin.get_initial(i)).replace(' ', ''))
                if '页' in i:
                    page_name = (pinyin.get_initial(i)).replace(' ', '')
                if '功能' in i:
                    function_name = (pinyin.get_initial(i)).replace(' ', '')
                    function_name_zh = i
            # 创建app目录结构
            AutoWrite().create_app_structure(app_name, page_name, *module_name)
            # 创建测试目录结构
            AutoWrite().create_features_structure(app_name, page_name, function_name, *module_name)

            # 写total文件
            AutoWrite().write_app_total_page_file(app_name, page_name, *module_name)

            # 写步骤文件
            AutoWrite().write_step_file(app_name, page_name)

            # 写用例文件
            AutoWrite().write_features_file(app_name, page_name, function_name, function_name_zh, *module_name)

        # # 写文件
        # if '功能' not in row[0] and '页' in row[0]:



'''
row[0] 路径
row[1] 编号 做tag
row[2] 场景
row[6] 步骤
'''