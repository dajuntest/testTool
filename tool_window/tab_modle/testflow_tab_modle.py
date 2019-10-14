#coding=utf-8
import PySimpleGUI as sg
# from tool_window.tab_logic import WindowCommonFunction


testflow_frame = [[sg.Button('Save'), sg.Button('Exit')]]  # [WindowCommonFunction().ToDoItem(x) for x in range(1, 6)] +

testflow_layout = [
    [sg.Frame('测试流程todo', testflow_frame)]
]