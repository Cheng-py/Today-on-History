import requests
import json
import time
import re


def get_Month():
    lt = time.localtime(time.time())
    lt = lt[1]
    if (lt>9):
        return str(lt)
    else:   # 月份小于10前面加个0，保证格式
        return "0"+str(lt)

def get_Day():
    return str(time.localtime()[2])

def get_ts(): # 获取时间戳
    return time.time()

def returnApi():
    Api_list=[]
    month = get_Month()
    day = get_Day()
    ts = get_ts()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    }
    url = "https://baike.baidu.com/cms/home/eventsOnHistory/"+month+".json?_="+str(ts)
    html = requests.get(url=url,headers=headers).json()
    for i in range(len(html[month][month+day])):
        year = html[month][month+day][i]['year']
        title = html[month][month+day][i]['title']
        link = html[month][month+day][i]['link']
        type = html[month][month+day][i]['type']
        desc = html[month][month+day][i]['desc']
        title = re.sub(r'<.*?>','',title)
        desc = re.sub(r'<.*?>','',desc)+'...'
        The_Api = {"year":year,"title":title,"link":link,"desc":desc,"type":type}
        Api_list.append(The_Api)
    return json.dumps(Api_list)

if __name__ == '__main__':
    returnApi()
