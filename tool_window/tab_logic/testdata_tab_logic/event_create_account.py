from app.caipiao.caipiao_mgw.api.mgw_api import MGW_Api
from app.caipiao.caipiao_user.build_caipiao_user import BuildCaipiaoUser
from base.small_tool import stool
import PySimpleGUI as sg

class EventCreateAccount(object):

    def create_account(self, user, ip, values):
        ip_address = stool.get_config_dict_yaml['BASE']['server'][ip]
        account = values['testdata_tab_account']
        if values['create_account'] == '1:1代理3层':
            BuildCaipiaoUser().build_1to1_agent_3level(user, ip)
