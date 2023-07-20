import feedparser
import tkinter as tk
from tkinter import scrolledtext
import threading

# RSSフィードをパースする
def fetch_feed(url):
    feed = feedparser.parse(url)
    return feed

# フィードのエントリをテキストエリアに表示する
def update_feed_display(feed):
    textarea.delete('1.0', tk.END)
    for entry in feed.entries:
        # 'link'属性の存在を確認する
        link = entry.link if 'link' in entry else "Link: Not Available"
        textarea.insert(tk.INSERT, f"Title: {entry.title}\nLink: {link}\n\n")
    refresh_button['state'] = 'normal'

# フィードを取得し、表示を更新する
def refresh_feed():
    refresh_button['state'] = 'disabled'
    threading.Thread(target=fetch_and_update).start()

# 別スレッドでフィードを取得し、表示を更新する
def fetch_and_update():
    feed = fetch_feed(url_entry.get())
    root.after_idle(update_feed_display, feed)

# GUIを作成する
root = tk.Tk()
root.title("RSS Reader")

url_entry = tk.Entry(root)
url_entry.pack()

refresh_button = tk.Button(root, text="Refresh Feed", command=refresh_feed)
refresh_button.pack()

textarea = scrolledtext.ScrolledText(root)
textarea.pack()

root.mainloop()
