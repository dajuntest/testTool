# coding=utf-8
from biz.caipiao_client.login_page import CpCLoginPage
from base.box import BoxDriver
import pytest


@pytest.fixture(autouse=True)
# @logger.catch(level='DEBUG')
def with_login_cpc():
    cpclogin = CpCLoginPage(BoxDriver())
    cpclogin.log('开始执行测试')
    login_result = False
    cpclogin.log('开始进行彩票系统登录')
    cpclogin.open_login_url()
    while not login_result:
        verify_number = cpclogin.get_verify_number()
        cpclogin.login(verify_number)
        login_result = cpclogin.login_result()
        if login_result:
            break
    yield
    cpclogin.close()



# @pytest.fixture(autouse=True)
# def demo_1():
#     logger.info('demo1')
#     webdriver.Chrome()
# @pytest.fixture(scope="session", autouse=True)
# def env(request):
#     """
#     Parse env config info
#     """
#     root_dir = request.config.rootdir
#     config_path = '{0}/config/env_config.yml'.format(root_dir)
#     with open(config_path) as f:
#         env_config = yaml.load(f) # 读取配置文件
#
#     allure.environment(host=env_config['host']['domain']) # 测试报告中展示host
#     allure.environment(browser=env_config['host']['browser']) # 测试报告中展示browser
#
#     return env_config