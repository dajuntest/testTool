#coding=utf-8
from behave import *
from base.driver_tool import WebAction


@given(u'账号输入 55hy04')
def step_impl1(context, account=None):
    WebAction.with_open('https://555.0234.co/pc/index.html').with_input('55hy04')
    # pass

@given(u'密码输入 1234567')
def step_impl(context, password=None):
    WebAction.with_input('1234567')
    # pass

@given(u'输入验证码')
def step_impl(context):
    pass

@when(u'点击 登录按钮')
def step_impl(context):
    pass

@then(u'登录成功')
def step_impl(context):
    pass

if __name__ == '__main__':
    step_impl1()

