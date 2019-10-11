#coding=utf-8

from poium import Page, PageElement

class LoginPage(Page):
    account = PageElement(id_='account')
    password = PageElement(xpath='//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input')
    submit = PageElement(id_='submit')


