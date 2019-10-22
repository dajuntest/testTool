from app.caipiao.caipiao_mgw.api.mgw_api import MGW_Api
from base.small_tool import stool
import PySimpleGUI as sg

class EventAccountAction(object):

    def account_action(self, ip, values):
        ip_address = stool.get_config_dict_yaml['BASE']['server'][ip]
        account = values['testdata_tab_account']
        if values['account_action'] == '获取账号信息':
            MGW_Api(ip_address).get_user_info(account)
        if values['account_action'] == '修改用户打码量':
            amount = sg.popup_get_text('输入数量,正数是加,负数是减')
            MGW_Api(ip_address).control_user_bet(account, amount)
        if values['account_action'] == '手动加减款':
            amount = sg.popup_get_text('输入数量,正数是加,负数是减')
            MGW_Api(ip_address).add_money(account, amount)