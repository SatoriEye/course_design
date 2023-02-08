from selenium import webdriver
import re

pat = re.compile('class="line_con line_90"')
pat2 = re.compile('class="bottom_wrap"')
path = "D:\\chromedriver_win32\\chromedriver.exe"
page_path = "C:\\Users\\unreal_num border\\Desktop\\debug\\2022VIVA\\网易2022世界杯数据系统 阿根廷VS法国.mhtml"
driver = webdriver.Chrome(executable_path=path)
driver.get(page_path)
s = str(driver.page_source)
