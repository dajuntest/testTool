import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from time import sleep
import codecs



def read_txt(file):

    f = open(file, encoding='utf-8')
    res = f.read()
    f.close()
    return res


class EmailTool(object):

    def send_by_plain(self, file):
        # 发送者的用户名和密码,服务器地址
        user = 'dajun.test@gmail.com'
        password = 'heli84327'

        # 发送者邮箱和接收者邮箱
        sender = 'dajun.test@gmail.com'
        # receiver 可以是一个list
        receiver = ['xiaokeep@outlook.com','dajun_test@outlook.com',]

        # 构造纯文本邮件内容
        text = read_txt(file)
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = Header('戚长发', 'utf-8')
        subject = '%s日报-彩票组' % time.strftime('%Y%m%d', time.localtime(time.time()))
        msg['subject'] = Header(subject, 'utf-8')

        # 发送消息
        smtp = smtplib.SMTP('smtp.gmail.com:587')  # 实例化SMTP对象
        smtp.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        smtp.starttls()
        smtp.login(user, password)  # 登陆smtp服务器
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送邮件 ，这里有三个参数

        #关闭连接
        smtp.close()

if __name__ == '__main__':
    # print(read_txt('dayReport.txt'))
    EmailTool().send_by_plain('dayReport.txt')