import PySimpleGUI as sg
from tool_window.tab_modle.bug_tab_modle import bug_layout
from tool_window.tab_modle.testflow_tab_modle import testflow_layout
from tool_window.tab_modle.web_tab_modle import web_layout
from tool_window.tab_modle.tool_tab_modle import tool_layout
from tool_window.tab_logic.web_tab_logic.web_tab_logic import EventControlWeb
from tool_window.tab_logic.bug_tab_logic.bug_tab_logic import event_control_bug
from tool_window.tab_logic.tool_tab_logic.tool_tab_logic import EventControlTool
from tool_window.tab_logic.testflow_tab_logic.testflow_tab_logic import event_control_testflow

# todo 添加测试数据tab标签页
# todo 添加安全测试tab标签页
def test_panel():

    sg.ChangeLookAndFeel('GreenTan')

    '''整体页面布局 '''

    # 面板整体布局初始化
    layout = [
        [sg.TabGroup([[sg.Tab('网页', web_layout, key='web'), sg.Tab('缺陷', bug_layout, key='bug'),
                       sg.Tab('小工具', tool_layout, key='tool'),
                       sg.Tab('测试流程', testflow_layout, key='testflow')]])],
        [sg.Output(size=(73, 18))],
        [sg.T('选择用户'), sg.Radio('长发', "RADIO2", key=u'长发'), sg.Radio('龙五', "RADIO2", key=u'龙五'),
         sg.Radio('安妮', "RADIO2", key=u'安妮')
         ]
    ]

    ''' WINDOWS窗口布局 '''

    # 窗口初始化
    window = sg.Window('测试辅助小工具', layout, default_element_size=(12, 1))

    # 事件循环到退出为止
    while True:
        event, values = window.Read(timeout=1800000)
        print(event, values)
        tab = layout[0][0].Get()
        try:
            if tab == 'web':
                EventControlWeb().event_control_web(event, values)
            if tab == 'bug':
                event_control_bug(event, values)
            if tab == 'tool':
                EventControlTool().event_control_tool(event, values)
            if tab == 'testflow':
                event_control_testflow(event, values)
        except:
            pass
        if event is None:  # always,  always give a way out!
            break
    window.Close()
