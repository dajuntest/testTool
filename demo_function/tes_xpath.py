from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('https://555.0234.co/pc/index.html')

# ele =  driver.find_element(By.XPATH, '//button[contains(.,'登录')]')   # 定位元素
ele = driver.find_element(By.XPATH, "//input[@placeholder='账号']")

driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele, "outline: 2px dashed #07bb46 !important")       # 元素的背景色和边框设置成绿色和红色

ele.click()   # 元素高亮一般用于点击事件之前，检查元素定位是否正确，方便查看UI自动化的过程
# from harser import Harser
#
# HTML = '''
#     <html><body>
#     <div class="header" id="id-header">
#         <li class="nav-item" data-nav="first-item" href="/nav1">First item</li>
#         <li class="nav-item" data-nav="second-item" href="/nav2">Second item</li>
#         <li class="nav-item" data-nav="third-item" href="/nav3">Third item</li>
#     </div>
#     <div>First layer
#         <h3>Lorem Ipsum</h3>
#         <span>Dolor sit amet</span>
#     </div>
#     <div>Second layer</div>
#     <div>Third layer
#         <span class="text">first block</span>
#         <span class="text">second block</span>
#         <span>third block</span>
#     </div>
#     <span>fourth layer</span>
#     <img />
#     <div class="footer" id="id-foobar" foobar="ab bc cde">
#         <h3 some-attr="hey">
#             <span id="foobar-span">foo ter</span>
#         </h3>
#     </div>
#     </body></html>
# '''
#
# harser = Harser(HTML)
#
# print(harser.find('span').xpath)


def make_decorator(self, step_type):
    def decorator(step_text):
        def wrapper(func):
            self.add_step_definition(step_type, step_text, func)
            return func

        return wrapper

    return decorator


