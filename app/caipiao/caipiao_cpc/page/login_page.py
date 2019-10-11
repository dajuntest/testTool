#coding=utf-8
from base.basepage import BasePage

from base.small_tool import stool
from loguru import logger
from base.boxdriver import BoxDriver

class CpCLoginPage(BasePage):

    CPC_LOGIN_LOCATE = stool.get_config_dict_yaml['CPC']['LOCATION']['login_page']
    ACCOUNT = stool.get_config_dict_yaml['ACCOUNT']['cpc']
    URL = stool.get_config_dict_yaml['CPC']['URL']
    time = int(stool.get_config_dict_yaml['BASE']['time'])

    def open_login_url(self, ip='240'):
        login_url = self.URL['login_page_url']['http'] + self.URL['login_page_url']['server'][ip] + self.URL['login_page_url']['base']
        self.log('打开登录页面:%s' % login_url)
        self.open(login_url)

    def get_verify_number(self):
        self.log('开始获取登录验证码')
        self.base_driver.click(self.CPC_LOGIN_LOCATE['verify_button'])
        self.log('开始保存验证码截图')
        image_conf = ya.get_config_dict['BASE']['file']['caipiao_clent_verifu_png']
        image_locate = self.CPC_LOGIN_LOCATE['verify_number']
        file_path = self.save_verify_png(image_conf, image_locate)
        self.log('保存截图成功')

        self.log('开始识别验证码')
        verify_number = self._get_verify_number(file_path)
        self.log('普通方式获取的验证码是：%s' % verify_number)
        verify_number_by_baiduocr = self._get_verify_number_by_baiduocr(file_path)
        self.log('百度OCR获取的验证码是: %s' % verify_number_by_baiduocr)
        return verify_number_by_baiduocr

    @logger.catch()
    def login(self, verify_number, user_name=u'长发', ip='240',account=None):
        if account == None:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPC_LOGIN_LOCATE['account'], self.ACCOUNT[ip][user_name]['account'][0])
            self.base_driver.type(self.CPC_LOGIN_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.type(self.CPC_LOGIN_LOCATE['verify_write'], verify_number)
            self.base_driver.click(self.CPC_LOGIN_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)
        else:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPC_LOGIN_LOCATE['account'], account)
            self.base_driver.type(self.CPC_LOGIN_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.type(self.CPC_LOGIN_LOCATE['verify_write'], verify_number)
            self.base_driver.click(self.CPC_LOGIN_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)

    def login_result(self):
        self.log('开始判断登录结果')
        result_flag = None
        self.base_driver._locate_element(self.CPC_LOGIN_LOCATE['alert'])
        result = self.base_driver.get_text(self.CPC_LOGIN_LOCATE['alert_text'])
        self.log('登录结果为:%s' % result)
        if result == self.CPC_LOGIN_LOCATE['alert_text_true']:
            self.log('登录成功,关闭提示框')
            self.base_driver.click(self.CPC_LOGIN_LOCATE['alert_comit'])
            self.base_driver.forced_wait(seconds=self.time)
            result_flag = True
        else:
            self.log('登录失败,进行重新登录操作')
            self.base_driver.click(self.CPC_LOGIN_LOCATE['alert_comit'])
            result_flag = False
        return result_flag

    def get_url(self):
        return self.base_driver.get_url()


    ''' 
    自动登录方法相关
    '''
    @logger.catch()
    def login_action(self, ip='240'):
        self.log('开始进行彩票系统登录')
        print(ip)
        print(type(ip))
        self.open_login_url(ip=ip)
        print('1111111')
        verify_number = self.get_verify_number()
        self.login(verify_number)

    def close_alert_(self):
        pass

if __name__ == '__main__':
    CpCLoginPage(BoxDriver()).login_action()