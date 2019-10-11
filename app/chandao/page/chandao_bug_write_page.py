#coding=utf-8
from base.box import BasePage, ya, BoxDriver
from biz.chandao.chandao_login_page import ChandaoLoginPage
from loguru import logger



class ChandaoBugWritePage(BasePage):

    CHANDAO_BUG_WRITE_LOCATE = ya.get_config_dict['CHANDAO']['LOCATION']['bug_write_page']
    URL = ya.get_config_dict['CHANDAO']['URL']
    time = int(ya.get_config_dict['BASE']['time'])

    def add_bug(self, **kwargs):
        self.open_bug_cat_url()
        self.add_bug_button()
        self.product_chosen(**kwargs)
        self.module_chosen(**kwargs)
        self.project_chosen(**kwargs)
        self.openedBuild_chosen(**kwargs)
        self.assignedTo_chosen(**kwargs)
        self.type_chosen(**kwargs)
        self.os_chosen(**kwargs)
        self.browser_chosen(**kwargs)
        self.severity_level(**kwargs)
        self.priority_level(**kwargs)
        self.write_bug(**kwargs)
        bug_id  = self.base_driver.get_text(self.CHANDAO_BUG_WRITE_LOCATE['bug_id'])
        return bug_id

    def add_bug_simple(self, **kwargs):
        self.open_bug_cat_url()
        self.add_bug_button()
        self.product_chosen(**kwargs)
        self.module_chosen(**kwargs)
        self.openedBuild_chosen(**kwargs)
        self.assignedTo_chosen(**kwargs)
        self.write_bug(**kwargs)
        self.bug_submit()
        self.base_driver.forced_wait(5)
        bug_id = self.base_driver.get_text(self.CHANDAO_BUG_WRITE_LOCATE['bug_id'])
        logger.info('缺陷保存成功,ID是:\n' + bug_id)
        return bug_id

    def open_bug_cat_url(self):
        self.base_driver.navigate(self.URL['bug_write_page']['bug_cat_url'])
        self.base_driver.forced_wait(self.time)
        logger.info('打开总缺陷显示页面')

    def add_bug_button(self):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['add_bug'])
        self.base_driver.forced_wait(self.time)
        logger.info('点击添加缺陷')

    def product_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['product_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['product_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['product_chosen']]
        self.base_driver.forced_wait(self.time)
        logger.info('选择产品:' + kwargs['product_chosen'])

    def module_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['module_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['module_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['module_chosen']]
        self.base_driver.forced_wait(self.time)
        logger.info('选择模块:' + kwargs['module_chosen'])

    def assignedTo_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['assignedTo_chosen_button'])  # 选择指派要先点击下所有用户才能保证正常获取到所有数据
        self.base_driver.forced_wait(self.time)
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['assignedTo_chosen'])
        self.base_driver.forced_wait(self.time)
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['assignedTo_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['assignedTo_chosen']]
        self.base_driver.forced_wait(self.time)
        logger.info('选择处理人:' + kwargs['assignedTo_chosen'])

    def project_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['project_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['project_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['project_chosen']]
        self.base_driver.forced_wait(self.time)

    def openedBuild_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['openedBuild_chosen_button'])  # 选择版本要先点击下所有才能保证正常获取到所有数据
        self.base_driver.forced_wait(self.time)
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['openedBuild_chosen'])
        self.base_driver.forced_wait(self.time)
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['openedBuild_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['openedBuild_chosen']]
        self.base_driver.forced_wait(self.time)
        logger.info('选择版本:' + kwargs['openedBuild_chosen'])

    def type_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['type_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['type_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['type_chosen']]
        self.base_driver.forced_wait(self.time)

    def os_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['os_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['os_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['os_chosen']]
        self.base_driver.forced_wait(self.time)

    def browser_chosen(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['browser_chosen'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['browser_chosen_list'])
        [i.click() for i in elements if i.text == kwargs['browser_chosen']]
        self.base_driver.forced_wait(self.time)

    def severity_level(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['severity_level'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['severity_level_list'])
        [i.click() for i in elements if i.text  == str(u'%s' % kwargs['severity_level']).split('.')[0]]
        self.base_driver.forced_wait(self.time)

    def priority_level(self, **kwargs):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['priority_level'])
        elements = self.base_driver._locate_elements(self.CHANDAO_BUG_WRITE_LOCATE['priority_level_list'])
        [i.click() for i in elements if i.text  == str(u'%s' % kwargs['severity_level']).split('.')[0]]
        self.base_driver.forced_wait(self.time)

    def write_bug(self, **kwargs):
        self.base_driver.type(self.CHANDAO_BUG_WRITE_LOCATE['bug_title'], u'%s' % kwargs['bug_title'])
        logger.info('填写缺陷标题:\n' + kwargs['bug_title'])
        self.base_driver.switch_to_frame(self.CHANDAO_BUG_WRITE_LOCATE['bug_body_iframe']) # 进入ifram
        # bug_body = u'[步骤]' + '\n' + u'%s'% kwargs['reappear_step'] + '\n' + u'[结果]' + '\n' + u'%s' % kwargs['actual_res'] + '\n' + u'[期望]' + '\n' + u'%s'%kwargs['expect_res']
        self.base_driver.type(self.CHANDAO_BUG_WRITE_LOCATE['bug_body'], kwargs['bug_body'])
        logger.info('填写缺陷内容:\n' + kwargs['bug_body'])
        self.base_driver.switch_to_default()

    def bug_submit(self):
        self.base_driver.click(self.CHANDAO_BUG_WRITE_LOCATE['bug_submit'])
        logger.info('缺陷提交成功')

# driver = BoxDriver()
# ChandaoLoginPage(driver).open_login_url()
# account, password = ChandaoLoginPage(driver).get_account(u'长发')
# ChandaoLoginPage(driver).login(account, password)
# chanbugw = ChandaoBugWritePage(driver)
# a = {'product_chosen': u'彩票01', 'module_chosen': u'/前台优化', 'openedBuild_chosen': u'主干', 'assignedTo_chosen': u'D:测试-戚长发', 'bug_title': u'测试', 'bug_body': '测试'}
# chanbugw.add_bug_simple(**a)