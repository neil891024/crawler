import requests
from bs4 import BeautifulSoup
url = 'https://student.hust.edu.tw/guidance?item=12&custom=2896&type=detail&isEn=0'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text,'html.parser')
datas = sp.find("td")

print(datas.text)
# print(sp.title.text)




