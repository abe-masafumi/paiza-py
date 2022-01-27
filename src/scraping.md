# scraping

----

参考資料

[Beautifulsoup,Seleniumを使ったスクレイピング](https://www.youtube.com/watch?v=usxBYNhDwa4)

[完成資料](https://colab.research.google.com/drive/17APH7ZmKFlYPxxxrmwejhh1URziMyZBT?usp=sharing#scrollTo=uhu6wjSV-H8W)

[簡単なスクレイピングについて書いてある](https://www.pasonatech.co.jp/workstyle/column/detail.html?p=2638)


作成途中

[numbers3](https://colab.research.google.com/drive/1UxO4HwLe0kJTL0TlWrCdqQxMLlCWOZtX#scrollTo=Ers5PE1sJR05)


----

* 例 :
  
  > 必要なライブラリをインポート
  
  ```py
    import chromedriver_binary
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    import json
    import csv
  ```
  ```py
    # 初期設定
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(options=opts)

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # （B表）A表以前の当せん番号

    # URLを指定して読み込み
    load_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/numbers/backnumber/index.html'
    driver.get(load_url)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # HTMLのテーブルとクラスを指定して取得
    tables = soup.find("table", class_="typeTK js-backnumber-b")
    time.sleep(5)

    # その中からaタグを取得
    linksB_href = tables.find_all("a")
    time.sleep(5)
    # print(linksB_href)

    # aタグのhrefを取得して配列に挿入
    list = []
    for link in linksB_href:
        href = link.get('href')
        text = link.get_text()
        if href and text:
            list.append([link.get('href'),text])
            # print("list")
    print("list")
    print(list)
    # exit()
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 取得したurlをfor文で回してデータを当選データを取得
    
    resultsB = []
    for key, i in enumerate(list):
        load_url = "https://www.mizuhobank.co.jp"+i[0]
        driver.get(load_url)
        time.sleep(10)
        html = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(2)

        if key < 135:
            # time.sleep(1)
            tables = soup.find("div", class_="spTableScroll sp-none")
        else:
            # time.sleep(2)
            tables = soup.find("div", class_="spTableScroll js-lottery-backnumber-list sp-none")

        tables = tables.select('tbody tr')
        # time.sleep(1)
        for data in tables:
            around = data.find('th').get_text()
            print("around")
            print(around)
            date = data.findChildren("td")[0].get_text()
            result = data.findChildren("td")[1].get_text()
            resultsB.append([around,date,result])
    print("resultsB")
    print(resultsB)
    # exit()  
    #  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # （A表）先月から過去1年間の当せん番号

    # URLを指定して読み込み
    load_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/numbers/backnumber/index.html'
    driver.get(load_url)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find("table", class_="typeTK")
    time.sleep(10)
    linksA_tr = tables.find_all("tr")
    time.sleep(10)

    # aタグのhrefを取得して配列に挿入
    list = []
    for key, link in enumerate(linksA_tr):
        th = link.find('th').get_text()
        td = link.findChildren('td')[0]
        href = td.find('a').get("href")
        if href and th:
            list.append([href, th])
    # print(list)
    # exit()
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    resultsA = []
    # 取得したurlをfor文で回してデータを当選データを取得
    for key, i in enumerate(list):
        load_url = "https://www.mizuhobank.co.jp"+i[0]
        driver.get(load_url)
        time.sleep(10)
        html = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(10)
        tables = soup.find_all("table", class_="typeTK")

        for table in tables:
            thead = table.find("thead")
            around = thead.findChildren("th")[1].get_text()
            tbody = table.find("tbody")
            date = tbody.findChildren("tr")[0].find("td").get_text()
            result = tbody.findChildren("tr")[1].find("td").get_text()
            resultsA.append([around,date,result])
    print("resultsA")
    print(resultsA)
    # exit()
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 今月分のデータ取得

    resultsThis = []
    # URLを指定してデータを取得
    load_url = "https://www.mizuhobank.co.jp/retail/takarakuji/check/numbers/numbers3/index.html"
    driver.get(load_url)
    time.sleep(10)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(10)
    tables = soup.find_all("table", class_="typeTK")

    for key, table in enumerate(tables):
      time.sleep(1)
      thead = table.find("thead")
      around = thead.findChildren("th")[1].get_text()
      tbody = table.find("tbody")
      date = tbody.findChildren("tr")[0].find("td").get_text()
      result = tbody.findChildren("tr")[1].find("td").get_text()
      resultsThis.append([around,date,result])
    print("resultsThis")
    print(resultsThis)
    # exit()
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 全てのデータを結合、dict化、ソートし、csvファイルに保存
    TOTALRESULT = resultsB + resultsA + resultsThis
    # print("TOTALRESULT結合")
    # print(TOTALRESULT)

    # TOTALRESULT = ["第1427回","2004年10月29日","7720"],["第10回","2004年10月29日","7723"],["第1428回","2004年10月29日","7721"],["第1429回","2004年10月29日","7782"],["第1回","2004年10月29日","7723"]

    keyName = ["time", "date", "result"]

    TOTALRESULT = [dict(zip(keyName,item)) for item in TOTALRESULT]

    for key,i in enumerate(TOTALRESULT):
        s2 = i["time"].translate(str.maketrans({'第': '', '回': ''}))
        # print(s2)
        TOTALRESULT[key]["time"] = int(s2)


    TOTALRESULT = sorted(TOTALRESULT, key=lambda x: x['time'])

    # ✨"useData"をcsvファイルに保存
    file_path = "./allData.csv"
    with open(file_path, 'w') as outfile:
        wr = csv.DictWriter(outfile, fieldnames = keyName)
        wr.writeheader()
        wr.writerows(TOTALRESULT)
    exit()
  ```