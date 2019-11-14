# encoding=utf-8

import jieba

seg_list = jieba.cut("假如账号输入55hy04而且密码输入1234567而且验证码输入")  # 默认是精确模式
print(", ".join(seg_list))


