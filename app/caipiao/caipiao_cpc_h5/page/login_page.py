#coding=utf-8
from base.basepage import BasePage
from base.small_tool import stool
from pynput.keyboard import Key, Controller


class CpCLoginPageH5(BasePage):

    CPC_LOGIN_H5_LOCATE = stool.get_config_dict_yaml['CPC']['LOCATION']['login_page_h5']
    ACCOUNT = stool.get_config_dict_yaml['ACCOUNT']['cpc']
    URL = stool.get_config_dict_yaml['CPC']['URL']
    time = int(stool.get_config_dict_yaml['BASE']['time'])

    def open_login_url(self, ip='240'):
        login_url = self.URL['login_page_url_h5']['http'] + self.URL['login_page_url_h5']['server'][ip] + self.URL['login_page_url_h5']['base']
        self.log('打开登录页面:%s' % login_url)
        self.open(login_url)
        self.log(('开始进入mobile模式'))
        self.change_to_mobile()
        self.forced_wait(self.time)


    def login(self, user_name, ip='240', account=None):
        if account == None:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPC_LOGIN_H5_LOCATE['account'], self.ACCOUNT[ip][user_name]['account'][0])
            self.base_driver.type(self.CPC_LOGIN_H5_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.click(self.CPC_LOGIN_H5_LOCATE['submit'])
            self.base_driver.click(self.CPC_LOGIN_H5_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)

        else:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPC_LOGIN_H5_LOCATE['account'], account)
            self.base_driver.type(self.CPC_LOGIN_H5_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.click(self.CPC_LOGIN_H5_LOCATE['submit'])
            self.base_driver.click(self.CPC_LOGIN_H5_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)

    def change_to_mobile(self):
        keyboard = Controller()
        keyboard.press(Key.f12)
        keyboard.release(Key.f12)
        self.base_driver.forced_wait(self.time)
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('m')
                keyboard.release('m')