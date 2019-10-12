#coding=utf-8
import base64
import json
from time import sleep
import time
from urllib import parse, request
from aip import AipOcr
from selenium import webdriver
import yaml

# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install baidu-aip


FILE = 'C:\\Users\\dajun\\Documents\\testTool\\conf.yaml'

class SmallTool(object):

    @property
    def get_config_dict_yaml(self, f=FILE):
        """
        获取所有配置
        :param f:
        :return:
        """
        with open(f, mode='r', encoding='UTF-8') as file_config:
            config_dict = yaml.load(file_config.read(), Loader=yaml.FullLoader)
            return config_dict

    @staticmethod
    def timestamp_to_time(timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    @staticmethod
    def json_beauty(text):
        data_text = json.loads(text)
        res = json.dumps(data_text, indent=2)
        return res

    @staticmethod
    def english2chinese(text):
        req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
        # 创建要提交的数据
        Form_Date = {}
        Form_Date['i'] = text
        Form_Date['doctype'] = 'json'
        Form_Date['form'] = 'AUTO'
        Form_Date['to'] = 'AUTO'
        Form_Date['smartresult'] = 'dict'
        Form_Date['client'] = 'fanyideskweb'
        Form_Date['salt'] = '1526995097962'
        Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
        Form_Date['version'] = '2.1'
        Form_Date['keyform'] = 'fanyi.web'
        Form_Date['action'] = 'FY_BY_REALTIME'
        Form_Date['typoResult'] = 'false'

        data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
        response = request.urlopen(req_url, data)  # 提交数据并解析
        html = response.read().decode('utf-8')  # 服务器返回结果读取
        # print(html)
        # 可以看出html是一个json格式
        translate_results = json.loads(html)  # 以json格式载入
        translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
        # print(translate_results)  # 输出结果
        return translate_results

    #todo 添加快捷截图功能
    def cut_screeon_image(self):
        pass

    # todo 添加prs.exe快捷功能

    def get_verify_number_by_baiduocr_bs64(image_bs64):
        config = {
            'appId': '17246577',
            'apiKey': 'B0128v8X47ciBLFEeU2iWK2F',
            'secretKey': '1yG3gKa5jaunMfQn235s1VLZa7Q69Ufu'
        }
        client = AipOcr(**config)

        image = base64.b64decode(image_bs64)
        result = client.basicGeneral(image)
        return result['words_result'][0]['words']


    # 获取下拉列表数据
    def get_calss_opthion(locate_one, locate_two, class_name):
        '''
        暂时都用xpath定位
        :param locate_one: 用于点击下下拉框显示出下拉列表
        :param locate_two: 用于获取下拉列表所有值
        :return: 选项值的列表集合
        '''

        driver = webdriver.Chrome()

        url = 'https://pms.27o1.cn/www/index.php?m=user&f=login'
        url2 = 'https://pms.27o1.cn/www/index.php?m=project&f=bug'
        driver.get(url)
        sleep(2)

        # 登录
        driver.find_element_by_id('account').send_keys('dajun')
        driver.find_element_by_xpath('//*[@id="login-form"]/form/table/tbody/tr[2]/td/input').send_keys('Dajun123')
        driver.find_element_by_id('submit').click()
        sleep(2)

        # 跳转到对应页面
        driver.get(url2)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="titlebar"]/div[2]/a[2]').click()  # 进入创建缺陷页面
        sleep(2)

        # 点击要获取的下拉框
        driver.find_element_by_xpath(locate_one).click()
        sleep(2)

        # 获取下拉框展示出来的所有元素
        select_opthion = driver.find_element_by_xpath(locate_two).find_elements_by_class_name(class_name)

        res = []
        for i in select_opthion:
            res.append(i.text)
        driver.quit()
        return res



stool = SmallTool()

# if __name__ == '__main__':
#     print(stool.get_config_dict['BASE'])