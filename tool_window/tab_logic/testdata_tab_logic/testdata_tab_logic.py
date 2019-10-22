#coding=utf-8
import PySimpleGUI as sg
from tool_window.tab_logic import WindowCommonFunction
from tool_window.tab_logic.testdata_tab_logic.event_account_action import EventAccountAction
from tool_window.tab_logic.testdata_tab_logic.event_create_account import EventCreateAccount


class EventControlTestData(WindowCommonFunction):

    def event_control_testdata(self, event, values):
        # 1.前置条件
        # 判断是否选择了用户,有了用户才能方便执行其他流程
        user = self.judge_choose_radio(values, self.user_list, '用户')
        if user:
            # 2 判断是否选择了环境:
            ip = self.judge_choose_radio(values, self.ip_list, '环境')
            # 2.1 账号信息变更
            if event == 'account_action':
                if ip and values['testdata_tab_account']:
                    EventAccountAction().account_action(ip, values)
                else:
                    sg.Popup('请输入账号')
            # 2.2 账号创建
            if event == 'account_create':
                EventCreateAccount().create_account(user, ip)

