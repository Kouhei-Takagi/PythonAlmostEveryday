import requests
from bs4 import BeautifulSoup
import hashlib
import time
import tkinter as tk
from threading import Thread

# 監視するURL
urls = ["https://qiita.com",
        "https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja"]

# 各URLの前回のウェブサイトのハッシュ値を保持する辞書
prev_hashes = {}

# tkinterのウィンドウを作成
window = tk.Tk()
window.title("Web Monitor👀✅")
labels = {}

for i, url in enumerate(urls):
    tk.Label(window, text=url).grid(row=i, column=0)
    labels[url] = tk.Label(window, text="Monitoring")
    labels[url].grid(row=i, column=1)
    prev_hashes[url] = None

def monitor(url, label):
    prev_hash = None
    while True:
        # ウェブサイトの内容を取得
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # テスト
        #print(soup.text)

        # ハッシュ値を計算
        current_hash = hashlib.sha256(soup.text.encode('utf-8')).hexdigest()

        # ハッシュ値が前回と異なる場合は更新あり
        if prev_hash is not None and current_hash != prev_hash:
            label.config(text="UPDATED✅")
        else:
            label.config(text="👀ING")

        prev_hash = current_hash

        # 30秒ごとにチェック
        time.sleep(30)

# 各URLについて別スレッドでウェブサイトの監視を開始
for url in urls:
    t = Thread(target=monitor, args=(url, labels[url]))
    t.start()

# GUIを表示
window.mainloop()
