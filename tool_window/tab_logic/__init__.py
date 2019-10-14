# _*_ coding: utf-8 _*_
import PySimpleGUI as sg
from operator import itemgetter
from loguru import logger
from base.small_tool import stool
from tool_window.tab_modle.bug_tab_modle import bug_layout
from tool_window.tab_modle.testdata_tab_modle import testdata_layout
from tool_window.tab_modle.testflow_tab_modle import testflow_layout
from tool_window.tab_modle.web_tab_modle import web_layout
from tool_window.tab_modle.tool_tab_modle import tool_layout


class WindowCommonFunction(object):

    def __init__(self):
        self.account_action_list = stool.get_config_dict_yaml['WINDOW']['WEB']['account_action_list']
        self.user_list = stool.get_config_dict_yaml['WINDOW']['WEB']['user_list']
        self.ip_list = stool.get_config_dict_yaml['WINDOW']['WEB']['ip_list']
        self.work_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['work_page_list']
        self.work_accout_list = stool.get_config_dict_yaml['ACCOUNT']['cpc']['240']['长发']['account']
        self.tool_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['tool_page_list']
        self.other_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['other_page_list']
        self.URL = stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['url']
        self.bug_product = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_product']
        self.bug_module = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_module']
        self.bug_openedbuild = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_openedbuild']
        self.bug_fixer = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_fixer']
        self.bug_search = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_search']
        self.bug_change = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_change']

        ''' WINDOWS窗口布局 '''

        # 面板整体布局初始化
        layout = [
            [sg.TabGroup([[sg.Tab('网页', web_layout, key='web'), sg.Tab('缺陷', bug_layout, key='bug'),
                           sg.Tab('小工具', tool_layout, key='tool'), sg.Tab('测试数据', testdata_layout, key='testdata'),
                           sg.Tab('测试流程', testflow_layout, key='testflow')]], key='tabgroup', )],
            [sg.Output(size=(120, 30))],
            [sg.T('选择用户'), sg.Radio('长发', "RADIO2", key=u'长发'), sg.Radio('龙五', "RADIO2", key=u'龙五'),
             sg.Radio('安妮', "RADIO2", key=u'安妮'), sg.Radio('小贤', "RADIO2", key=u'小贤'),
             ],
            [sg.T('选择环境'), sg.Radio('240环境', "RADIO1", key='240'), sg.Radio('55环境', "RADIO1", key='55'),
             sg.Radio('5143环境', "RADIO1", key='5143'), sg.Radio('msg2环境', "RADIO1", key='msg2')]
        ]

        # 窗口初始化
        self.window = sg.Window('测试辅助小工具', layout, default_element_size=(12, 1))


    def ToDoItem(self, num):
        return [sg.Text(f'{num}. '), sg.CBox(''), sg.In(enable_events=True)]

    def update_account(self, user, ip, page):
        work_account_list_update = stool.get_config_dict_yaml['ACCOUNT'][page][ip][user]['account']
        logger.info('获取的用户列表是:' + str(work_account_list_update))
        print('获取的用户列表是:' + str(work_account_list_update))
        self.window.Element('account').Update(self.work_accout_list, work_account_list_update)

    def update_tool_message(self, text):
        self.window.Element('message').Update(text)

    @logger.catch()
    def append_message(self, element, text, values):
        res = values[element] + text + '\n'
        self.window.Element(element).Update(res)

    def judge_choose_woke_page(self, values):
        if values['work_page']:
            logger.info('选择的页面是:' + values['work_page'])
            print('选择的页面是:' + values['work_page'])
            return values['work_page']
        else:
            sg.Popup('请选择要操作的页面')
            return False

    @logger.catch()
    def judge_choose_radio(self, values, choose_list, key_word=None):
        # 判断是否选择了单选框中的一个且返回选择的值
        res = None
        logger.info('开始判断是否选择了' + key_word)
        print('开始判断是否选择了' + key_word)
        user_choose_status = itemgetter(*choose_list)(values)  # itemgetter方法把前一列表值当后一字典的键值来返回对应键的值,这里都是bool值的返回
        user_choose_result = any(user_choose_status)  # 判断user_choose_status中是否有一个值为True
        if user_choose_result:  # any方法判断获取结果中是否有一个为True且返回bool值
            # 1.2 获取为True的值
            res = choose_list[user_choose_status.index(True)]  # 面板是单选框类型所以只有一个为True
            logger.info('你选择的%s是:' % key_word + res)
            print('你选择的%s是:' % key_word + res)
            return res
        else:
            sg.Popup('请选择' + key_word)
            return False

    # def judge_choose_ip(self, values):
    #     ip = None
    #     ip_choose_status = itemgetter(*self.ip_list)(values)
    #     ip_choose_result = any(ip_choose_status)
    #     if ip_choose_result:
    #         ip = self.ip_list[ip_choose_status.index(True)]
    #         logger.info('选择的环境是:' + ip)
    #         # todo 根据环境和页面的选择查询过呢更新对应账号,也许不好实现
    #         # 2.1.2 执行登录页面操作
    #         return ip
    #     else:
    #         sg.Popup('请选择环境')
    #         return False
    #
    # def judge_choose_user(self, values):
    #     user = None
    #     logger.info('开始判断是否选择了用户')
    #     user_choose_status = itemgetter(*self.user_list)(values)  # itemgetter方法把前一列表值当后一字典的键值来返回对应键的值,这里都是bool值的返回
    #     user_choose_result = any(user_choose_status) # 判断user_choose_status中是否有一个值为True
    #     if user_choose_result:  # any方法判断获取结果中是否有一个为True且返回bool值
    #         # 1.2 获取为True的用户名
    #         user = self.user_list[user_choose_status.index(True)]  # 面板是单选框类型所以只有一个为True
    #         logger.info('你选择的用户是:' + user)
    #         return user
    #     else:
    #         sg.Popup('请选择用户')
    #         return False


