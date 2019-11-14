#coding=utf-8
from selenium import webdriver
from poium import Page, PageElement

class CpCHomePage(Page):
    cpchp_login_account_input = PageElement(xpath="//input[@placeholder='账号']", describe='账号')
    cpchp_login_password_input = PageElement(xpath="//input[@placeholder='密码']", describe='密码')
    cpchp_verify_number_button = PageElement(xpath="//div[@class='code-boxs']//img", describe='验证码按钮')
    cpchp_verify_number_input = PageElement(xpath="//input[@placeholder='验证码']", describe='验证码输入框')
    cpchp_login_button = PageElement(xpath="//button[contains(.,'登录')]", describe='登录按钮')
    cpchp_register_button = PageElement(xpath="//button[contains(.,'立即注册')]", describe='注册按钮')

    popup = PageElement(xpath="//button[@class='btn_ok bg-col'][contains(.,'确定')]", describe='弹框') # todo 归到其他类中去


if __name__ == '__main__':
    # cpc = CpCHomePage(webdriver.Chrome())
    # cpc.get('https://555.0234.co/pc/index.html')
    # for i in cpc.cpchp_login_account_input:
    #     print(i)
    kwa = {'a':'123','b':'232'}
    k, v = next(iter(kwa.items()))
    print(kwa.items())
    print(k,v)