import PySimpleGUI as sg
from base.small_tool import stool

work_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['work_page_list']
work_accout_list = stool.get_config_dict_yaml['ACCOUNT']['cpc']['240']['长发']['account']
account_action_list = stool.get_config_dict_yaml['WINDOW']['WEB']['account_action_list']
tool_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['tool_page_list']
other_page_list = stool.get_config_dict_yaml['WINDOW']['WEB']['other_page_list']


web_frame1 = [
    [sg.Text('工作网页'),
     sg.InputCombo(work_page_list, size=(18, 1), key='work_page', default_value=' ', enable_events=True),
     sg.Text('选择账号'),
     sg.InputCombo(work_accout_list, size=(19, 1), key='account', default_value=' ', )],
    [sg.Button('执行', key='open_work_page', size=(8, 1))],
]
web_frame2 = [
    [sg.Text('工具网页'), sg.InputCombo(tool_page_list, size=(18, 1), key='tool_page', default_value=' '),
     sg.Text('其他网页'), sg.InputCombo(other_page_list, size=(19, 1), key='other_page', default_value=' ')],
]

web_layout = [
    [sg.Frame('工作网页', web_frame1, key='work_web_frame')],
    [sg.Frame('其他网页(选中即执行)', web_frame2, key='other_web_frame', size=(50, 20))]
]