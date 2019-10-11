# coding=utf-8

# pytest -s -q  ./case/caipiao-client/test_buy_lottery.py  --alluredir  ./runner/result/
# allure generate ./runner/result/  -o  ./runner/report/  --clean
# allure open ./runner/report/
from time import sleep
import pytest
import allure
from biz.caipiao_client.lottery_hall_page import CpCLotteryHallPage
from base.box import  ya


@allure.feature('购彩大厅测试')
class TestLotteryHall(object):

    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    @allure.story('随机购买一注')
    @allure.severity('严重')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.testlink.com")
    # @logger.catch()
    def test_buy_random_one(self, with_open_lottery_page):
        '''
        这个测试的是随机选择一种彩票,然后随机购买一注,记录并显示购买的结果
        with_login_cpc: 用于登录彩票页面
        with_open_lottery_page: 用于进入购彩大厅页面
        '''

        # Arrange 准备工作
        # file = 'D:\\coding\\biz\\conf.yaml'
        cpclotteryhall = CpCLotteryHallPage()
        file_path = ya.get_config_dict(cpclotteryhall.file)['BASE']['file']['png_path']
        lottery_name_png = file_path + 'lottery_name.png'
        bet_name_png = file_path + 'bet_name.png'
        odd_number_png = file_path + 'odd_number.png'

        with allure.step('选择彩种:'):
            allure.attach(with_open_lottery_page, '选择的彩种是:')
            cpclotteryhall.get_screenshot_as_file(lottery_name_png)
            allure.attach.file(lottery_name_png, name='彩种截图', attachment_type=allure.attachment_type.PNG)

        with allure.step('随机购买一注'):
            cpclotteryhall.log('随机购买一注')
            cpclotteryhall.select_random_one()
            cpclotteryhall.log('点击确认购买')
            cpclotteryhall.submit_ensure_buy()
            bet_name = cpclotteryhall.get_bet_type()
            cpclotteryhall.log('下注种类是: %s' % bet_name)
            allure.attach(bet_name, '下注种类是: ')
            cpclotteryhall.get_screenshot_as_file(bet_name_png)
            allure.attach.file(bet_name_png, name='下注截图', attachment_type=allure.attachment_type.PNG)
            cpclotteryhall.log('确定购买')
            cpclotteryhall.submit_yes()
            result = cpclotteryhall.get_alert_text()
            cpclotteryhall.log('购买结果是: %s' % result)
            cpclotteryhall.log('确认弹框')
            cpclotteryhall.submit_alert()
            cpclotteryhall.forced_wait()
            odd_number = cpclotteryhall.get_odd_number()
            cpclotteryhall.log('兑奖号是: %s' % odd_number)
            allure.attach(odd_number, '兑奖号是:')
            cpclotteryhall.get_screenshot_as_file(odd_number_png)
            allure.attach.file(odd_number_png, name='兑奖号截图',
                               attachment_type=allure.attachment_type.PNG)

        # Assert 验证结果
            cpclotteryhall.log('测试结果验证,如果显示购买成功就测试通过')
            allure.attach(result, '购买结果是:')
            assert result == '购买成功'

        cpclotteryhall.log('测试结束,关闭浏览器')


if __name__ == '__main__':
    pytest.main(["-q", "-s", " -k test_buy_lottery.py", "--alluredir  ./runner/result/"])
    # TestLotteryHall().test_buy_random_one()