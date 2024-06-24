import pandas as pd

# Excelファイルのパスのリスト
files = [
    'path/to/week1.xlsx',
    'path/to/week2.xlsx',
    'path/to/week3.xlsx',
    'path/to/week4.xlsx',
    'path/to/week5.xlsx'
]

# 各ファイルを読み込み、1つのDataFrameに結合
all_data = pd.DataFrame()
for file in files:
    # Excelファイルを読み込む
    df = pd.read_excel(file)
    # 必要に応じてDataFrameを加工
    all_data = pd.concat([all_data, df])

# 結合されたデータを表示
print(all_data.head())