# coding=utf-8
import time
# from base.boxdriver import BoxDriver
# from app.chandao.page.chandao_bug_write_page import ChandaoBugWritePage
from app.google.google_sharesheet.save_data_to_googlesheet import SaveDataToSheet
from app.telegram.bot import TelegramBot
from loguru import logger
from base.small_tool import stool
from app.chandao.api.chandao_api import ChanDaoApi


class EventAddBug(object):

    def bug_to_chandao_data(self, valuse):
        data = {}
        data['product_chosen'] = valuse['bug_product']
        data['module_chosen'] = valuse['bug_module']
        data['assignedTo_chosen'] = valuse['bug_fixer']
        data['openedBuild_chosen'] = valuse['bug_openedbuild']
        data['bug_title'] = valuse['bug_title']
        data['bug_body'] = valuse['bug_body']
        logger.info('要保存到禅道的缺陷内容是:\n' + str(data))
        print('要保存到禅道的缺陷内容是:\n' + str(data))
        return data

    @logger.catch()
    def bug_to_chandao_data_by_api(self, valuse):
        data = {}
        data['product_chosen'] = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_product_to_number'][valuse['bug_product']]
        data['module_chosen'] = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_module_to_number'][valuse['bug_module']]
        data['assignedTo_chosen'] = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_fixer_to_username'][valuse['bug_fixer']]
        data['openedBuild_chosen'] = stool.get_config_dict_yaml['WINDOW']['BUG']['bug_openedbuild_to_number'][valuse['bug_openedbuild']]
        data['bug_title'] = valuse['bug_title']
        data['bug_body'] = valuse['bug_body']
        logger.info('要保存到禅道的缺陷内容是:\n' + str(data))
        print('要保存到禅道的缺陷内容是:\n' + str(data))
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
        print('要保存到google的缺陷内容是:\n' + str(data))
        return data

    def add_to_db(self):
        pass

    def add_bug(self, user, values):
        # 1 准备bug数据
        logger.info('\n\n--------------开始保存缺陷--------------\n\n')
        print('\n\n--------------开始保存缺陷--------------\n\n')
        data_for_google = self.bug_to_google_data(values)
        data_for_google[0][3] = user
        data_for_chandao = self.bug_to_chandao_data_by_api(values)
        # 2 执行保存到google的操作
        logger.info('\n\n--------------开始保存到google--------------\n\n')
        print('\n\n--------------开始保存到google--------------\n\n')
        try:
            SaveDataToSheet().save_bug(data_for_google)
        except:
            logger.info('保存到google失败,建议重试' + '\n')
            print('保存到google失败,建议重试' + '\n')
            pass
        # 3 执行保存到禅道的操作
        try:
            logger.info('\n\n--------------开始保存到禅道--------------\n\n')
            print('\n\n--------------开始保存到禅道--------------\n\n')
            bug_id, bug_url = ChanDaoApi().add_bug_by_api(user, **data_for_chandao)

        except Exception as msg:
            logger.info('保存到禅道失败,建议重试' + '\n')
            logger.error(msg)
            print('保存到禅道失败,建议重试' + '\n')
            print(msg)
            pass
        # finally:
        #     chanbugw.close()
        # 4 将生成的缺陷id号保存到google上
        try:
            logger.info('\n\n--------------保存缺陷ID--------------\n\n')
            print('\n\n--------------保存缺陷ID--------------\n\n')
            bug_title_data_list = SaveDataToSheet().get_values()['values']
            compare_data = values['bug_title']
            SaveDataToSheet().updata_bug_id(bug_title_data_list, compare_data, bug_id)
        except:
            pass
        # 5 将生成的缺陷链接保存到Google上
        try:
            logger.info('\n\n--------------保存缺陷URL--------------\n\n')
            print('\n\n--------------保存缺陷URL--------------\n\n')
            # bug_url = ya.get_config_dict['CHANDAO']['URL']['bug_control']['link_base_url'] + '%s.html' % bug_id
            # logger.info('缺陷URL:' + bug_url)
            SaveDataToSheet().updata_bug_url(bug_title_data_list, compare_data, bug_url)
        except:
            pass

        # 2.4.6 通知到telegram对应的开发
        try:
            logger.info('\n\n--------------通知对应处理人--------------\n\n')
            print('\n\n--------------通知对应处理人--------------\n\n')
            logger.info('要通知的处理人是:' + values['bug_fixer'])
            print('要通知的处理人是:' + values['bug_fixer'])
            # 组装通知的内容
            text = '------你有新BUG啦啦啦------\n' \
                   '提交人:' + user + '\n' \
                   '缺陷标题:\n' + compare_data + '\n' \
                   '缺陷URL:\n' \
                   + bug_url
            TelegramBot().send_to_developer_api(values['bug_fixer'], text)
        except:
            pass
