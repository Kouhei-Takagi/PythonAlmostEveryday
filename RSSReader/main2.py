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
    for entry in feed.entries:
        textarea.insert(tk.INSERT, f"Title: {entry.title}\nLink: {entry.link}\n\n")

# フィードを取得し、表示を更新する
def refresh_feed():
    textarea.delete('1.0', tk.END)
    threading.Thread(target=fetch_and_update).start()

# 別スレッドでフィードを取得し、表示を更新する
def fetch_and_update():
    feed = fetch_feed(url_entry.get())
    update_feed_display(feed)

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
