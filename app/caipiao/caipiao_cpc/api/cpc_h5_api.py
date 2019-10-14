#coding=utf-8
import requests
from loguru import logger
from base.small_tool import stool
import json


class CPC_Api(object):

    def __init__(self, ip, account='55hy04', password='1234567'):
        self.ip = ip
        self.account = account
        self.password = password

    # 获取验证码
    def _get_verify_code(self):
        try:
            url = "http://" + self.ip + "/passport/validate_image.do"
            verify_code = None
            response = requests.request("POST", url).json()
            if response:
                image_base64 = (str((response)['data']).split(','))[1]
                verify_code = stool.get_verify_number_by_baiduocr_bs64(image_base64)
                return verify_code
            else:
                verify_code = '1234'
        except:
            verify_code = '1234'

    # 登录所需的session
    def _get_session_and_temporary(self):
        # 获取sessionid和temporaryid
        url = "https://" + self.ip + "/passport/distribute_sessionid.do"
        headers = {'X-Requested-With': "XMLHttpRequest", 'Content-Type': "application/json"}
        response = requests.request("GET", url, headers=headers).json()
        sessionid = (response)['data']['sessionid']
        temporaryid = (response)['data']['temporaryId']
        logger.info('获取登录session成功:\n' + sessionid + '\n' + temporaryid)
        return sessionid, temporaryid

    # 登录操作
    def login(self):
        # 登录点击操作
        verify_code = self._get_verify_code()
        sessionid, temporaryid = self._get_session_and_temporary()
        url = "http://" + self.ip + "/passport/login.do"
        payload = "{'account': %s, 'password': %s, 'headImg': %s}" % (self.account, self.password, verify_code)
        headers = {
            'temporary-sessionId': temporaryid,
            'Accept': "application/json, text/plain, */*",
            'X-Requested-With': "XMLHttpRequest",
            'sessionid': sessionid,
            'openId': "xiniv2318656f042749ee3a04a8275e458d2dd",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        logger.info('登录操作成功')
        print(response.text)
        return sessionid

    # 获取邀请码列表
    def get_invite_code_list(self):
        sessionid = self.login()
        url = "http://" + self.ip + "/agent/lottery_share/list.do"
        payload = "{count: 15, offset: 0, total: 1, role: 1}"
        headers = {
            'sessionid': sessionid,
        }
        response = requests.request("POST", url, data=payload, headers=headers).json()
        print(json.dumps(response, indent=2))

    # 常见邀请码
    def create_invita_code(self):
        sessionid, temporaryid = self._get_session_and_temporary()
        url = "http://" + self.ip + "/agent/lottery_share/add.do"
        payload = "{role: 1,FrequentLottery: 7,QuickThree: 7,ElevenPickFive: 7,Three: 7,PCEggs: 7,PK10: 7,SixMark: 7,SevenStar: 7}"
        headers = {
            'sessionid': sessionid,
            'cache-control': "no-cache",
            'Postman-Token': temporaryid
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        return self.get_invite_code_list()

    '''用户基本信息'''

    # 获取用户信息
    def check_status(self):
        sessionid = self.login()
        url = "http://" + self.ip + "/passport/check_status.do"
        headers = {'sessionid': sessionid}
        response = requests.request("POST", url, headers=headers).json()
        print(response)
        return response






    '''创建用户'''

    # 无邀请码创建用户
    def create_account_no_regerrer(self, **kwargs):
        sessionid, temporaryid = self._get_session_and_temporary()
        verify_code = self._get_verify_code()
        print(verify_code)
        url = "http://" + self.ip + "/passport/register.do"
        # payload = {
        #     'account': kwargs['_id'],
        #     'password': kwargs['password'],
        #     'repassword': kwargs['password'],
        #     'verifyImg': kwargs['verify_code']
        # }
        payload = "{'account': %s,'password': %s,'repassword': %s,'verifyImg': %s}"\
                  % (kwargs['_id'], kwargs['password'], kwargs['password'], verify_code)
        headers = {
            'temporary-sessionId': temporaryid,
            'X-Requested-With': "XMLHttpRequest",
            'sessionid': sessionid,
            # 'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, data=payload, headers=headers).json()
        print(response['msg'])
        return response['msg']

    # 有邀请码创建用户
    def create_account_with_regerrer(self, **kwargs):
        verify_code = self._get_verify_code()
        sessionid, temporaryid = self._get_session_and_temporary()
        url = "http://" + self.ip + "/passport/register.do"
        payload = {
            'account': kwargs['_id'],
            'password': kwargs['password'],
            'repassword': kwargs['password'],
            'verifyImg': verify_code,
            'real_name': 'asd',
            'qq': '8758321',
            'phone': '13928573234',
            'wechat': '8294jsjer',
            'referrer': '65281811'
        }
        headers = {
            'temporary-sessionId': temporaryid,
            'X-Requested-With': "XMLHttpRequest",
            'sessionid': sessionid,
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


if __name__ == '__main__':
#     kwargs = {
#                 "_id": "cesi3331",
#                 "password": "123456",
#                 "verify_code": "4500"
#     }
#
    CPC_Api('555.0234.co').check_status()
