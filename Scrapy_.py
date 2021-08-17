import requests
from lxml import etree
import os
import json
import time
import re



def get_Month():
    lt = time.localtime(time.time())
    lt = lt[1]
    if (lt>9):
        return str(lt)
    else:
        return "0"+str(lt)

def get_Day():
    return str(time.localtime()[2])

def get_sjc():
    return time.time()

def returnApi():
    Api_list=[]
    month = get_Month()
    day = get_Day()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        #     'Cookie':'BIDUPSID=434B76AC4C98285BBCE35970C1F850D7; PSTM=1586866907; BDUSS=FIUGUxcDFsb0FGa2RDQ2hSeEZDU0U1MjlXRlBMZnlnOTFMeUpBWkF2TG82bHBmRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOhdM1~oXTNfWW; BDUSS_BFESS=FIUGUxcDFsb0FGa2RDQ2hSeEZDU0U1MjlXRlBMZnlnOTFMeUpBWkF2TG82bHBmRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOhdM1~oXTNfWW; __yjs_duid=1_ec83e1938ec710747f47e7a3536745dc1621345304820; BDSFRCVID_BFESS=Cd4OJexroG0Y4zTH01hhUxAK-9hEYKcTDYLtOwXPsp3LGJLVgaSTEG0Ptf-xU40-2ZlgogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbue_II5JIP3qn7I5-Oo5P6HbxoXK-JqHD7XVh7H3p7keqOzyb75XlI-DPAjbn5aQ6bCa56EWhk2ep72y-vSh4Ij5tTQLtuqyeJl-qcH0KQpsIJM5-DWbT8U5f5mLbQGaKviaKJjBMb1MlvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe65WeaDHt6tsKjAX3JjV5PK_Hn7zeUbfjM4pbq7H2M-jyRnE-pPMtRnsStnqyIFBMML4yUbn0pcrbgOfhUJb-IOdspcs34JH0p0kQN3T-PKLMNIJoTC-yJRJDn3oyUvJXp0n3tvly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJUutfD7H3KC2JC0MbM5; BK_SEARCHLOG={"key":["Could not connect to Redis at 127.0.0.1:6379: Connection refused","Windows Power Shell和cmd有什么区别"]}; BAIDUID=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; MCITY=-:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1628495776,1628650449,1628756390,1629086443; channel=baidusearch; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=3; BAIDUID_BFESS=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; ab_sr=1.0.1_NTBlZTE5OWM4ZDY5ZjY3OTE5YTIxZjY4YzY2NTM2MTM4NzgwMzI3ZTViNWYxMGEwN2YwMmNiZTRmNDIxZDI4MzFmNDJhZGE2NGIyOGI4OTU1NWYzZDk5ZmJkNzg4ZTc3ZGZhNThmYmEzMGVlNGM3OWY3YWYwODE3ZDI2N2FiNGJhNTlhNzA0ZGFkMmQ1OWI5MGFkYWZkMTM4NTk0NDM1Yg==; RT="z=1&dm=baidu.com&si=nknybyt5wna&ss=ksebpgot&sl=2&tt=4a5&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=4hu&ul=7p0&hd=7pj"; H_PS_PSSID=34333_34369_31660_34375_33848_34092_34106_34111_26350_34415_34319_34288_34388; BA_HECTOR=8g85a00g040l2k2k2g1ghk61d0r'
        # }
    }
    url = "https://baike.baidu.com/cms/home/eventsOnHistory/"+month+".json?_=1629098631978"
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
    print(json.loads(returnApi()))
