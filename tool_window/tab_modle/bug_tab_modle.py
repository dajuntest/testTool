import PySimpleGUI as sg
from base.small_tool import stool

sg.ChangeLookAndFeel('GreenTan')

bug_product = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_product']
bug_module = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_module']
bug_openedbuild = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_openedbuild']
bug_fixer = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_fixer']
bug_search = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_search']
bug_change = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_change']


bug_body_default = '[步骤]\n\n' \
                   '[结果]\n\n' \
                   '[期望]\n\n' \
                   '截图在小工具中,粘贴生成url:\n' \
                   '\n'
bug_frame = [
    [sg.Text('产品'), sg.InputCombo(bug_product, size=(11, 1), key='bug_product' ,),
     sg.Text('模块'), sg.InputCombo(bug_module, size=(11, 1), key='bug_module', default_value=' ')],
    [sg.Text('版本'), sg.InputCombo(bug_openedbuild, size=(11, 1), key='bug_openedbuild'),
     sg.Text('开发'), sg.InputCombo(bug_fixer, size=(11, 1), key='bug_fixer', default_value=' ')],
    [sg.Text('标题'), sg.InputText('必填', size=(29, 2), key='bug_title'), sg.Button('提交', key='add_bug')],
    [sg.Multiline(default_text=bug_body_default, size=(39, 6), key='bug_body')]
]
bug_frame2 = [
    [sg.Text('查操作', justification='center')],
    [sg.InputOptionMenu(bug_search, size=(13, 1), key='bug_search', default_value=' ')],
    [sg.T('')],
    [sg.Text('改操作', justification='center')],
    [sg.InputText('输入缺陷ID', size=(13, 1))],
    [sg.T('')],
    [sg.InputOptionMenu(bug_change, size=(13, 1), key='bug_change' ,default_value=' ')],
]

bug_layout = [
    [sg.Frame('增', bug_frame, ), sg.Frame('查与改', bug_frame2, size=(10, 15))]
]