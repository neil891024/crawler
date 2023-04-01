import requests as req 
from openpyxl import Workbook #使用excel的模組


wb = Workbook() #創建excel檔案
ws = wb.active #使用預設的工作表

title = ['課名','作者','價格','預購價','販售數'] #將要取得的資訊寫為一個列表
ws.append(title) #將資料寫到第一橫排

header = { #避免被網站擋掉
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

for index in range(28): #使用for跑過28個頁面
    url = 'https://api.hahow.in/api/courses?limit=24&page='
    url = url+str(index)
    print(url)
    r= req.get(url)
    r = req.get(url,headers=header)
    print(r)
    
    root_json = r.json() #用json格式來解析

    for data in root_json['data']:
        course =[]
        course.append(data['title'])
        course.append(data['owner']['name'])
        course.append(data['price'])
        course.append(data['preOrderedPrice'])
        course.append(data['numSoldTickets'])

        ws.append(course)

wb.save('data.xlsx')
