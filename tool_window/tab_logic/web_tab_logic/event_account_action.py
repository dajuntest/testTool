# coding=utf-8
from app.caipiao.caipiao_cpc.page.login_page import CpCLoginPage
from app.caipiao.caipiao_cpc.page.login_page_h5 import CpCLoginPageH5
from app.caipiao.caipiao_mgw.page.login_page import CpMLoginPage
from base.boxdriver import BoxDriver
from app.caipiao.caipiao_mgw.api.mgw_api import MGW_Api
import PySimpleGUI as sg


class EventAccountAction(object):

    @staticmethod
    def account_action(ip, values):
        if values['account']:
            if values['account_action'] == '获取账号信息':
                MGW_Api(ip).get_user_info(values['account'])
            elif values['account_action'] == '修改用户打码量':
                amout = sg.PopupGetText('请输入金额:正值是增加,负值是减少')
                MGW_Api(ip).control_user_bet(values['account'], amout)
            elif values['account_action'] == '手动加减款':
                amout = sg.PopupGetText('请输入要加多少钱')
                MGW_Api(ip).add_money(values['account'], amout)
        else:
            sg.PopupGetText('请选择账号')