import PySimpleGUI as sg


tool_frame = [
    [sg.In('请输入英文', key='translate', size=(23, 1)), sg.Button('翻译', key='c2e', size=(5, 1))],
    [sg.In('请输入时间戳', key='time', size=(23, 1)), sg.Button('转换', key='timestamp', size=(5, 1))],
    [sg.In('请输入JSON', key='json', size=(23, 1)), sg.Button('转换', key='json_beatiful', size=(5, 1))],
    [sg.In('逗号分割环境和查询语句', key='sql', size=(23, 1)), sg.Button('SQL', key='sql_action', size=(5, 1))],
    [sg.Button('截图', key='cut_page', size=(5, 1)), sg.Button('步骤记录', key='step_recode', size=(5, 1))]
]

tool_layout = [
    [sg.Frame('', tool_frame, key='tool_web_frame'), sg.T(' '),
     sg.Multiline('这里会显示操作结果:', key='message', size=(28, 11))]
]