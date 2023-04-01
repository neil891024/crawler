import requests as req #用req代替requests
#用httpbin測試get
#url = "https://httpbin.org/get" 
url = 'https://httpbin.org//basic-auth/123456/123456' 

params = { #加入參數
    'page' :'2',
    'count':'5'
}

data = { #加入資料
    'name' : 'white',
    'age' : 23
}

header = { #大部分網站都有防爬蟲，需要弄成網路請求
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# r = req.get(url,params=params) #發送http的請求到ur1這個網址
# print(r.text) #讀取網站中的圖片

r = req.post(url,params=params,data=data) #發送http的請求到ur1這個網址
print(r.text) #讀取網站中的圖片


# with open('123.jpg',mode='rb') as file: #儲存檔案(名稱 來源)
#     image = {'upload_image':file.read()}
r=req.get(url,auth=('123456','123456'),timeout=5) 
print(r.text) #讀取網站內的文字

# print(r.content) #讀取網站中的圖片
