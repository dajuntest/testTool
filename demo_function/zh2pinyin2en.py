import pinyin.cedict

# 转拼音
# nǐhǎo
# print(pinyin.get('你好'))
#
# # ni hao
# print(pinyin.get('你好', format="strip", delimiter=" "))
#
# # ni3hao3
# print(pinyin.get('你好', format="numerical"))

# 获取首字母 n h
print((pinyin.get_initial('彩票01-H5-V1')).replace(' ', ''))

# # 转英文
# # ['you (informal, as opposed to courteous 您[nin2])']
# print(pinyin.cedict.translate_word('你'))
#
# # ['Hello!', 'Hi!', 'How are you?']
# print(pinyin.cedict.translate_word('模块'))
#
# # [['你', ['you (informal, as opposed to courteous 您[nin2])']], ['你好', ['Hello!', 'Hi!', 'How are you?']], ['好', ['to be fond of', 'to have a tendency to', 'to be prone to']]]
# print(list(pinyin.cedict.all_phrase_translations('注册模块')))
#
# #获取首字母并转为大写 Z
# print(pinyin.get_initial("注册模块")[0].upper())