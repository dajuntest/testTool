import requests
import telebot
from base.small_tool import stool
from loguru import logger

TOKEN = stool.get_config_dict_yaml['TELEGRAM']['bot']['bot_one']['token']
# todo 以更安全的方式进行保存token

class TelegramBot(object):

    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)

    def send_to_developer(self, developer, text):
        chat_id = (str(stool.get_config_dict_yaml['TELEGRAM']['user'][developer]).split(','))[0]
        chat_firstname = (str(stool.get_config_dict_yaml['TELEGRAM']['user'][developer]).split(','))[1]
        self.bot.send_message(chat_id, text)
        logger.info('通知-*-%s-*-成功' % chat_firstname)
        print('通知-*-%s-*-成功' % chat_firstname)

    def send_to_developer_api(self, developer, text):
        url = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN
        chat_id = (str(stool.get_config_dict_yaml['TELEGRAM']['user'][developer]).split(','))[0]
        chat_firstname = (str(stool.get_config_dict_yaml['TELEGRAM']['user'][developer]).split(','))[1]
        querystring = {"chat_id": chat_id, "text": text}
        requests.request("POST", url, params=querystring)
        logger.info('通知-*-%s-*-成功' % chat_firstname)
        print('通知-*-%s-*-成功' % chat_firstname)


if __name__ == '__main__':
    compare_data = '测试下'
    url = 'https://www.baidu.com'
    text = '------你有新BUG啦啦啦------\n' \
           '缺陷标题:' + compare_data + '\n' \
           '缺陷URL:\n' \
           + url


    # TelegramBot().send_to_developer(u'L:测试-龙五', text)
    TelegramBot().send_to_developer_api(u'D:测试-戚长发', text)
    print((str(stool.get_config_dict_yaml['TELEGRAM']['user'][u'L:测试-龙五']).split(','))[0])
    print((TelegramBot().bot.get_updates())[1])