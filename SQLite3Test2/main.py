import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)  # create a connection
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    if conn:
        return conn
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()  # create a cursor object
        c.execute(create_table_sql)  # execute an sql statement
    except Error as e:
        print(e)


def insert_data(conn, insert_data_sql):
    """ insert new data into the table
    """
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()  # commit the changes
    except Error as e:
        print(e)


def select_data(conn, select_data_sql):
    """ query data from the table
    """
    try:
        c = conn.cursor()
        c.execute(select_data_sql)
        
        rows = c.fetchall()  # fetch all rows of a query result
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def main():
    database = r"sqlite_db.sqlite"  # database file

    create_table_sql = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer
                                    ); """

    insert_data_sql = """INSERT INTO tasks(name, priority)
                         VALUES('Task 1', 1);"""

    select_data_sql = "SELECT * from tasks"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create tasks table
        create_table(conn, create_table_sql)
        # insert data
        insert_data(conn, insert_data_sql)
        # select data
        select_data(conn, select_data_sql)
    else:
        print("Cannot create the database connection.")


if __name__ == '__main__':
    main()
