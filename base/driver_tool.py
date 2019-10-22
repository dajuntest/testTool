from app.caipiao.caipiao_cpc.page.home_page import CpCHomePage
from selenium import webdriver

from app.caipiao.caipiao_cpc.page.lottery_hall_page import CpCLotteryHallPage


class TotalPage(CpCHomePage):
    # cpchp = CpCHomePage
    pass


class WebAction(object):

    page = TotalPage(webdriver.Chrome())

    # 动态传入类属性
    @classmethod
    def with_click(cls, click_element):
        if hasattr(cls.page, click_element):
            getattr(cls.page, click_element).click()
        return cls

    @classmethod
    def with_input(cls, input_element, text):
        if hasattr(cls.page, input_element):
            getattr(cls.page, input_element).send_keys(text)
        return cls

    @classmethod
    def with_open(cls, url):
        cls.page.get(url)
        return cls

    @classmethod
    def with_Slide(cls):
        pass


# if __name__ == '__main__':
    # print(dir(CpCHomePage))
    # print(CpCHomePage.__dict__)