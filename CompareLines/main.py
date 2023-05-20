import tkinter as tk
import difflib

def compare_texts():
    text1 = text_field1.get("1.0", tk.END).splitlines()
    text2 = text_field2.get("1.0", tk.END).splitlines()

    differ = difflib.ndiff(text1, text2)

    diffs = list(differ)

    result_text1.delete("1.0", tk.END)
    result_text2.delete("1.0", tk.END)
    
    for diff in diffs:
        if diff[0] == '-':
            result_text1.insert(tk.END, diff[2:], 'red')
            result_text1.insert(tk.END, '\n')
        elif diff[0] == '+':
            result_text2.insert(tk.END, diff[2:], 'green')
            result_text2.insert(tk.END, '\n')
        else:
            result_text1.insert(tk.END, diff[2:])
            result_text1.insert(tk.END, '\n')
            result_text2.insert(tk.END, diff[2:])
            result_text2.insert(tk.END, '\n')

root = tk.Tk()

# テキストフィールド1の作成
text_field1 = tk.Text(root, height=10, width=50, borderwidth=2, highlightthickness=2, highlightbackground="black")
text_field1.pack()

# テキストフィールド2の作成
text_field2 = tk.Text(root, height=10, width=50, borderwidth=2, highlightthickness=2, highlightbackground="black")
text_field2.pack()

# ボタンの作成
compare_button = tk.Button(root, text="Compare Texts", command=compare_texts)
compare_button.pack()

# 結果表示用テキストフィールド1の作成
result_text1 = tk.Text(root, height=20, width=50, borderwidth=2, highlightthickness=2, highlightbackground="black")
result_text1.tag_config('red', background='red')
result_text1.pack()

# 結果表示用テキストフィールド2の作成
result_text2 = tk.Text(root, height=20, width=50, borderwidth=2, highlightthickness=2, highlightbackground="black")
result_text2.tag_config('green', background='green')
result_text2.pack()

root.mainloop()
