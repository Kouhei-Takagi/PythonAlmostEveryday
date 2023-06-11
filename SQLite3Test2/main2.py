import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ db_fileで指定されたSQLiteデータベースへのデータベース接続を作成
    """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)  # 接続を作成
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    if conn:
        return conn
    return None


def create_table(conn, create_table_sql):
    """ create_table_sql文からテーブルを作成
    """
    try:
        c = conn.cursor()  # カーソルオブジェクトを作成
        c.execute(create_table_sql)  # SQL文を実行
    except Error as e:
        print(e)


def insert_data(conn, insert_data_sql):
    """ テーブルに新しいデータを挿入
    """
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()  # 変更を確定
    except Error as e:
        print(e)


def select_data(conn, select_data_sql):
    """ テーブルからデータをクエリ
    """
    try:
        c = conn.cursor()
        c.execute(select_data_sql)
        
        rows = c.fetchall()  # クエリ結果の全行を取得
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def main():
    database = r"./SQLite3Test2/sqlite_db.sqlite"  # データベースファイル

    create_table_sql = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer
                                    ); """

    insert_data_sql = """INSERT INTO tasks(name, priority)
                         VALUES('Task 1', 1);"""

    select_data_sql = "SELECT * from tasks"

    # データベース接続を作成
    conn = create_connection(database)

    if conn is not None:
        # tasksテーブルを作成
        create_table(conn, create_table_sql)
        # データを挿入
        insert_data(conn, insert_data_sql)
        # データを選択
        select_data(conn, select_data_sql)
    else:
        print("データベース接続を作成できません。")


if __name__ == '__main__':
    main()
