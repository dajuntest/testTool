#coding=utf-8
from behave import *
from base.webaction import WebAction
from app.cp01_h5_old import Cp01H5OldTotalPage

web = WebAction(Cp01H5OldTotalPage)

@step(u'测试')
def step_impl(context):
    web.get('123123').input('dfsfsdfs')


