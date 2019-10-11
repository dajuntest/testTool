import requests
from loguru import logger

class MGW_Api(object):

    def __init__(self, ip):
        # 获取登录sessionid和temporaryid
        self.ip = ip
        url = "https://" + ip + "/passport/distribute_sessionid.do"
        headers = {'X-Requested-With': "XMLHttpRequest", 'Content-Type': "application/json"}
        response = requests.request("GET", url, headers=headers).json()
        self.sessionid = (response)['data']['sessionid']
        temporaryid = (response)['data']['temporaryId']
        logger.info('获取登录session成功:\n' + self.sessionid + '\n' + temporaryid)

        #获取登录token
        url = "http://" + ip + "/passport/manage_login.do"
        payload = "{'account': 'dajunadmin', 'password': '123456'}"
        headers = {
            'temporary-sessionId': temporaryid,
            'Content-Type': "application/json",
            'X-Requested-With': "XMLHttpRequest",
            'sessionid': self.sessionid,
        }
        response = requests.request("POST", url, data=payload, headers=headers).json()
        token = response['data']
        logger.info('获取登录token成功:\n' + token)

        # 登录点击操作
        url = "http://" + ip + "/passport/login_validate.do"
        payload = {'accessToken': token}
        requests.request("POST", url, data=payload)
        logger.info('登录操作成功')

    def add_money(self, account, amount):
        url = "http://" + self.ip + "/manage/finance/manual_cash_transfer.do"
        payload = "{'type': 7, 'amount': %s, 'remark': '1', 'needDoRecord': 'false', 'account': %s, 'ratio': 0}" % (amount, account)
        headers = {'sessionid': self.sessionid}
        response = requests.request("POST", url, data=payload, headers=headers)
        logger.info(response.text)

    def control_user_bet(self, account, amount):
        url = "https://" + self.ip + "/manage/finance/add_or_subtract_bet_num.do"
        payload = "{'account': %s, 'amount': %d, 'remark': 'ceshi'}" % (account, amount)
        headers = {
            'sessionid': self.sessionid
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        logger.info('修改用户打码量成功')
        return self.get_user_info(account)

    def get_user_info(self, account):
        url = "https://" + self.ip + "/manage/finance/get_user_info.do"
        payload = "{'account':%s}" % account
        headers = {'sessionid': self.sessionid}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        logger.info('账户余额:' + str(response['data']['balance']))
        logger.info('当前打码量:' + str(response['data']['betNumCurrent']))
        logger.info('所需打码量:' + str(response['data']['betNumNeed']))


if __name__ == '__main__':
    MGW_Api('555.0234.co').control_user_bet('55dl10', 1)