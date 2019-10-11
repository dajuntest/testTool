# coding=utf-8
import time
from base.box import BoxDriver
from bot.google.save_data_to_googlesheet import SaveDataToSheet
from biz.chandao.chandao_bug_write_page import ChandaoBugWritePage
from loguru import logger

class AddBug(object):

    def bug_to_chandao_data(self, valuse):
        data = {}
        data['product_chosen'] = valuse['bug_product']
        data['module_chosen'] = valuse['bug_module']
        data['assignedTo_chosen'] = valuse['bug_fixer']
        data['openedBuild_chosen'] = valuse['bug_openedbuild']
        data['bug_title'] = valuse['bug_title']
        data['bug_body'] = valuse['bug_body']
        logger.info('要保存到禅道的缺陷内容是:\n' + str(data))
        return data

    def bug_to_google_data(self, valuse):
        bug_id = 'null'
        bug_title = valuse['bug_title']
        bug_fixer = valuse['bug_fixer']
        bug_tester = 'null'
        bug_status = u'打开'
        bug_product = valuse['bug_product']
        bug_moudle = valuse['bug_module']
        bug_openedbuild = valuse['bug_openedbuild']
        bug_open_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        bug_close_time = 'null'
        bug_body = valuse['bug_body']
        bug_link = 'null'
        data = [[bug_id, bug_title, bug_fixer, bug_tester, bug_status, bug_product, bug_moudle, bug_openedbuild,
                  bug_open_time, bug_close_time, bug_body, bug_link]]
        logger.info('要保存到google的缺陷内容是:\n' + str(data))
        return data

    def add_to_google(self, data):
        SaveDataToSheet().save_bug(data)

    def add_to_chandao(self, data):
        ChandaoBugWritePage(BoxDriver()).add_bug_simple(data)

    def add_to_db(self):
        pass