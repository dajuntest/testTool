import PySimpleGUI as sg
from base.small_tool import stool


account_action_list = stool.get_config_dict_yaml['WINDOW']['WEB']['account_action_list']
account_create_list = stool.get_config_dict_yaml['WINDOW']['WEB']['account_create_list']

testdata_frame1 = [
    [sg.Button('前端'), sg.Button('后台'), sg.Button('生产')],
    [sg.Text('账号后台操作')],
    [sg.Text('账号'),
     sg.InputText('', size=(21, 1), key='testdata_tab_account')],
    [sg.Text('操作'),
     sg.InputCombo(account_action_list, size=(18, 1), key='account_action', default_value=' ', enable_events=True)],
]

testdata_layout = [
    [sg.Frame('', testdata_frame1, key='testdata_frame'),
    sg.Multiline('这里会显示操作结果:', key='message', size=(28, 11))],
    [sg.Text('账号生成'),
     sg.InputCombo(account_create_list, size=(18, 1), key='account_create', default_value=' ', enable_events=True)]
]