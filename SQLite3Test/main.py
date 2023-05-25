import sqlite3
import os

# データベースファイルのパス
db_file = './SQLite3Test/sample.db'

# データベースファイルの存在を確認
if not os.path.exists(db_file):
    # データベースが存在しない場合、新しく作成
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # テーブルを作成
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')

    # データを挿入
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John Doe", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jane Smith", 30))

    # コミットして変更を確定
    conn.commit()
else:
    # データベースが存在する場合、接続
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

# データを取得して表示
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
