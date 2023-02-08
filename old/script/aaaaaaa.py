import time

[900, 640]
loc = [30,150]
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

click()