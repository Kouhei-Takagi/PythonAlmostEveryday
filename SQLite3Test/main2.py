import sqlite3
import os

class SampleDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        # データベースファイルの存在を確認
        if not os.path.exists(self.db_file):
            # データベースが存在しない場合、新しく作成
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()

            # テーブルを作成
            self.cursor.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                )
            ''')

            # データを挿入
            self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John Doe", 25))
            self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jane Smith", 30))

            # コミットして変更を確定
            self.conn.commit()
        else:
            # データベースが存在する場合、接続
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()

    def fetch_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        # 接続を閉じる
        self.conn.close()

# クラスのインスタンス化と使用例
db = SampleDatabase('./SQLite3Test/sample2.db')
db.connect()

users = db.fetch_users()
for user in users:
    print(user)

db.close()
