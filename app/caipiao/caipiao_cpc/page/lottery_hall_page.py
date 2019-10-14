#coding=utf-8
import random
from base.basepage import BasePage
from base.small_tool import stool


class CpCLotteryHallPage(BasePage):

    def __init__(self):
        self.CPC_LOTTERY_HALL_LOCATE = stool.get_config_dict_yaml['CPC']['LOCATION']['lottery_hall_page']
        self.URL = stool.get_config_dict_yaml['CPC']['URL']
        self.time = int(stool.get_config_dict_yaml['BASE']['time'])


    def random_lottery_id(self):
        lottery_type = str(random.choice(cpclotteryhall.URL['lottery_hall_page']['number']['lottery_type_id']))
        return lottery_type

    def open_lottery_hall(self, lottery_id, ip='240'):
        if ip == 240:
            self.log('默认使用的环境是是: %s' % self.URL['lottery_hall_page']['server'][ip])
        lottery_url = self.URL['lottery_hall_page']['http'] + self.URL['lottery_hall_page']['server'][ip] + \
                      self.URL['lottery_hall_page']['base'] + lottery_id
        self.open(lottery_url)

    def select_random_one(self):
        '''
        点击随机一注
        :return:
        '''
        self.base_driver.click(self.CPC_LOTTERY_HALL_LOCATE['random_one'])
        self.base_driver.forced_wait(seconds=self.time)

    def submit_ensure_buy(self):
        '''
        点击确认投注
        :return:
        '''
        self.base_driver.click(self.CPC_LOTTERY_HALL_LOCATE['lottery_buy'])
        self.base_driver.forced_wait(seconds=self.time)

    def submit_yes(self):
        '''
        点击确认框中的yes
        :return:
        '''
        self.base_driver.click(self.CPC_LOTTERY_HALL_LOCATE['confirm_yes'])
        self.base_driver.forced_wait(seconds=self.time)

    def submit_alert(self):
        '''
        点击确认框的确定按钮
        :return:
        '''
        self.base_driver._locate_element(self.CPC_LOTTERY_HALL_LOCATE['alert'])
        self.base_driver.click(self.CPC_LOTTERY_HALL_LOCATE['alert_comit'])

    def get_alert_text(self):
        '''
        获取弹框的提示信息
        :return:
        '''
        self.base_driver._locate_element(self.CPC_LOTTERY_HALL_LOCATE['alert'])
        text = self.base_driver.get_text(self.CPC_LOTTERY_HALL_LOCATE['alert_text'])
        return text

    def get_odd_number(self):
        '''
        获取到单号的数值
        :return:
        '''
        dr = self.base_driver._locate_element(self.CPC_LOTTERY_HALL_LOCATE['odd_number'])
        odd_number = dr.get_attribute('onclick')
        return odd_number.split('\'')[1]

    def get_lottery_name(self):
        '''
        获取下注的彩票名
        :return:
        '''
        lottery_name = self.base_driver.get_text(self.CPC_LOTTERY_HALL_LOCATE['lottery_name'])
        return lottery_name

    def get_bet_type(self):
        '''
        获取彩票的下注类型
        :return:
        '''
        bet_name = self.base_driver.get_text(self.CPC_LOTTERY_HALL_LOCATE['bet_type'])
        return bet_name


# cpclotteryhall = CpCLotteryHallPage()
