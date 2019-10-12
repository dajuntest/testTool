#coding=utf-8
from base.basepage import BasePage
from base.small_tool import stool
from time import sleep


class ChandaoBugControl(BasePage):

    CHANDAO_BUG_CONTROL_LOCATE = stool.get_config_dict_yaml['CHANDAO']['LOCATION']['bug_contrl']
    URL = stool.get_config_dict_yaml['URL']

    def find_bug_id(self, bug_title):

        '''
        获取缺陷在禅道平台的id号
        :param bug_title:
        :return:bug_id
        '''

        bug_id = ''
        bug_product_url_lists = [self.CHANDAO_BUG_CONTROL_LOCATE['bug_product_lists_base_url'] + i for i in str(self.CHANDAO_BUG_CONTROL_LOCATE['bug_product_id_lists']).split(',')]
        self.base_driver.navigate(self.URL['bug_control']['all_bug_url'])  # 进入查看所有缺陷的页面
        # self.base_driver.click(self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_button'])  # 点击搜索打开搜索栏
        for i in bug_product_url_lists:
            self.base_driver.navigate(i)
            sleep(2)
            self.base_driver.select_by_index(self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_operator1_or'], self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_operator1_or_value'])  # 选择第一组条件为包含
            self.base_driver.type(self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_operator1_value'], bug_title)# 输入缺陷标题
            self.base_driver.select_by_index(self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_operator_andor'], self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_operator_andor_value'])  # 选择多条间是并且关系
            self.base_driver.click(self.CHANDAO_BUG_CONTROL_LOCATE['bug_search_submit_button'])  # 点击搜索按钮
            sleep(2)
            try:
                print(self.base_driver.get_text(self.CHANDAO_BUG_CONTROL_LOCATE['bug_id']))
                bug_id += self.base_driver.get_text(self.CHANDAO_BUG_CONTROL_LOCATE['bug_id'])
            except:
                print('Not found this bug')
        return bug_id

    def find_bug_link(self, bug_id):
        '''
        :param bug_id:
        :return: bug_link
        '''
        # bug的链接可以直接拼接得到
        bug_link = self.URL['bug_control']['link_base_url'] + str(bug_id)
        return bug_link

    def find_bug_status(self, bug_link):
        self.base_driver.navigate(bug_link)
        sleep(1)
        bug_status =  self.base_driver.get_text(self.CHANDAO_BUG_CONTROL_LOCATE['bug_status'])
        return bug_status

    def close_bug(self, bug_link):
        self.base_driver.navigate(bug_link)
        sleep(1)
        self.base_driver.click(self.CHANDAO_BUG_CONTROL_LOCATE['bug_close_button'])
        sleep(1)
        self.base_driver.select_by_index(self.CHANDAO_BUG_CONTROL_LOCATE['bug_resolution_select'], self.CHANDAO_BUG_CONTROL_LOCATE['bug_resolution_select_value'])
        self.base_driver.click(self.CHANDAO_BUG_CONTROL_LOCATE['bug_resolution_submit'])

    def get_products(self):
        pass
        # todo 获取到所有的单独项目名方便遍历获取缺陷id

    def test(self):
        self.base_driver.navigate('http://msg2.0234.co/mgw/login')
        self.base_driver.type('x,//*[@id="account"]','admin')
        self.base_driver.type('x,//*[@id="password"]','123456')
        self.base_driver.click('x,//*[@id="app"]/div/div[2]/div[3]/form/div[3]/div/div/span/button')
        self.base_driver.forced_wait(2)
        print(self.base_driver.window_handles())
        # self.base_driver._locate_element('x,//*[@id="abId0.37190198505005334"]').type('x,//*[@id="abId0.37190198505005334"]/input', '123')

# chanbugcon = ChandaoBugControl()
# chanbugcon.test()

#abId0\.3882290392259462 > input