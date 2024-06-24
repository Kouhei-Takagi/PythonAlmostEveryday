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
df.to_csv(f'./DATA/buy-securities_data_{today}.csv', index=False, encoding='utf-8')

print("CSVファイルが保存されました。")

# CSVファイルを読み込む
file_path = f'./DATA/buy-securities_data_{today}.csv'
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
plt.title('証券会社ごとの買い越し量')
plt.gca().invert_yaxis()  # y軸を降順に表示
plt.savefig(f'./DATA/buy-{today}.png')
plt.show()

# 特定の証券会社に色を適用するための詳細設定
highlight_companies = ["GMOクリック証券", "SBI証券", "楽天証券", "松井証券"]
global_macro_companies = ["ゴールドマン・サックス", "シティグループ証券", "ＪＰモルガン証券"]
highlight_color = "magenta"  # 特定の国内個人投資家向け証券会社
global_macro_color = "blue"  # グローバルマクロ戦略を採用する証券会社
default_color = "grey"  # デフォルトの色
cta_companies = ["クレディ・スイス", "モルガン・スタンレー"]
institutional_companies = ["みずほ証券", "野村證券"]
cta_color = "green"  # トレンドフォロー（CTA）戦略を採用する証券会社
institutional_color = "black"  # 国内機関投資家向け証券会社

# 棒グラフを描画（カテゴリ別色分けでさらに詳細化）
plt.figure(figsize=(12, 8))
for idx, row in data.iterrows():
    if row['証券会社'] in highlight_companies:
        color = highlight_color
    elif row['証券会社'] in global_macro_companies:
        color = global_macro_color
    elif row['証券会社'] in cta_companies:
        color = cta_color
    elif row['証券会社'] in institutional_companies:
        color = institutional_color
    else:
        color = default_color
    plt.barh(row['証券会社'], row['取引量'], color=color)

plt.xlabel('取引量')
plt.ylabel('証券会社')
plt.title('証券会社ごとの取引量（カテゴリ別色分け）')
plt.gca().invert_yaxis()  # y軸を降順に表示
plt.savefig(f'./DATA/colored-buy-{today}.png')
plt.show()
