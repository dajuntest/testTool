#coding=utf-8
from base.boxdriver import BoxDriver
from aip import AipOcr
from PIL import Image
from loguru import logger

class BasePage(object):
    """
    测试系统的最基础的页面类，是所有其他页面的基类
    """
    # 变量
    base_driver = None

    def __init__(self, driver: BoxDriver):
        self.base_driver = driver

    def open(self, url):
        self._by_char = ','
        self.base_driver.navigate(url)
        self.base_driver.maximize_window()
        self.base_driver.implicitly_wait(5)

    def log(self, msg):
        logger.info(msg)
        print(msg)

    def forced_wait(self, seconds=2):
        self.base_driver.forced_wait(seconds)

    def close(self):
        self.base_driver.close_browser()

    def get_screenshot_as_png(self):
         self.base_driver.get_screenshot_as_png()

    def get_screenshot_as_file(self, file):
         self.base_driver.get_screenshot_as_file(file)

    def save_verify_png(self, image_conf, image_locate):
        image_name = image_conf.split(self._by_char)[0].strip()
        image_path = image_conf.split(self._by_char)[1].strip()
        try:
            _file_name = image_name
            _file_name_wz = str(_file_name) + '.png'
            _file_path = image_path + _file_name_wz
            self.base_driver.get_screenshot_as_file(_file_path)  # get_screenshot_as_file截屏
            captchaElem = self.base_driver._locate_element(image_locate)  # # 获取指定元素（验证码）
            # 因为验证码在没有缩放，直接取验证码图片的绝对坐标;这个坐标是相对于它所属的div的，而不是整个可视区域
            # location_once_scrolled_into_view 拿到的是相对于可视区域的坐标  ;  location 拿到的是相对整个html页面的坐标
            captchaX = int(captchaElem.location['x'])
            captchaY = int(captchaElem.location['y'])
            # 获取验证码宽高
            captchaWidth = captchaElem.size['width']
            captchaHeight = captchaElem.size['height']

            captchaRight = captchaX + captchaWidth
            captchaBottom = captchaY + captchaHeight

            imgObject = Image.open(_file_path)  # 获得截屏的图片
            imgCaptcha = imgObject.crop((captchaX, captchaY, captchaRight, captchaBottom))  # 裁剪
            imgCaptcha.save(_file_path)
            return _file_path
        except Exception as e:
            print('error ：', e)

    def _get_verify_number_by_baiduocr(self, file_path):

        config = {
            'appId': '17246577',
            'apiKey': 'B0128v8X47ciBLFEeU2iWK2F',
            'secretKey': '1yG3gKa5jaunMfQn235s1VLZa7Q69Ufu'
        }
        client = AipOcr(**config)

        with open(file_path, 'rb') as fp:
            image = fp.read()
        result = client.basicAccurate(image)
        return result['words_result'][0]['words']
