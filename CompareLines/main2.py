import tkinter as tk
import difflib
import nltk
nltk.download('punkt')

def compare_texts():
    text1_words = nltk.word_tokenize(text_field1.get("1.0", tk.END))
    text2_words = nltk.word_tokenize(text_field2.get("1.0", tk.END))

    differ = difflib.ndiff(text1_words, text2_words)

    diffs = list(differ)

    result_text1.delete("1.0", tk.END)
    result_text2.delete("1.0", tk.END)
    
    for diff in diffs:
        if diff[0] == '-':
            result_text1.insert(tk.END, diff[2:], 'red')
            result_text1.insert(tk.END, ' ')
        elif diff[0] == '+':
            result_text2.insert(tk.END, diff[2:], 'green')
            result_text2.insert(tk.END, ' ')
        else:
            result_text1.insert(tk.END, diff[2:])
            result_text1.insert(tk.END, ' ')
            result_text2.insert(tk.END, diff[2:])
            result_text2.insert(tk.END, ' ')

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
