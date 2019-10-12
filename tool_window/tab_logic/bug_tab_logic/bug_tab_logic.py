#coding=utf-8
from app.google.google_sharesheet.save_data_to_googlesheet import SaveDataToSheet
from tool_window.tab_logic import WindowCommonFunction
from base.boxdriver import BoxDriver
from loguru import logger
from tool_window.tab_logic.bug_tab_logic.event_add_bug import EventAddBug


class EventControlBug(WindowCommonFunction):

    def event_control_bug(self, event, values):
        # 1.前置条件
        # 判断是否选择了用户,有了用户才能方便执行其他流程
        user = self.judge_choose_radio(values, self.user_list, '用户')
        if user:
            # 2.提交缺陷的流程
            if event == 'add_bug':
                EventAddBug().add_bug(user, values)