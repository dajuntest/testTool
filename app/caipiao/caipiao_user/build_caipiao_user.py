import random

from app.caipiao.caipiao_cpc.api.cpc_h5_api import CPC_Api
from app.mongdb.base_fun.base_function import BaseMongoFun
from base.small_tool import stool
from test.auto_test.test_data.create_user_data import UserBuilder
from loguru import logger



class BuildCaipiaoUser(object):

    def __init__(self):
        self.ubuild = UserBuilder

    @logger.catch()
    def build_cpc_user(self, user, ip, collection='cpc_account', values=None):
        # 格式换账号名称,ip + Q + 三位随机数组合  Q前端 H后端
        # todo 如果是又聊天室角色名称是另外一种格式
        account = ip[:2] + 'Q' + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        # 通过测试数据生成工厂生成格式化测试数据
        user_data = (self.ubuild.with_user_name(user).with_ip(ip).with_id(account).build())['userdata']
        # 调用api接口生成数据
        ip_address = stool.get_config_dict_yaml['BASE']['server'][ip]
        for i in range(6):
            res = CPC_Api(ip_address).create_account_no_regerrer(**user_data)
            if res != '验证码错误':
                # 保存数据资料到mangodb中
                BaseMongoFun().insert_one(collection, user_data)
                break
            i += 1

    def save_cpc_user2mongo(self, user, ip, collection='cpc_account, values=None'):
        pass # todo 保存一些账号基本信息到mongo
        # 获取一些基本信息再进行保存

    def build_mgw_user(self):
        pass



# if __name__ == '__main__':
#     BuildCaipiaoUser().build_cpc_user('长发', '55')