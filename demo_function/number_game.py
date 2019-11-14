# import random
#
#
# class NumberGame(object):
#
#     def __init__(self):
#         self.right_number = random.randint(0, 1024)
#         self.user = input('请输入用户名:')
#         self.guess_time = 0
#         self.input_history = []
#
#     def play_game(self):
#         while True:
#             guess_number = int(input('请输入猜测的数字:'))
#             if guess_number == self.right_number:
#                 if self.guess_time < 4:
#                     print('恭喜你猜对了')
#                     self.input_history.append(self.user+','+str(self.guess_time)+','+str(guess_number))
#                     break
#                 if self.guess_time >= 4:
#                     print('很遗憾,超过3次,游戏结束')
#                     break
#             if guess_number > self.right_number:
#                 if guess_number == 3:
#                     print('游戏中断')
#                     break
#                 elif guess_number == 1:
#                     print('你猜大了')
#                     self.guess_time += 1
#                     self.input_history.append(self.user + ',' + str(self.guess_time) + ',' + str(guess_number))
#                     print(self.input_history)
#                 elif self.guess_time == 3:
#                     print('游戏结束')
#                 else:
#                     print('你猜大了')
#                     self.guess_time += 1
#                     self.input_history.append(self.user + ',' + str(self.guess_time) + ',' + str(guess_number))
#             if guess_number < self.right_number:
#                 if guess_number == 3:
#                     print('游戏中断')
#                     break
#                 elif guess_number == 1:
#                     print('你猜小了')
#                     self.guess_time += 1
#                     self.input_history.append(self.user + ',' + str(self.guess_time) + ',' + str(guess_number))
#                     print(self.input_history)
#                 elif self.guess_time == 3:
#                     print('游戏结束')
#                 else:
#                     print('你猜小了')
#                     self.guess_time += 1
#                     self.input_history.append(self.user + ',' + str(self.guess_time) + ',' + str(guess_number))
#
#
# if __name__ == '__main__':
#     NumberGame().play_game()

# import re
#
# a = '我的密码是:12345asdfadsf你帮我记住'
# print(re.findall('(:.*?)你', a))

from selenium import webdriver
from PIL import Image



class demo():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')

    def cut_element_screen(self):
        self.driver.save_screenshot(self.cut_element_screen.__name__ + '.png')
        element = self.driver.find_element_by_id("su")
        print(element.location)                # 打印元素坐标
        print(element.size)                    # 打印元素大小

        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        im = Image.open(self.cut_element_screen.__name__ + '.png')
        im = im.crop((left, top, right, bottom))
        im.save(self.cut_element_screen.__name__ + '.png')

if __name__ == '__main__':
    demo().cut_element_screen()