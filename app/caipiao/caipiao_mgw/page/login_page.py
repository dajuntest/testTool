#coding=utf-8
from base.basepage import BasePage
from base.small_tool import stool
from loguru import logger
from base.boxdriver import BoxDriver
from pynput.keyboard import Key, Controller


class CpMLoginPage(BasePage):

    CPM_LOGIN_LOCATE = stool.get_config_dict_yaml['CPM']['LOCATION']['login_page']
    ACCOUNT = stool.get_config_dict_yaml['ACCOUNT']['cpm']
    URL = stool.get_config_dict_yaml['CPM']['URL']
    time = int(stool.get_config_dict_yaml['BASE']['time'])

    def open_login_url(self, ip='240'):
        login_url = self.URL['login_page_url']['http'] + self.URL['login_page_url']['server'][ip] + self.URL['login_page_url']['base']
        self.log('打开登录页面:%s' % login_url)
        self.open(login_url)

    @logger.catch()
    def login(self, user_name=u'长发', ip='240', account=None):
        if account == None:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPM_LOGIN_LOCATE['account'], self.ACCOUNT[ip][user_name]['account'][0])
            self.base_driver.type(self.CPM_LOGIN_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.click(self.CPM_LOGIN_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)
            Controller().press(Key.enter)
            Controller().release(Key.enter)
            self.base_driver.forced_wait(seconds=self.time)
        else:
            self.log('开始进行登录操作')
            self.base_driver.type(self.CPM_LOGIN_LOCATE['account'], account)
            self.base_driver.type(self.CPM_LOGIN_LOCATE['password'], self.ACCOUNT[ip][user_name]['password'])
            self.base_driver.click(self.CPM_LOGIN_LOCATE['submit'])
            self.base_driver.forced_wait(seconds=self.time)
            Controller().press(Key.enter)
            Controller().release(Key.enter)
            self.base_driver.forced_wait(seconds=self.time)


# if __name__ == '__main__':
#     CpMLoginPage(BoxDriver()).open_login_url()
