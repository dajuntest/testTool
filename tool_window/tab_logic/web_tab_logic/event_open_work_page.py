# coding=utf-8
from app.caipiao.caipiao_cpc.page.login_page import CpCLoginPage
from app.caipiao.caipiao_cpc.page.login_page_h5 import CpCLoginPageH5
from app.caipiao.caipiao_mgw.page.login_page import CpMLoginPage
from base.boxdriver import BoxDriver


class EventOpenWorkPage(object):

    driver = None

    def __init__(self, driver=BoxDriver):
        self.driver = driver

    def login_cpc(self, user_name, ip, account):
        cpc = CpCLoginPage(self.driver)
        cpc.log('开始进行彩票系统登录')
        cpc.open_login_url(ip)
        verify_number = cpc.get_verify_number()
        cpc.login(verify_number, user_name, ip=ip, account=account)

    def login_cpc_h5(self, user_name, ip, account):
        cpch5 = CpCLoginPageH5(self.driver)
        cpch5.log('开始登录彩票h5页面')
        cpch5.open_login_url(ip)
        cpch5.login(user_name, ip=ip, account=account)

    def login_cpm(self, user_name, ip, account):
        cpm = CpMLoginPage(self.driver)
        cpm.log('开始登录彩票管理页面')
        cpm.open_login_url(ip)
        cpm.login(user_name, ip=ip, account=account)

    def open_work_page(self, user, ip, page, values):
        if page == '彩票PC':
            self.login_cpc(user, ip, values['account'])
        elif page == '彩票H5':
            self.login_cpc_h5(user, ip, values['account'])
        elif page == '彩票管理':
            self.login_cpm(user, ip, values['account'])


# if __name__ == '__main__':
#
#     AutoLogin(BoxDriver(browser_type=1)).login_cpm('长发', '240', account=None)
