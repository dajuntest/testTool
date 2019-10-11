#coding=utf-8
import requests
from loguru import logger
from base.box import get_verify_number_by_baiduocr_bs64
import json

class CPC_Api(object):

    def __init__(self, ip, account=None, password='123456'):
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
                verify_code = get_verify_number_by_baiduocr_bs64(image_base64)
            else:
                verify_code = '1234'
        except:
            verify_code = '1234'

    def _get_session_and_temporary(self):
        # 获取sessionid和temporaryid
        url = "https://" + self.ip + "/passport/distribute_sessionid.do"
        headers = {'X-Requested-With': "XMLHttpRequest", 'Content-Type': "application/json"}
        response = requests.request("GET", url, headers=headers).json()
        sessionid = (response)['data']['sessionid']
        temporaryid = (response)['data']['temporaryId']
        logger.info('获取登录session成功:\n' + sessionid + '\n' + temporaryid)
        return sessionid, temporaryid

        #获取登录token
        # url = "http://" + ip + "/passport/manage_login.do"
        # payload = "{'account': 'dajunadmin', 'password': '123456'}"
        # headers = {
        #     'temporary-sessionId': temporaryid,
        #     'Content-Type': "application/json",
        #     'X-Requested-With': "XMLHttpRequest",
        #     'sessionid': self.sessionid,
        # }
        # response = requests.request("POST", url, data=payload, headers=headers).json()
        # token = response['data']
        # logger.info('获取登录token成功:\n' + token)

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

    def get_invite_code_list(self):
        sessionid = self.login()
        url = "http://" + self.ip + "/agent/lottery_share/list.do"
        payload = "{count: 15, offset: 0, total: 1, role: 1}"
        headers = {
            'sessionid': sessionid,
        }
        response = requests.request("POST", url, data=payload, headers=headers).json()
        print(json.dumps(response, indent=2))

    # , name, password, verify_num = '1234', qq = None, wechat = None, regerrer = None, real_name = None
    def create_account(self):
        sessionid, temporaryid = self._get_session_and_temporary()
        url = "http://" + self.ip + "/passport/register.do"
        payload = "{'account': 'ceshi1234','password': '123456','repassword': '123456','verifyImg': '1234','real_name': 'asd',qq: '8758321',phone: '13928573234','wechat': '8294jsjer',referrer: '65281811'}"
        headers = {
            'temporary-sessionId': temporaryid,
            'X-Requested-With': "XMLHttpRequest",
            'sessionid': sessionid,
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)

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

if __name__ == '__main__':
    CPC_Api('555.0234.co').create_account()
