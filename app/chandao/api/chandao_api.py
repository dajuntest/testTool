#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup
from loguru import logger
from base.small_tool import stool


class ChanDaoApi(object):

    def __init__(self, account='长发'):
        self.sessionid = self._get_sessionid()
        self._login(account)

    @logger.catch()
    def add_bug_by_api(self, **kwargs):
            # 提交缺陷
            url_add_bug = "http://pms.27o1.cn/zentao/bug-create-1-0.json"
            payload = {
                'assignedTo': kwargs['assignedTo_chosen'],  # todo 这个参数怎么传还要看下
                'title': kwargs['bug_title'],
                'steps': kwargs['bug_body'].replace('\n', '<br\>'),
                'product': kwargs['product_chosen'],
                'module': kwargs['module_chosen'],
                'openedBuild[]': kwargs['openedBuild_chosen']
            }
            querystring = {"zentaosid": self.sessionid}
            requests.request("POST", url_add_bug, data=payload, params=querystring)


            #获取缺陷id和缺陷url
            logger.info('缺陷提交成功')
            print('缺陷提交成功')
            url_bug_id = "http://pms.27o1.cn/zentao/bug-browse-1-0-unclosed-0-id_desc.html"
            response = requests.request("GET", url_bug_id, params=querystring)
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

    def _login(self, account):
        url = "http://pms.27o1.cn/zentao/user-login.html"
        querystring = {"zentaosid": self.sessionid}
        account1 = stool.get_config_dict_yaml['ACCOUNT']['chandao'][account]['account']
        password = stool.get_config_dict_yaml['ACCOUNT']['chandao'][account]['password']
        payload = {'account': account1, 'password': password}
        requests.request("POST", url, data=payload, params=querystring)

    @logger.catch()
    def get_image_url(self, image_path):
        url = "http://pms.27o1.cn/zentao/file-ajaxUpload-5d9c2cf057318.html"
        headers = {
            'Cookie': "za=dajun; zentaosid=%s" % self.sessionid,
        }
        querystring = {"dir": "image", "zentaosid": self.sessionid}
        payload = {
            'localUrl': image_path
        }
        files = {'imgFile': ('bug_image.png', open(image_path, 'rb'), 'image/png', {})}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring, files=files).json()
        url = 'http://pms.27o1.cn' + response['url']
        logger.info('生成的图片链接为:\n' + url)
        print('生成的图片链接为:\n' + url)
        return url


if __name__ == '__main__':
    chandao = ChanDaoApi()
    chandao.get_image_url('../../../test/image/bug_image.png')
