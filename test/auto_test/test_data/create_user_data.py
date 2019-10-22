# codind=utf-8
from collections import OrderedDict
import json
import faker

#
# f=faker.Faker(locale='zh-CN') #需要指定国家，生成的数据是根据中国进行生成，比如电话号码等
#
# print(dir(f)) #打印对象可用的所有方法
#
# print(f.file_name()) #随机生成文件名称
# print(f.province()) #随机生成省份
# print(f.password()) #随机生成密码
# print(f.name()) #随机生成名字
# print(f.image_url()) #随机生成图片连接
# print(f.email()) #随机生成邮箱
# print(f.country()) #随机生成国家名称
# print(f.city()) #随机生成城市名称
# print(f.date()) #随机生成时间
# print(f.ssn()) #随机生成证件名称
#
# # fake=Faker() #默认生成美国英文数据
# fake=Faker(locale='zh_CN')
#
# # 地址类
# print("地址类".center(20,"-"))
# print(fake.address())#海南省成市丰都深圳路p座 425541
# print(fake.street_address())#深圳街X座
# print(fake.street_name())#长沙路
# print(fake.city_name(),fake.city())#兰州 贵阳市  (相差“市”)
# print(fake.province())#陕西省
#
#
# #公司类：
# print("公司类".center(20,"-"))
# print(fake.company())#惠派国际公司信息有限公司
# print(fake.company_suffix())#网络有限公司
# print(fake.company_prefix())#鑫博腾飞
#
# #个人信息类
# print("个人信息类".center(20,"-"))
# print(fake.name())#东浩
# print(fake.simple_profile())
# #{'username': 'leihan', 'name': '武帅', 'sex': 'F', 'address': '吉林省淮安市双滦家街C座 210434', 'mail': 'lishao@hotmail.com', 'birthdate': '1988-11-12'}
# print(fake.user_name(),fake.password(special_chars=False))#ajiang zI2QbHy02p
#
# #文章类
# print("文章类".center(20,"-"))
# print(fake.word())#当前
# print(fake.words(3))#['欢迎', '支持', '图片']
# print(fake.sentence(3))#精华有关一些.
# print(fake.paragraph())#大家电话空间一起操作图片要求.上海发展到了之间用户也是的人.必须记者关系介绍注册.用户时候投资发布.

# 地址信息类：
# fake.address()：完整地址，比如海南省成市丰都深圳路p座
# 425541
# fake.street_address()：街道 + 地址，比如兴城路A座
# fake.street_name()：街道名，比如宜都街
# fake.city_name()：城市名, 比如兰州
# fake.city()：城市, 比如兰州市
# fake.province()：省份名, 比如陕西省
# fake.postcode()：邮编
# fake.country()：国家
#
# 公司信息类：
# fake.company()：公司名，比如惠派国际公司信息有限公司
# fake.company_suffix()：公司名后缀(公司性质)，比如网络有限公司
# fake.company_prefix()：公司名前缀，比如鑫博腾飞
#
# 日期类：
# fake.date(pattern="%Y-%m-%d", end_datetime=None)
# fake.year()：随机年份
# fake.day_of_week()：随机星期数
# fake.time(pattern="%H:%M:%S", end_datetime=None)：随机时间
#
# 网络类：
# fake.company_email()：企业邮箱
# fake.email(): 邮箱
#
# 个人信息类：
# fake.name()：姓名
#
# fake.user_name(*args, **kwargs)：用户名，只是随机的英文姓名组合，一般是6位
# fake.phone_number()：电话号码
# fake.simple_profile(sex=None)：简略个人信息，包括用户名，姓名，性别，地址，邮箱，出生日期。比如
# {'username': 'chao', 'name': '胡秀兰', 'sex': 'M', 'address': '宁夏回族自治区玉市沙湾宁德路t座 873713', 'mail': 'uxiao@yahoo.com',
#  'birthdate': '1998-06-12'}
# fake.profile(fields=None, sex=None)：详略个人信息，比简略个人信息多出公司名、血型、工作、位置、域名等等信息。
# fake.password()：密码
# 参数选项：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母。
# 默认情况：length = 10, special_chars = True, digits = True, upper_case = True, lower_case = True
# fake.job()：工作
#
# 文章类：
# fake.word(ext_word_list=None)：随机词语
# ext_word_list可以是一个列表，那么词语会从列表中取
# fake.words(nb=3, ext_word_list=None)：随机多个词语
# nb是数量，对于words来说是返回多少个词语
# fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)：随机短语（会包括短语结束标志点号）
# fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)：随机段落
# fake.paragraphs(nb=3, ext_word_list=None)：多个随机段落
#
# 数据类型类：
# fake.pystr(min_chars=None, max_chars=20)：自定义长度的随机字符串
# fake.pyint(): 随机整数


# todo 生成一般边界值的测试数据:长度,格式校验(电话,身份证,),数字,字母,大小写,中文,特殊字符
from app.mongdb.base_fun.base_function import BaseMongoFun


class User(object):
    contentDict = OrderedDict()
    dataDict = OrderedDict()

    def __init__(self):
        self.dataDict['_id'] = ''
        self.dataDict['account_type'] = ''
        self.dataDict['ip'] = ''
        self.dataDict['user_name'] = ''
        self.dataDict['password'] = ''
        self.dataDict['agent_number'] = ''
        self.dataDict['agency_level'] = ''
        self.dataDict['chat_room_role'] = ''
        self.dataDict['balance'] = ''
        self.dataDict['other_balance'] = ''
        self.dataDict['bet_number'] = ''
        self.dataDict['bankcard'] = ''
        self.dataDict['bankcard_password'] = ''
        self.dataDict['name'] = ''
        self.dataDict['QQ'] = ''
        self.dataDict['phone_number'] = ''
        self.dataDict['weixin'] = ''
        self.dataDict['invita_code'] = ''
        self.dataDict['invita_code_information'] = ''
        self.dataDict['account_description'] = ''
        self.contentDict['userdata'] = self.dataDict

    def get_id(self):
        return self.dataDict['_id']

    def set_id(self, account):
        self.dataDict['_id'] = account

    def get_account_type(self):
        return self.dataDict['account_type']

    def set_account_type(self, account_type):
        self.dataDict['account_type'] = account_type

    def get_ip(self):
        return self.dataDict['ip']

    def set_ip(self, ip):
        self.dataDict['ip'] = ip

    def get_user_name(self):
        return self.dataDict['user_name']

    def set_user_name(self, user_name):
        self.dataDict['user_name'] = user_name

    def get_password(self):
        return self.dataDict['password']

    def set_password(self, password):
        self.dataDict['password'] = password

    def get_agent_number(self):
        return self.dataDict['agent_number']

    def set_agent_number(self, agent_number):
        self.dataDict['agent_number'] = agent_number

    def get_agency_level(self):
        return self.dataDict['agency_level']

    def set_agency_level(self, agency_level):
        self.dataDict['agency_level'] = agency_level

    def get_chat_room_role(self):
        return self.dataDict['chat_room_role']

    def set_chat_room_role(self, chat_room_role):
        self.dataDict['chat_room_role'] = chat_room_role

    def get_balance(self):
        return self.dataDict['balance']

    def set_balance(self, balance):
        self.dataDict['balance'] = balance

    def get_other_balance(self):
        return self.dataDict['other_balance']

    def set_other_balance(self, other_balance):
        self.dataDict['other_balance'] = other_balance

    def get_bet_number(self):
        return self.dataDict['bet_number']

    def set_bet_number(self, bet_number):
        self.dataDict['bet_number'] = bet_number

    def get_bankcard(self):
        return self.dataDict['bankcard']

    def set_bankcard(self, bankcard):
        self.dataDict['bankcard'] = bankcard

    def get_bankcard_password(self):
        return self.dataDict['bankcard_password']

    def set_bankcard_password(self, bankcard_password):
        self.dataDict['bankcard_password'] = bankcard_password

    def get_name(self):
        return self.dataDict['name']

    def set_name(self, name):
        self.dataDict['name'] = name

    def get_QQ(self):
        return self.dataDict['QQ']

    def set_QQ(self, QQ):
        self.dataDict['QQ'] = QQ

    def get_phone_number(self):
        return self.dataDict['phone_number']

    def set_phone_number(self, phone_number):
        self.dataDict['phone_number'] = phone_number

    def get_weixin(self):
        return self.dataDict['weixin']

    def set_weixin(self, weixin):
        self.dataDict['weixin'] = weixin

    def get_invita_code(self):
        return self.dataDict['invita_code']

    def set_invita_code(self, invita_code):
        self.dataDict['invita_code'] = invita_code

    def get_invita_code_information(self):
        return self.dataDict['invita_code_information']

    def set_invita_code_information(self, invita_code_information):
        self.dataDict['invita_code_information'] = invita_code_information

    def get_account_description(self):
        return self.dataDict['account_description']

    def set_account_description(self, account_description):
        self.dataDict['account_description'] = account_description


class UserBuilder(object):
    user = User()

    @classmethod
    def with_id(cls, account):
        cls.user.set_id(account)
        return cls

    @classmethod
    def with_account_type(cls, account_type):
        cls.user.set_account_type(account_type)
        return cls

    @classmethod
    def with_ip(cls, ip):
        cls.user.set_ip(ip)
        return cls

    @classmethod
    def with_user_name(cls, user_name):
        cls.user.set_user_name(user_name)
        return cls

    @classmethod
    def with_password(cls, password):
        cls.user.set_password(password)
        return cls

    @classmethod
    def with_agency_number(cls, agency_number):
        cls.user.set_agency_number(agency_number)
        return cls

    @classmethod
    def with_agency_level(cls, agency_level):
        cls.user.set_agency_level(agency_level)
        return cls

    @classmethod
    def with_chat_room_role(cls, chat_room_role):
        cls.user.set_chat_room_role(chat_room_role)
        return cls

    @classmethod
    def with_balance(cls, balance):
        cls.user.set_balance(balance)
        return cls

    @classmethod
    def with_other_balance(cls, other_balance):
        cls.user.set_other_balance(other_balance)
        return cls

    @classmethod
    def with_bet_number(cls, bet_number):
        cls.user.set_bet_number(bet_number)
        return cls

    @classmethod
    def with_bankcard(cls, bankcard):
        cls.user.set_bankcard(bankcard)
        return cls

    @classmethod
    def with_bankcard_password(cls, bankcard_password):
        cls.user.set_bankcard_password(bankcard_password)
        return cls

    @classmethod
    def with_name(cls, name):
        cls.user.set_name(name)
        return cls

    @classmethod
    def with_QQ(cls, QQ):
        cls.user.set_QQ(QQ)
        return cls

    @classmethod
    def with_phone_number(cls, phone_number):
        cls.user.set_phone_number(phone_number)
        return cls

    @classmethod
    def with_weixin(cls, weixin):
        cls.user.set_weixin(weixin)
        return cls

    @classmethod
    def with_invita_code(cls, invita_code):
        cls.user.set_invita_code(invita_code)
        return cls

    @classmethod
    def with_invita_code_information(cls, invita_code_information):
        cls.user.set_invita_code_information(invita_code_information)
        return cls

    @classmethod
    def with_account_description(cls, account_description):
        cls.user.set_account_description(account_description)
        return cls

    @classmethod
    def build(cls):
        f_cn = faker.Faker(locale='zh-CN')
        if not cls.user.get_id():
            cls.user.set_id(f_cn.user_name()[:6])
        if not cls.user.get_password():
            cls.user.set_password('123456')
        if not cls.user.get_ip():
            cls.user.set_ip('55')
        return json.loads(json.dumps(cls.user.contentDict, default=lambda o: o.__dict__, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    testdata = ((UserBuilder.build())['userdata'])
    BaseMongoFun().insert_one([''])