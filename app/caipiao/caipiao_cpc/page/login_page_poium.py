from poium import Page, PageElement
from selenium import webdriver


class BaiduIndexPage(Page):

    search_input = PageElement(css="#kw", describe="搜索框")
    search_button = PageElement(css="#su", describe="搜索按钮")

class CPCLoginPage(Page):
    login = PageElement(id_='id', describe='登录')
    pass

class ToutolPage(BaiduIndexPage, CPCLoginPage):
    pass

class WebAction(BaiduIndexPage, CPCLoginPage):

    page = ToutolPage(webdriver.Chrome())

    # 动态传入类属性
    @classmethod
    def with_click(cls, click_element):
        if hasattr(cls.page, click_element):
            getattr(cls.page, click_element).click()
        return cls

    @classmethod
    def with_input(cls):
        cls.page.search_input.send_keys('poium')
        return cls

    @classmethod
    def with_input(cls, input_element, text):
        if hasattr(cls.page, input_element):
            getattr(cls.page, input_element).send_keys(text)
        return cls

    @classmethod
    def with_open(cls):
        cls.page.get('https://www.baidu.com')
        return cls

if __name__ == '__main__':
    weba = WebAction()
    weba.with_open().with_input().with_click('search_button')

