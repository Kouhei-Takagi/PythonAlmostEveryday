import sqlite3

# データベースに接続
conn = sqlite3.connect('./KyujinBoxScraping/kyujinbox.db')
c = conn.cursor()

# クエリを実行してデータを取得
c.execute("SELECT * FROM scraped_data")
rows = c.fetchall()

# データを表示
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
