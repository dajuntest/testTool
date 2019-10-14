import PySimpleGUI as sg

from tool_window.tab_logic.testdata_tab_logic.testdata_tab_logic import EventControlTestData
from tool_window.tab_modle.bug_tab_modle import bug_layout
from tool_window.tab_modle.testdata_tab_modle import testdata_layout
from tool_window.tab_modle.testflow_tab_modle import testflow_layout
from tool_window.tab_modle.web_tab_modle import web_layout
from tool_window.tab_modle.tool_tab_modle import tool_layout
from tool_window.tab_logic.web_tab_logic.web_tab_logic import EventControlWeb
from tool_window.tab_logic.bug_tab_logic.bug_tab_logic import EventControlBug
from tool_window.tab_logic.tool_tab_logic.tool_tab_logic import EventControlTool
# from tool_window.tab_logic.testflow_tab_logic.testflow_tab_logic import event_control_testflow


# todo 添加测试数据tab标签页
# todo 添加安全测试tab标签页
class TestPanel(object):

    def __init__(self, window):
        # 事件循环到退出为止
        while True:
            event, values = window.Read(timeout=3600000)
            tab = window.Element('tabgroup').Get()
            print(event, values)
            try:
                if tab == 'web':
                    EventControlWeb().event_control_web(event, values)
                if tab == 'bug':
                    EventControlBug().event_control_bug(event, values)
                if tab == 'tool':
                    EventControlTool().event_control_tool(event, values)
                if tab == 'testdata':
                    EventControlTestData().event_control_testdata(event, values)
                # if tab == 'testflow':
                #     event_control_testflow(event, values)
            except:
                pass
            if event is None:  # always,  always give a way out!
                break
        window.Close()