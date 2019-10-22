#coding=utf-8
from behave import *
from base.driver_tool import WebAction

WebAction.page.login_account_input


@given(u'账号输入{account}')
def step_impl(context, account):
    WebAction.with_open('https://555.0234.co/pc/index.html').with_input(WebAction.page.login_account_input, account)

@given(u'密码输入{password}')
def step_impl(context, password):
    WebAction.with_input(WebAction.page.login_password_input, password)

@given(u'输入验证码')
def step_impl(context):
    pass

@when(u'点击 登录按钮')
def step_impl(context):
    pass

@then(u'登录成功')
def step_impl(context):
    pass

