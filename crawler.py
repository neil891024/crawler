#抓取 PTT電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})
# 網站大多有防爬蟲，須讓程式具有人類的操作
with req.urlopen(request) as response: #開啟網址
    data=response.read().decode("utf-8")
#解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser") #使用bs4解析html的資料
titles=root.find_all("div",class_="title") #尋找所有 class="title" 的div標籤 標籤"div"，搜尋條件class_="title"
for title in titles:
    if title.a != None: #如果標題包含 a 標籤(沒有被刪除).印出來
        print(title.a.text)

#print(titles) #抓取<a>標籤內的文字
#print(root.title.text) #抓取標籤內的文字(大標題)
#要找出想要的資料在原始碼中的特色