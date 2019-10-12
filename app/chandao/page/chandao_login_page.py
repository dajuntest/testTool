#coding=utf-8
from base.basepage import BasePage
from base.boxdriver import BoxDriver
from base.small_tool import stool
from loguru import logger


class ChandaoLoginPage(BasePage):

    CHANDAO_LOGIN_LOCATE = stool.get_config_dict_yaml['CHANDAO']['LOCATION']['login_page']
    URL = stool.get_config_dict_yaml['CHANDAO']['URL']
    time = int(stool.get_config_dict_yaml['BASE']['time'])

    def open_login_url(self):
        self.open(self.URL['login_page']['login_url'])
        logger.info('打开禅道页面:' + self.URL['login_page']['login_url'])
        print('打开禅道页面:' + self.URL['login_page']['login_url'])

    def login(self, accout, password):
        self.base_driver.type(self.CHANDAO_LOGIN_LOCATE['account'], accout)
        self.base_driver.type(self.CHANDAO_LOGIN_LOCATE['password'], password)
        self.base_driver.click(self.CHANDAO_LOGIN_LOCATE['submit'])
        logger.info('成功登录禅道页面')
        print('成功登录禅道页面')
        self.base_driver.forced_wait(self.time)

    def get_account(self, user):
        account = stool.get_config_dict_yaml['ACCOUNT']['chandao'][user]['account']
        password = stool.get_config_dict_yaml['ACCOUNT']['chandao'][user]['password']
        logger.info('获取禅道账号和密码:\n' + account + ',' + password)
        print('获取禅道账号和密码:\n' + account + ',' + password)
        return account, password

    def page_url(self):
        return self.base_driver.get_url()

    def colse(self):
        self.base_driver.close_browser()

# chanlogin = ChandaoLoginPage(BoxDriver())
# chanlogin.open_login_url()
# chanlogin.login('dajun', 'Dajun123')