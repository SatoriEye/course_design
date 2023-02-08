# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import win32api
import win32con
import os

path = "C:\\Users\\unreal_num border\\Desktop\\debug\\linkdata.txt"
rpath = "C:\\Users\\unreal_num border\\Desktop\\debug"


def click():
    titlename = u"文件另存为"
    calssname = u"#32770"
    import win32gui, win32api, win32con
    # win = win32gui.FindWindow(None, titlename)
    # (left, top, right, bottom) = win32gui.GetWindowRect(win)
    win32api.SetCursorPos([30,150])
    # win32api.SetCursorPos((left + (right - left) - 55, top + (bottom - top) - 25))  # 光标定位
    # 鼠标点击
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.keybd_event(13, 0, 0, 0)  # 按下enter
    win32api.SetCursorPos([900, 640])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.keybd_event(13, 0, 0, 0)  # 按下enter


def mhtml_downloader(news_url):
    # 测试网址
    # 打开另存为mhtml功能
    options = webdriver.ChromeOptions()
    options.add_argument('--save-page-as-mhtml')
    # 设置chromedriver，并打开webdriver
    driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
    driver.get(news_url)
    # 模拟键盘操作
    win32api.keybd_event(17, 0, 0, 0)  # 按下ctrl
    win32api.keybd_event(65, 0, 0, 0)  # 按下a
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放a
    win32api.keybd_event(83, 0, 0, 0)  # 按下s
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放s
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ctrl
    win32api.keybd_event(13, 0, 0, 0)  # 按下enter
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放enter
    time.sleep(3)
    click()
    # 预估下载时间，后期根据实际网速调整
    time.sleep(3)
    # 关闭webdriver
    driver.close()


data = ''
with open(path, 'r') as f:
    data = str(f.read()).split('\n')

if not os.path.exists(os.path.join(rpath, 'mhtml_data')):
    os.mkdir(os.path.join(rpath, 'mhtml_data'))

for i in data:
    news_url = "https://sports.163.com" + i
    mhtml_downloader(news_url)
