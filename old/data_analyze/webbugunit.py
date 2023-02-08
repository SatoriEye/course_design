import re
import os
from selenium.webdriver import Chrome


def mhtml_traversal(file_path):
    mhtml_path = [k for i, j, k in os.walk(file_path)][0]
    return mhtml_path



def violation_filter(data_array):
    res = []
    filter_pattern = re.compile("\d+'\x20[\u4e00-\u9fa5]+\x20[\u4e00-\u9fa5]+")
    for i in data_array:
        d = filter_pattern.findall(i)
        if d != []:
            for j in d:
                res.append(j)
    return res


def analyze_data_violation(path):
    pat = re.compile("<span data-v-3af0ea2c")
    pat_end_here = re.compile('</span>')
    driver = Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
    driver.get(path)
    s = driver.page_source
    d = pat.finditer(s)
    data_array = []
    for i in d:
        starthere = i.end()
        endhere = pat_end_here.search(s[starthere:]).span()
        data_array.append(s[starthere:][:endhere[0]])
    data_array = violation_filter(data_array)
    driver.close()
    return data_array


# analyze_data_violation(path)


def analyze_data_contest_info(path):
    pat_score = re.compile('<div data-v-3af0ea2c="" class="score_box">')
    pat_host_country = re.compile('<div data-v-3af0ea2c="" class="team_name home_name">')
    pat_away_country = re.compile('<div data-v-3af0ea2c="" class="team_name away_name">')
    pat_time = re.compile('<span data-v-3af0ea2c="" class="time">')
    pat_loc = re.compile('<span data-v-3af0ea2c="" class="venue">')
    pat_end_here = re.compile('</span>')
    pat_end_here_aaaaaa = re.compile('</div>')
    driver = Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
    driver.get(path)
    data_dict = dict()
    s = driver.page_source
    country1 = dict()
    country2 = dict()
    # 匹配国家,字典初始化顺序不能乱, 否则数据出问题
    # 主场匹配
    info = pat_host_country.finditer(s)
    for i in info:
        starthere = i.end()
        endhere = pat_end_here_aaaaaa.search(s[starthere:]).span()
        country1['country'] = s[starthere:][:endhere[0]]

    # 客场匹配
    info = pat_away_country.finditer(s)
    for i in info:
        starthere = i.end()
        endhere = pat_end_here_aaaaaa.search(s[starthere:]).span()
        country2['country'] = s[starthere:][:endhere[0]]

    # 分数匹配
    info = pat_score.finditer(s)
    for i in info:
        starthere = i.end()
        endhere = pat_end_here_aaaaaa.search(s[starthere:]).span()
        temp = re.compile("\d")
        score = temp.findall(s[starthere:][:endhere[0]])
        country1['score'] = score[0]
        country2['score'] = score[1]

    # 时间匹配
    info = pat_time.finditer(s)
    for i in info:
        temp = re.compile("\d+\.")
        starthere = i.end()
        endhere = pat_end_here.search(s[starthere:]).span()
        if temp.findall(s[starthere:][:endhere[0]]) == []:
            continue
        data_dict['time'] = s[starthere:][:endhere[0]]

    # 地点匹配
    info = pat_loc.finditer(s)
    for i in info:
        starthere = i.end()
        endhere = pat_end_here.search(s[starthere:]).span()
        data_dict['where'] = s[starthere:][:endhere[0]]

    # 数据整合
    data_array = analyze_data_violation(path)
    # print(data_array)
    data_dict['violation'] = data_array
    data_dict['host_country'] = country1
    data_dict['away_country'] = country2
    return data_dict


def get_desktop_path():
    import os
    return os.path.join(os.path.expanduser("~"), 'Desktop')

def exec_and_save():
    import json
    webdriver_path = "D:\\chromedriver_win32\\chromedriver.exe"
    file_path = "D:\\信息\\临时工作区间\\课程设计\\2022VIVA"
    mhtml = mhtml_traversal(file_path)
    desktop_path = get_desktop_path()
    if not os.path.exists(os.path.join(desktop_path, "result")):
        os.mkdir(os.path.join(desktop_path, "result"))
    desktop_path = os.path.join(desktop_path, "result")
    for i in mhtml:
        f = open(os.path.join(desktop_path, i[14:-6]+".json"), 'w')
        data_dict = analyze_data_contest_info(path=os.path.join(file_path, i))
        data_dict = json.dumps(data_dict)
        f.write(data_dict)
        f.close()




exec_and_save()