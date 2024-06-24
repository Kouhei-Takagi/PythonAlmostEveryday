import pandas as pd
import pyperclip
import datetime

# 現在の日付の取得
today = datetime.today()

# クリップボードの内容を読み込む
data = pyperclip.paste()

# 文字列データをDataFrameに変換
data_list = [line.split('\t') for line in data.split('\n') if line]
df = pd.DataFrame(data_list[1:], columns=data_list[0])

# DataFrameをCSVに保存
df.to_csv(f'./DATA/sell-securities_data_{today}.csv', index=False, encoding='utf-8')

print("CSVファイルが保存されました。")