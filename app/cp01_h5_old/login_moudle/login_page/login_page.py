#coding=utf-8
from poium import Page, PageElement

class LoginPage(Page):

    elementid = PageElement(xpath="osdjlkdgja", describe='测试')

    login_page_url = '/mobile/studio/#/index'
    account_input = PageElement(xpath="//input[@placeholder='请输入账号']", describe='账号')
    password_input = PageElement(xpath="//input[@placeholder='请输入密码']", describe='密码')
    verify_number_button = PageElement(xpath="//div[@id='code']//img", describe='验证码按钮')
    verify_number_input = PageElement(xpath="//input[@placeholder='请输入验证码(区分大小写)']", describe='验证码输入框')
    login_button = PageElement(xpath="//div[@class='redBtn'][contains(.,'登录')]", describe='登录按钮')
    register_button = PageElement(xpath="//div[@class='whitBtn'][contains(.,'下载App')]", describe='下载App')