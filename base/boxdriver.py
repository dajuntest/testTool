# _*_ coding: utf-8 _*_
from __future__ import print_function
import time
import json
import websocket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# todo 添加是否用无页面启动方式

class BoxDriver(object):
    """
    私有全局变量
    """
    _base_driver = None
    _by_char = None
    """
    构造方法
    """
    def __init__(self, browser_type=0, download_path="c:\\Downloads", by_char=",", profile=None):
        """
        构造方法：实例化 BoxDriver 时候使用
        :param browser_type: 浏览器类型
        :param by_char: 分隔符，默认使用","
        :param profile:
            可选择的参数，如果不传递，就是None
            如果传递一个 profile，就会按照预先的设定启动火狐
            去掉遮挡元素的提示框等
        """
        self._by_char = by_char
        if browser_type == 0 :
            profile = webdriver.ChromeOptions()
            # profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

            # download.default_directory：设置下载路径
            # profile.default_content_settings.popups：设置为 0 禁止弹出窗口
            prefs = {'profile.default_content_settings.popups': 0,
                     'download.default_directory': download_path}
            profile.add_experimental_option('prefs', prefs)
            driver = webdriver.Chrome(chrome_options=profile)
            # driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=options)
        elif browser_type == 1:
            # if profile is not None:
                # profile = FirefoxProfile(profile)
            profile = webdriver.FirefoxProfile()
            # 指定下载路径
            profile.set_preference('browser.download.dir', download_path)
            # 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
            profile.set_preference('browser.download.folderList', 2)
            # 在开始下载时是否显示下载管理器
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            # 对所给出文件类型不再弹出框进行询问
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
            driver = webdriver.Firefox(firefox_profile=profile)
        else:
            driver = webdriver.Ie()
        try:
            self._base_driver = driver
            self._by_char = by_char
        except Exception:
            raise NameError("Browser %s Not Found! " % browser_type)

    def _convert_selector_to_locator(self, selector):
        """
        转换自定义的 selector 为 Selenium 支持的 locator
        :param selector: 定位字符，字符串类型，"i, xxx"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char)[0].strip()
        selector_value = selector.split(self._by_char)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")

        return locator

    def _locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            element = self._base_driver.find_element(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return element

    def _locate_elements(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            elements = self._base_driver.find_elements(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return elements

    def get_attribute(self, selector, attr_name):
        """
        获取元素属性的值
        :param selector: 元素定位
        :param attr_name: 元素属性名，如：'type'
        :return:
        """
        return self._locate_element(selector).get_attribute(attr_name)

    def get_attr_exist(self, selector, attr_name):
        """
        判断元素属性是否存在
        :param selector: 元素定位
        :param attr_name: 元素属性名，如：'type'
        :return: True: 元素属性存在
        """
        """
        c = d.get_attribute('x,//*[@id="keepLoginon"]','checked')
        # None
        print(c)
        # False
        print(bool(c)) 
       """
        # 假如元素中没有 'checked',不会报错，只会返回结果： None
        if self.get_attribute(selector, attr_name) == None:
            return False
        else:
            return True

    """
    浏览器本身相关方法
    """

    def refresh(self, url=None):
        """
        刷新页面
        如果 url 是空值，就刷新当前页面，否则就刷新指定页面
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self._base_driver.refresh()
        else:
            self._base_driver.get(url)

    def window_handles(self):
        self._base_driver.window_handles

    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.maximize_window()

    def get_screenshot_as_file(self, file):
        self._base_driver.get_screenshot_as_file(file)

    def get_screenshot_as_png(self):
        self._base_driver.get_screenshot_as_png()

    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self._base_driver.get(url)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self._base_driver.quit()

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self._base_driver.close()

    """
    基本元素相关方法
    """
    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    """
    元素属性相关方法
    """
    def get_value(self, selector):
        """
        返回元素的 value
        :param selector: 定位字符串
        :return:
        """
        el = self._locate_element(selector)
        return el.get_attribute("value")

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_element(selector)
        return el.get_attribute(attribute)

    def get_text(self, selector):
        """
        Get element text information.

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_element(selector)
        return el.text

    def get_displayed(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self._locate_element(selector)
        return el.is_displayed()

    def get_exist(self, selector):
        """
        该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param self:
        :param selector: 元素定位，如'id,account'
        :return: 布尔值
        """
        flag = True
        try:
            self._locate_element(selector)
            return flag
        except:
            flag = False
            return flag

    def get_enabled(self,selector):
        """
        判断页面元素是否可点击
        :param selector: 元素定位
        :return: 布尔值
        """
        if self._locate_element(selector).is_enabled():
            return True
        else:
            return False

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        return self._base_driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self._base_driver.current_url

    def get_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self._locate_element(selector)
        return el.is_selected()

    def get_text_list(self, selector):
        """
        根据selector 获取多个元素，取得元素的text 列表
        :param selector:
        :return: list
        """

        el_list = self._locate_elements(selector)

        results = []
        for el in el_list:
            results.append(el.text)

        return results
    """
    弹出窗口相关方法
    * 如果弹框的元素可以F12元素查看，则直接使用点击，获取元素等方法
    * 如果弹框元素无法查看，则使用如下方法可以搞定
    """
    def accept_alert(self):
        """
            Accept warning box.

            Usage:
            driver.accept_alert()
            """
        self._base_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        """
        self._base_driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        """
        获取 alert 弹出框的文本信息
        :return: String
        """
        return self._base_driver.switch_to.alert.text

    def type_in_alert(self,text):
        """在prompt对话框内输入内容"""
        self._base_driver.switch_to.alert.send_keys(text)
        self.forced_wait(1)
    """
    进入框架、退出框架
    """
    def switch_to_frame(self, selector):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("i,el")
        """
        el = self._locate_element(selector)
        self._base_driver.switch_to.frame(el)

    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self._base_driver.switch_to.default_content()

    """
    等待方法
    """
    def forced_wait(self, seconds= 2 ):
        """
        强制等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self._base_driver.implicitly_wait(seconds)

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self._convert_selector_to_locator(selector)

        WebDriverWait(self._base_driver, seconds).until(expected_conditions.presence_of_element_located(locator))
    """上传"""
    def upload_input(self,selector,file):
        """
        上传文件 （ 标签为 input 类型，此类型最常见，最简单）
        :param selector: 上传按钮定位
        :param file: 将要上传的文件（绝对路径）
        :return: 无
        """
        self._locate_element(selector).send_keys(file)

    """ websocket方法"""
    def websocket_help(url, data):
        ws = websocket.create_connection(url)
        res = ws.send(json.dumps(data))
        ws.close()
        return res