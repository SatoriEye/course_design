
import re

pattern = re.compile('<a class="\w+" href="\S+" target="_blank">数据</a>')
pattern2 = re.compile('href="\S+"')
path = 'C:\\Users\\unreal_num border\\Desktop\\debug\\link.txt'
data = ""
with open(path, "r", encoding='utf-8') as f:
    data = f.read()
    analyzed_data = pattern.findall(data)
    for i in analyzed_data:
        print(pattern2.findall(str(i))[0][6:-1])
    # print(analyzed_data)
    # print(len(analyzed_data))
    # for i in analyzed_data:
    #     print(i)
