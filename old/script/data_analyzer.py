import re
import selenium
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
source_path = "https://sports.163.com"
append_path = "/worldcup2022/data/live.html#/statistics/3718455"
driver.get(source_path+append_path)
print(driver.page_source)

