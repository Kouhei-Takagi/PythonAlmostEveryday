import tkinter as tk
from tkinter import ttk, messagebox

data = []

def add_task():
    task = task_entry.get()
    importance = importance_var.get()
    urgency = urgency_var.get()
    if task != "":
        task_list.insert("", "end", values=(importance, urgency, task))
        data.append((importance, urgency, task))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def delete_task():
    try:
        selected_item = task_list.selection()[0]
        task_list.delete(selected_item)
        # Remove the corresponding item from data
        for item in data:
            if item == task_list.item(selected_item, 'values'):
                data.remove(item)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def sort_tasks_by_importance():
    task_list.delete(*task_list.get_children())
    values = sorted(data, key=lambda x: x[0], reverse=True)  # Reverse sorting because 5 is highest importance
    for value in values:
        task_list.insert("", "end", values=value)

def sort_tasks_by_urgency():
    task_list.delete(*task_list.get_children())
    values = sorted(data, key=lambda x: x[1], reverse=True)  # Reverse sorting because 5 is highest urgency
    for value in values:
        task_list.insert("", "end", values=value)

# GUI作成
app = tk.Tk()
app.title("ToDo List")

# タスクエントリボックス作成
task_entry = tk.Entry(app, font=('Helvetica', 20))
task_entry.pack(pady=10)

# タスク重要度
importance_var = tk.StringVar(app)
importance_var.set('5')  # default value
importance_label = tk.Label(app, text='Importance')
importance_label.pack(pady=5)
importance_opt = tk.OptionMenu(app, importance_var, '5', '4', '3', '2', '1')
importance_opt.pack(pady=5)

# タスク緊急度
urgency_var = tk.StringVar(app)
urgency_var.set('5')  # default value
urgency_label = tk.Label(app, text='Urgency')
urgency_label.pack(pady=5)
urgency_opt = tk.OptionMenu(app, urgency_var, '5', '4', '3', '2', '1')
urgency_opt.pack(pady=5)

# ツリービュー（表形式）の作成
task_list = ttk.Treeview(app, columns=("Importance", "Urgency", "Task"), show="headings")
task_list.heading("Importance", text="Importance")
task_list.heading("Urgency", text="Urgency")
task_list.heading("Task", text="Task")
task_list.pack(pady=10)

# ボタン作成
add_task_button = tk.Button(app, text='Add Task', width=20, command=add_task)
add_task_button.pack(pady=10)

delete_task_button = tk.Button(app, text='Delete Task', width=20, command=delete_task)
delete_task_button.pack(pady=10)

sort_importance_button = tk.Button(app, text='Sort by Importance', width=20, command=sort_tasks_by_importance)
sort_importance_button.pack(pady=10)

sort_urgency_button = tk.Button(app, text='Sort by Urgency', width=20, command=sort_tasks_by_urgency)
sort_urgency_button.pack()

# アプリを実行
app.mainloop()
