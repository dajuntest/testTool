#coding=utf-8
import PySimpleGUI as sg
from tool_window.tab_logic import WindowCommonFunction


testflow_frame = [WindowCommonFunction().ToDoItem(x) for x in range(1, 6)] + [[sg.Button('Save'), sg.Button('Exit')]]

testflow_layout = [
    [sg.Frame('测试流程todo', testflow_frame)]
]