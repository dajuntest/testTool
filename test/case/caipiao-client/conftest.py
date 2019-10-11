# coding=utf-8
from biz.caipiao_client.lottery_hall_page import cpclotteryhall
import pytest

@pytest.fixture()
def with_open_lottery_page(with_login_cpc):
    lottery_id = cpclotteryhall.random_lottery_id()
    cpclotteryhall.open_lottery_hall(lottery_id)
    lottery_name = cpclotteryhall.get_lottery_name()
    cpclotteryhall.log('选取彩票为: %s' % lottery_name)
    # allure.attach(lottery_name, '选择的彩种是:')
    # cpclotteryhall.get_screenshot_as_file(lottery_name_png)
    yield lottery_id
    # logger.info('测试结束关闭浏览器')
    # BasePage().close()

# @pytest.fixture(autouse=True)
# def demo_2():
#     logger.info('demo2')
