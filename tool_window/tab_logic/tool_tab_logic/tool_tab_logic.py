#coding=utf-8
from app.chandao.api.chandao_api import ChanDaoApi
from base.small_tool import stool
from tool_window.tab_logic import WindowCommonFunction


class EventControlTool(WindowCommonFunction):

    def event_control_tool(self, event, values):
        # 翻译流程
        if event == 'c2e':
            text = stool.english2chinese(values['translate'])
            self.update_tool_message(text)
        # 时间戳转换
        if event == 'timestamp':
            text = stool.timestamp_to_time(int(values['time']))
            self.update_tool_message(text)
        # json格式化
        if event == 'json_beatiful':
            text = stool.json_beauty(values['json'])
            self.update_tool_message(text)
        # 截图
        if event == 'cut_page':
            image_file = stool.cut_screeon_image()
            image_url = ChanDaoApi().get_image_url(image_file)
            self.update_tool_message(image_url)
            self.append_message('bug_body', image_url, values)
        # 步骤记录
        if event == 'step_recode':
            stool.prs_exe()
        # 下载二维码
        if event == 'apk_download':
            pass # todo

