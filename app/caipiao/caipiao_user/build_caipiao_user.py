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
    def build_cpc_user(self, user, ip, collection='cpc_account', account=None, agent_number=None):
        # 格式换账号名称,ip + Q + 三位随机数组合  Q前端 H后端
        if account == None:
            # todo 如果是又聊天室角色名称是另外一种格式
            account = ip[:2] + 'Q' + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

        # 通过测试数据生成工厂生成格式化测试数据
        if agent_number == None:
            user_data = (self.ubuild.with_user_name(user).with_ip(ip).with_id(account).build())['userdata']
        else:
            user_data = (self.ubuild.with_user_name(user).with_ip(ip).with_id(account).with_agency_number(agent_number).build())['userdata']
        # 调用api接口生成数据
        ip_address = stool.get_config_dict_yaml['BASE']['server'][ip]
        for i in range(6):
            res = CPC_Api(ip_address).create_account_no_regerrer(**user_data)
            if res != '验证码错误':
                # 保存数据资料到mangodb中
                BaseMongoFun().insert_one(collection, user_data)
                break
            i += 1

    # 创建代理用户: 1:1代理三层 (1:1指一个上级只有一个直属下级,三层指包括自己在内的三层代理)
    def build_1to1_agent_3level(self, user, ip):
        # 创建总代理账号,格式化创建ip+d+构建编号+0
        build_result = {}  # 保存构建结果
        agent_base = ip[:2] + 'd' + str(random.random(9)) + str(random.random(9)) + str(random.random(9))
        ip_address = stool.get_config_dict_yaml['BASE']['server'][ip]
        return_percentage = 9

        # 总代账号登录创建邀请码
        general_agent = agent_base + str('0')
        self.build_cpc_user(user, ip, collection='cpc_account', account=general_agent)
        cpc_g = CPC_Api(ip_address, account=general_agent)
        cpc_g.create_invita_code(str(return_percentage))
        invitation_code = cpc_g.get_invite_code_list()
        build_result['总代'] = {'账号': general_agent, '邀请码': invitation_code}

        # 用总代的邀请码注册一级代理账号且给出邀请码
        level1_agent = agent_base + str('1')
        self.build_cpc_user(user, ip, collection='cpc_account', account=level1_agent, agent_number=invitation_code)
        cpc_1 = CPC_Api(ip_address, account=level1_agent)
        cpc_1.create_invita_code(str(return_percentage-1))
        invitation_code_1 = cpc_1.get_invite_code_list()
        build_result['一级代理'] = {'账号': level1_agent, '邀请码': invitation_code_1}

        # 用一级代理创建二级代理且给出代理邀请码
        level2_agent = agent_base + str('2')
        self.build_cpc_user(user, ip, collection='cpc_account', account=level2_agent, agent_number=invitation_code)
        cpc_2 = CPC_Api(ip_address, account=level2_agent)
        cpc_2.create_invita_code(str(return_percentage-2))
        invitation_code_2 = cpc_2.get_invite_code_list()
        build_result['二级代理'] = {'账号': level2_agent, '邀请码': invitation_code_2}

        return build_result

    def save_cpc_user2mongo(self, user, ip, collection='cpc_account, values=None'):
        pass # todo 保存一些账号基本信息到mongo
        # 获取一些基本信息再进行保存

    def build_mgw_user(self):
        pass


# if __name__ == '__main__':
#     BuildCaipiaoUser().build_cpc_user('长发', '55')