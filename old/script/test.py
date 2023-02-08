

import selenium
import re
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())
driver.get("https://zh.wikipedia.org/zh-sg/2022%E5%B9%B4%E5%9C%8B%E9%9A%9B%E8%B6%B3%E5%8D%94%E4%B8%96%E7%95%8C%E7%9B%83#%E5%8F%83%E8%B3%BD%E5%90%8D%E5%96%AE")
print(driver.page_source)