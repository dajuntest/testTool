# import os
#
# res =  os.system('C:\\Windows\\System32\\SnippingTool.exe')
#
# print(res)

#
from pywinauto.application import Application
# from pywinauto.keyboard import SendKeys
from pywinauto.keyboard import send_keys
from pywinauto import findwindows
import time
#
app = Application(backend="uia").start("C:\\Windows\\System32\\SnippingTool.exe")
# app.top_window()
title_snip = u'截图工具'
title_save = u'另存为'
app[title_snip].wait('visible', timeout=10)
send_keys('^' + 'n')
time.sleep(30)
a = findwindows.find_window(title_save)
print(a)


# app[title_save].wait('visible', timeout=30)
# print(app[title_save].print_control_identifiers())
app[title_save]['保存'].click()
# app[title_notepad].menu_select('新建')
# print(app[title_notepad].print_control_identifiers())
# app.window().menu_select(u'新建')
# print(app.active())active

#_*_coding=utf-8_*_
import pywinauto
from pywinauto.mouse import *
from pywinauto.keyboard import *
import time
#1.运行记事本程序
app = pywinauto.Application().start('notepad.exe')
#2.窗体选择
title_notepad = u'无标题-记事本'
#3.选择一个菜单项
app[title_notepad].menu_select('帮助->关于记事本')
time.sleep(3)
#4.点击新弹出窗体的确定按钮
out_note=u'关于记事本'
button_name_ok='确定'
app[out_note][button_name_ok].click()
#5.查看一个窗体含有的控件，子窗体，菜单
print(app[title_notepad].print_control_identifiers())
#-------------------无标题记事本的含有的控件，子窗体，菜单-----------------
# Control Identifiers:
#
# Notepad - '无标题 - 记事本'    (L8, T439, R892, B815)
# ['无标题 - 记事本Notepad', 'Notepad', '无标题 - 记事本']
# child_window(title="无标题 - 记事本", class_name="Notepad")
#    |
#    | Edit - ''    (L16, T490, R884, B807)
#    | ['无标题 - 记事本Edit', 'Edit']
#    | child_window(class_name="Edit")
#    |
#    | StatusBar - ''    (L16, T785, R884, B807)
#    | ['StatusBar', '无标题 - 记事本StatusBar', 'StatusBar   第 1 行，第 1 列']
#    | child_window(class_name="msctls_statusbar32")
# None

#6.在记事本中输入一些文本
#[tips-> ctrl+点击鼠标左键快速查看被调用函数]
app.title_notepad.Edit.type_keys('pywinauto works!\n',with_spaces=True,with_newlines=True)
app.title_notepad.Edit.type_keys('hello word !\n',with_spaces=True,with_newlines=True)
#7.选择编辑菜单->编辑时间/日期
# app[title_notepad].menu_select('编辑->时间/日期(&d)')
#8.连接已运行程序
#如连接微信 借助spy++找到运行程序的handle
app1=pywinauto.Application(backend='uia').connect(handle=0x00320830)
#9.查看运行窗口窗体名称
print(app1.window())
print(app1['Dialog'].print_control_identifiers())
# Dialog - '微信'    (L968, T269, R1678, B903)
# ['微信Dialog', 'Dialog', '微信']
# child_window(title="微信", control_type="Window")
#    |
#    | Pane - 'ChatContactMenu'    (L-10000, T-10000, R-9999, B-9999)
#    | ['ChatContactMenu', 'ChatContactMenuPane', 'Pane', 'Pane0', 'Pane1']
#    | child_window(title="ChatContactMenu", control_type="Pane")
#    |    |
#    |    | Pane - ''    (L-10019, T-10019, R-9980, B-9980)
#    |    | ['', 'Pane2', '0', '1']
#    |
#    | Pane - ''    (L948, T249, R1698, B923)
#    | ['2', 'Pane3']
# None
#10.通过路径去打开一个已有程序
#11.鼠标控制
x=0
y=0
for i in range(20):
    step_x = i*8
    step_y = i*5
    move(coords=(step_x,step_y ))
    time.sleep(1)

#12.键盘控制
#键盘对应的ascii http://www.baike.com/wiki/ASCII
#发送键盘指令,打开命令行，输入一条命令for /l %i in (1,1,100) do tree
send_keys('{VK_LWIN}')
send_keys('cmd')
send_keys('{VK_RETURN}')
time.sleep(3)
send_keys('for /L +5i in +9 1,1,100+0 do tree {VK_RETURN}',with_spaces=True)


