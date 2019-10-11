#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup

class ChanDaoApi(object):

    def add_bug(self, user, **kwargs):
        # 获取sessionid
        sessionid = self._get_sessionid()

        # 提交缺陷
        url_add_bug = "http://pms.27o1.cn/zentao/bug-create-1-0.json"
        payload = {
            'assignedTo': kwargs['assignedTo_chosen'],
            'title': kwargs['bug_title'],
            'steps': kwargs['bug_body'],
            'product': kwargs['product_chosen'],
            'module': kwargs['module_chosen'],
            'openedBuild[]': kwargs['openedBuild_chosen']
        }
        headers = {
            'Cookie': "za=%s; zentaosid=%s;" % (user, sessionid),
        }
        requests.request("POST", url_add_bug, data=payload, headers=headers)

        #获取缺陷id和缺陷url
        url_bug_id = "http://pms.27o1.cn/zentao/bug-browse-1-0-unclosed-0-id_desc.html"
        response = requests.request("GET", url_bug_id, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.select('#bugList > tbody > tr > td.c-id.cell-id > a')
        bug_id = data[0].get_text()
        bug_url = 'http://pms.27o1.cn' + str(data[0].get('href'))
        return bug_id, bug_url


    def _get_sessionid(self):
        url = "http://pms.27o1.cn/zentao/api-getSessionID.json"
        response = requests.request("GET", url).json()
        sessionid = (json.loads(response['data']))['sessionID']
        return sessionid


    def get_image_url(self):
        #获取session
        sessionid = self._get_sessionid()

        url = "http://pms.27o1.cn/zentao/file-ajaxUpload-5d9c2cf057318.html"
        headers = {
            'Cookie': "za=dajun; zentaosid=%s" % sessionid,
        }
        querystring = {"dir": "image"}
        payload = {
            'localUrl': 'D:\\bug_image\\1.png'
        }
        files = {'imgFile': ('1.png', open('D:\\bug_image\\1.png', 'rb'), 'image/png', {})}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring, files=files).json()
        url = response['url']
        return url


if __name__ == '__main__':
    ChanDaoApi.get_image_url()