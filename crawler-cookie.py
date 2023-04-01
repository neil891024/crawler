#抓取 PTT八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1", #點擊已滿18歲的選項
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

    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]
#主程式:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" #取得PTT八卦版的網址
count=0 #頁數
while count<5: #抓幾頁
    pageURL="https://www.ptt.cc"+getData(pageURL) #取得上一頁
    count+=1
