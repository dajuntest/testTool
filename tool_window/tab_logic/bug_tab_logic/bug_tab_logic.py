#coding=utf-8

from tool_window.tab_logic.web_tab_logic.event_open_work_page import EventOpenWorkPage
from base.boxdriver import BoxDriver




def event_control_bug(self, event, values):
    # 1.前置条件
    # 判断是否选择了用户,有了用户才能方便执行其他流程
    user = self.judge_choose_user(values)
    if user:


    # 2. 各类型事件操作流程
    # 2.1 打开功能网页的流程
        if event == 'work_page' or event == 'open_work_page' or event == 'account_action':
            # 2.1.1 先要判断选择了环境和网页没:
            ip, page = self.judge_choose_ip(values), self.judge_choose_woke_page(values)
            if ip and page:
                # 2.1.2 获取账号事件 说明中指出要先执行才能获取对应账号,在代码中就不写了
                if event == 'work_page':
                    # 执行更新测试账号的操作
                    self.update_account(user, ip, page)
                # 2.1.3 打开网页事件
                if event == 'open_work_page':
                    EventOpenWorkPage(BoxDriver()).open_work_page(user, ip, page, values)
                    # if page == '彩票PC':
                    #     self.auto_login(BoxDriver()).login_cpc(user, ip, values['account'])
                    # elif page == '彩票H5':
                    #     self.auto_login(BoxDriver()).login_cpc_h5(user, ip, values['account'])
                    # elif page == '彩票管理':
                    #     self.auto_login(BoxDriver()).login_cpm(user, ip, values['account'])
                if event == 'account_action':
                    if values['account']:
                        if values['account_action'] == '获取账号信息':
                            MGW_Api(ip).get_user_info(values['account'])
                        elif values['account_action'] == '修改用户打码量':
                            amout = sg.PopupGetText('请输入金额:正值是增加,负值是减少')
                            MGW_Api(ip).control_user_bet(values['account'], amout)
                        elif values['account_action'] == '手动加减款':
                            amout = sg.PopupGetText('请输入要加多少钱')
                            MGW_Api(ip).add_money(values['account'], amout)


    # 2.2 打开工具页面的流程
        if event == 'open_tool_page':
            url_name = values['tool_page']
            url = self.URL[url_name]
            self._open_url(url)

    # 2.3 打开其他页面的流程
        if event == 'open_other_page':
            url_name = values['other_page']
            url = self.URL[url_name]
            self._open_url(url)

