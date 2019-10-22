#coding=utf-8
from tool_window.tab_logic import WindowCommonFunction
from tool_window.tab_logic.web_tab_logic.event_open_work_page import EventOpenWorkPage
from base.boxdriver import BoxDriver


class EventControlWeb(WindowCommonFunction):


    def event_control_web(self, event, values):
        # 1.前置条件
        # 判断是否选择了用户,有了用户才能方便执行其他流程
        user = self.judge_choose_radio(values, self.user_list, '用户')
        if user:
        # 2.1 打开功能网页的流程
            if event in ('work_page', 'open_work_page', 'account_action'):
                # 2.1.1 先要判断选择了环境和网页没:
                ip, page = self.judge_choose_radio(values, self.ip_list, '环境'), self.judge_choose_woke_page(values)
                if ip and page:
                    # 2.1.2 获取账号事件 说明中指出要先执行才能获取对应账号,在代码中就不写了
                    if event == 'work_page':
                        # 执行更新测试账号的操作
                        self.update_account(user, ip, page)
                    # 2.1.3 打开网页事件
                    if event == 'open_work_page':
                        EventOpenWorkPage(BoxDriver()).open_work_page(user, ip, page, values)


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

