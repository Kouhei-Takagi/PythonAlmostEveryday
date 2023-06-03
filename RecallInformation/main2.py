import os
import time
import requests
from bs4 import BeautifulSoup

StartURL = "https://www.mlit.go.jp/report/press/jidosha08_hh_"
EndURL = ".html"
StartNumber = "004797" # 000001から始めると、データが大量になりすぎるので、004797から始める
EndNumber = "004799"
BasePath = "./RecallInformation/"

for i in range(int(StartNumber), int(EndNumber) + 1):
    url = StartURL + str(i).zfill(6) + EndURL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

    # PDFのリンクをすべて取得
    links = soup.select("a[href$='.pdf']")

    for link in links:
        # PDFのURLを取得
        pdf_url = "https://www.mlit.go.jp" + link['href']
        # PDFの内容を取得
        pdf = requests.get(pdf_url)

        # PDFファイル名を取得
        filename = os.path.join(BasePath, link['href'].split('/')[-1])

        # PDFをディスクに保存
        with open(filename, 'wb') as f:
            f.write(pdf.content)
    time.sleep(5) # 5秒スリープ, これがないと、サーバーに負荷をかけてしまうので、注意
