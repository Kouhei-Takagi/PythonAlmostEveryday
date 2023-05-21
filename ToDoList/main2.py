import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

data = pd.DataFrame(columns=['Importance', 'Urgency', 'Task'])

def add_task():
    task = task_entry.get()
    importance = importance_var.get()
    urgency = urgency_var.get()
    if task != "":
        global data
        data = data.append({'Importance': importance, 'Urgency': urgency, 'Task': task}, ignore_index=True)
        task_entry.delete(0, tk.END)
        plot_data()
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def plot_data():
    fig.clear()
    ax = fig.add_subplot(111)
    for i, row in data.iterrows():
        ax.scatter(row['Importance'], row['Urgency'], label=row['Task'])
    ax.set_xlabel('Importance')
    ax.set_ylabel('Urgency')
    ax.set_title('Task Plot')
    ax.legend(loc='lower right')  # Adjust legend position to avoid overlapping with points
    ax.set_xlim([0, 6])  # Set x-axis range from 1 to 5
    ax.set_ylim([0, 6])  # Set y-axis range from 1 to 5
    canvas.draw()

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

# matplotlib figure
fig = Figure(figsize=(5, 5), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack()

# ボタン作成
add_task_button = tk.Button(app, text='Add Task', width=20, command=add_task)
add_task_button.pack(pady=10)

# アプリを実行
app.mainloop()
