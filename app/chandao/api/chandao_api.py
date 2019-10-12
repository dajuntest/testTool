#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup
from loguru import logger
from base.small_tool import stool


class ChanDaoApi(object):

    @logger.catch()
    def add_bug_by_api(self, user, **kwargs):
        # try:
            # 获取sessionid
            sessionid = self._get_sessionid()

            # 提交缺陷
            url_add_bug = "http://pms.27o1.cn/zentao/bug-create-1-0.json"
            payload = {
                'assignedTo': kwargs['assignedTo_chosen'],  # todo 这个参数怎么传还要看下
                'title': kwargs['bug_title'],
                'steps': kwargs['bug_body'],
                'product': kwargs['product_chosen'],
                'module': kwargs['module_chosen'],
                'openedBuild[]': kwargs['openedBuild_chosen']
            }
            # user = user.encode('utf-8').decode('latin1')
            user = stool.get_config_dict_yaml['ACCOUNT']['chandao'][user]['account']
            headers = {'Cookie': "za=%s; zentaosid=%s;" % (user, 'gimvlkomh2pne4vp8gd26j9q16')}  # todo 做成根据账号可变的
            requests.request("POST", url_add_bug, data=payload, headers=headers)

            #获取缺陷id和缺陷url
            logger.info('缺陷提交成功')
            print('缺陷提交成功')
            url_bug_id = "http://pms.27o1.cn/zentao/bug-browse-1-0-unclosed-0-id_desc.html"
            response = requests.request("GET", url_bug_id, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.select('#bugList > tbody > tr > td.c-id.cell-id > a')
            bug_id = data[0].get_text()
            bug_url = 'http://pms.27o1.cn' + str(data[0].get('href'))
            logger.info('生成的缺陷url:' + bug_url)
            print('生成的缺陷url:' + bug_url)
            return bug_id, bug_url

    def _get_sessionid(self):
        url = "http://pms.27o1.cn/zentao/api-getSessionID.json"
        response = requests.request("GET", url).json()
        sessionid = (json.loads(response['data']))['sessionID']
        return sessionid

    def _login(self):
        pass

    def get_image_url(self):
        #获取session
        sessionid = self._get_sessionid()

        url = "http://pms.27o1.cn/zentao/file-ajaxUpload-5d9c2cf057318.html"
        headers = {
            'Cookie': "za=dajun; zentaosid=%s" % sessionid,
        }
        querystring = {"dir": "image"}
        payload = {
            # 'localUrl': 'D:\\bug_image\\1.png'
            'localUrl': 'C:\\Users\\dajun\\Pictures\\Camera Roll\\1.png'
        }
        files = {'imgFile': ('1.png', open('C:\\Users\\dajun\\Pictures\\Camera Roll\\1.png', 'rb'), 'image/png', {})}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring, files=files).json()
        url = response['url']
        logger.info('生成的图片链接为:\n' + url)
        print('生成的图片链接为:\n' + url)
        return url

    # def add_byg_by_web(self):
    #
    #     driver = BoxDriver()
    #     ChandaoLoginPage(driver).open_login_url()
    #     account, password = ChandaoLoginPage(driver).get_account(user)
    #     ChandaoLoginPage(driver).login(account, password)
    #     chanbugw = ChandaoBugWritePage(driver)
    #     bug_id = chanbugw.add_bug_simple(**data_for_chandao)


# if __name__ == '__main__':
#     data = {'product_chosen': '彩票01', 'module_chosen': '/前台优化', 'assignedTo_chosen': 'D:测试-戚长发', 'openedBuild_chosen': '主干', 'bug_title': '必1填', 'bug_body': '[步骤]\n\n[结果]\n\n[期望]\n\n截图在小工具中,粘贴生成url:\n\n\n'}
#     user = '长发'.encode('utf-8').decode('latin1')
#     print(ChanDaoApi().add_bug(user, **data))