import sqlite3

class TaskManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_task_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, title):
        self.cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        self.conn.commit()

    def complete_task(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()

def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            task_id, title, completed = task
            status = "Complete" if completed else "Incomplete"
            print(f"- {task_id}: {title} ({status})")

# アプリケーションの実行例
db = TaskManager('./SQLite3Test/tasks.db')
db.connect()
db.create_task_table()

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter task title: ")
        db.add_task(title)
        print("Task added successfully.")
    elif choice == '2':
        task_id = input("Enter task ID to mark as complete: ")
        db.complete_task(task_id)
        print("Task marked as complete.")
    elif choice == '3':
        tasks = db.get_all_tasks()
        print_tasks(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

db.close()
