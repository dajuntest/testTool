#coding=utf-8
from behave import *
from base.webaction import WebAction
from app.cp01_h5_old import Cp01H5OldTotalPage


web = WebAction(Cp01H5OldTotalPage)


@step(u'"{账号}"输入"{element}"')
def step_impl(context):
    web.get('https://555.0234.co/mobile/studio/#/login').input('account_input')


@step(u'密码输入')
def step_impl(context):
    web.input('password_input')


@step(u'验证码输入')
def step_impl(context):
    pass


@step(u'点击登录按钮')
def step_impl(context):
    pass


@step(u'登录成功')
def step_impl(context):
    pass


# @step("账号输入")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 假如账号输入')
#
#
# @step("密码输入")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 而且密码输入')
#
#
# @step("验证码输入")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 而且验证码输入')
#
#
# @step("点击登录按钮")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 当点击登录按钮')
#
#
# @step("登录成功")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 那么登录成功')
#
#
# @step("士大夫撒旦")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: 假如士大夫撒旦')