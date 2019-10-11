import telebot
from base.box import ya
from loguru import logger

TOKEN = ya.get_config_dict['TELEGRAM']['bot']['bot_one']['token']
# todo 以更安全的方式进行保存token

class TelegramBot(object):

    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)

    def send_to_developer(self, developer, text):
        chat_id = (str(ya.get_config_dict['TELEGRAM']['user'][developer]).split(','))[0]
        chat_firstname = (str(ya.get_config_dict['TELEGRAM']['user'][developer]).split(','))[1]
        self.bot.send_message(chat_id, text)
        logger.info('通知-*-%s-*-成功' % chat_firstname)


if __name__ == '__main__':
    compare_data = '测试下'
    url = 'https://www.baidu.com'
    text = '------你有新BUG啦啦啦------\n' \
           '缺陷标题:' + compare_data + '\n' \
           '缺陷URL:\n' \
           + url


    TelegramBot().send_to_developer(u'L:测试-龙五', text)
    TelegramBot().send_to_developer(u'D:测试-戚长发', text)
    # print((str(ya.get_config_dict['TELEGRAM']['user'][u'L:测试-龙五']).split(','))[0])
    # print((TelegramBot().bot.get_updates())[1])