#coding=utf-8
import base64
import json
import os
from time import sleep
import time
from urllib import parse, request
from aip import AipOcr
from selenium import webdriver
import yaml
from PIL import ImageGrab

# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install baidu-aip


FILE = 'C:\\Users\\dajun\\Documents\\testTool\\conf.yaml'
image_file = './test/image/bug_image.png'

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

    def cut_screeon_image(self, image_path=image_file):
        im = ImageGrab.grab()  # 可以添加一个坐标元组进去 不加就是全屏截屏
        im.save(image_path)
        return image_path

    def prs_exe(self):
        os.system('C:\\Windows\\System32\\psr.exe')

    def get_verify_number_by_baiduocr_bs64(self, image_bs64):
        config = {
            'appId': '17246577',
            'apiKey': 'B0128v8X47ciBLFEeU2iWK2F',
            'secretKey': '1yG3gKa5jaunMfQn235s1VLZa7Q69Ufu'
        }
        client = AipOcr(**config)

        image = base64.b64decode(image_bs64)
        result = client.basicAccurate(image)
        return result['words_result'][0]['words']

    # 获取下拉列表数据
    def get_calss_opthion(self, locate_one, locate_two, class_name):
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

    # 对选中的地方进行高亮的虚线框样式添加
    def high_line_style(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver = webdriver.Chrome()

        driver.get('https://555.0234.co/pc/index.html')

        # ele =  driver.find_element(By.XPATH, '//button[contains(.,'登录')]')   # 定位元素
        ele = driver.find_element(By.XPATH, "//input[@placeholder='账号']")

        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele,
                              "outline: 2px dashed #07bb46 !important")  # 元素的背景色和边框设置成绿色和红色

        ele.click()

    # 树状结构查看文件夹
    def tree_cat(self):
        __author__ = 'AlbertS'

        import os
        import os.path

        def dfs_showdir(path, depth):
            if depth == 0:
                print("root:[" + path + "]")

            for item in os.listdir(path):
                if '.git' not in item:
                    print("| " * depth + "+--" + item)

                    newitem = path + '/' + item
                    if os.path.isdir(newitem):
                        dfs_showdir(newitem, depth + 1)
        # if __name__ == '__main__':
        #     dfs_showdir('.', 0)


stool = SmallTool()

# if __name__ == '__main__':
#
#     b64 = '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'
#     stool.get_verify_number_by_baiduocr_bs64(b64)