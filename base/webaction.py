from selenium import webdriver

class WebAction(object):

    page = None

    def __new__(cls, totalpage):
        cls.page = totalpage(webdriver.Chrome())
        return super().__new__(cls)

    # 动态传入类属性
    @classmethod
    def click(cls, element):
        if hasattr(cls.page, element):
            getattr(cls.page, element).click()
        return cls

    @classmethod
    def input(cls, element, text):
        if hasattr(cls.page, element):
            getattr(cls.page, element).send_keys(text)
        return cls

    @classmethod
    def get(cls, url):
        cls.page.get(url)
        return cls
