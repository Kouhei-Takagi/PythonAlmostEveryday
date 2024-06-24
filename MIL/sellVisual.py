import pandas as pd
import pyperclip
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl

# 現在の日付の取得
today = datetime.today()
# 日付の形式を整形する
today = today.strftime('%Y%m%d')

# クリップボードの内容を読み込む
data = pyperclip.paste()

# 文字列データをDataFrameに変換
data_list = [line.split('\t') for line in data.split('\n') if line]
df = pd.DataFrame(data_list[1:], columns=data_list[0])

# DataFrameをCSVに保存
df.to_csv(f'./DATA/sell-securities_data_{today}.csv', index=False, encoding='utf-8')

print("CSVファイルが保存されました。")

# CSVファイルを読み込む
file_path = f'./DATA/sell-securities_data_{today}.csv'
data = pd.read_csv(file_path)

# データを確認
data.head()

# ヘッダーが正しく設定されていないため、ファイルを再読み込みしヘッダーを指定
data = pd.read_csv(file_path, header=None, names=['証券会社', '取引量'])

# '取引量'のカラムでカンマを削除し数値型に変換
data['取引量'] = data['取引量'].str.replace(',', '').astype(int)

# データを確認
data.head()

# Matplotlibのフォントをヒラギノ角ゴ ProN W3に設定
mpl.rcParams['font.family'] = 'Hiragino Sans'
mpl.rcParams['font.sans-serif'] = ['Hiragino Sans W3']

# 棒グラフを描画
plt.figure(figsize=(12, 8))
plt.barh(data['証券会社'], data['取引量'], color='skyblue')
plt.xlabel('取引量')
plt.ylabel('証券会社')
plt.title('証券会社ごとの売り越し量')
plt.gca().invert_yaxis()  # y軸を降順に表示
plt.savefig(f'./DATA/sell-{today}.png')
plt.show()

# カテゴリと色を設定するディクショナリを作成
categories = {
    "外資系": "blue",
    "国内系": "green",
    "米国": "red",
    "オランダ": "purple",
    "フランス": "orange",
    "スイス": "cyan",
    "香港": "magenta",
    "日本": "yellow"
}

# データフレームにカテゴリと色のカラムを追加
# ここではファイルパスから再度データを読み込む
file_path = f'./DATA/sell-securities_data_{today}.csv'
data = pd.read_csv(file_path, header=None, names=['証券会社', '取引量'])

# '取引量'のカラムでカンマを削除し数値型に変換
data['取引量'] = data['取引量'].str.replace(',', '').astype(int)

# 各証券会社にカテゴリを割り当てるための仮のデータ（本来はデータに含めるべき）
company_categories = {
    "野村證券": "国内系", "バークレイズ証券": "外資系", "BNPパリバ証券": "フランス", "シティグループ証券": "米国",
    "ビーオブエー証券": "米国", "ＳＭＢＣ日興証券": "国内系", "ＵＢＳ証券": "スイス", "日産証券": "日本",
    "インタラクティブ証券": "外資系", "フィリップ証券": "外資系", "モルガン・スタンレー": "米国", "松井証券": "国内系",
    "楽天証券": "国内系", "東海東京証券": "国内系", "アイザワ証券": "国内系"
}

# カテゴリと色をデータフレームにマッピング
data['カテゴリ'] = data['証券会社'].map(company_categories)
data['色'] = data['カテゴリ'].map(categories)

# 棒グラフをカラーコードに基づいて描画
plt.figure(figsize=(12, 8))
for category, group in data.groupby('カテゴリ'):
    plt.barh(group['証券会社'], group['取引量'], color=group['色'].iloc[0], label=category)

plt.xlabel('取引量')
plt.ylabel('証券会社')
plt.title('証券会社ごとの取引量（カテゴリ別色分け）')
plt.gca().invert_yaxis()  # y軸を降順に表示
plt.legend(title='カテゴリ')
plt.show()