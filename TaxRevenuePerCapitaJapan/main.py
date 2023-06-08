import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

# CSVファイルを読み込む
df = pd.read_csv('./TaxRevenuePerCapitaJapan/z-024.csv', encoding='shift_jis', skiprows=2)

# 最初の48行だけを取得
df = df.iloc[:48]

# 欠損値の処理
df = df.fillna(0)

# データ型の変換
df['地方税計'] = df['地方税計'].astype(float)

# '地方税計'列を抽出
local_tax = df[['Unnamed: 0', '地方税計']]

# プロットの準備
plt.figure(figsize=(10, 5))
plt.bar(local_tax['Unnamed: 0'], local_tax['地方税計'])
plt.xlabel('都道府県')
plt.ylabel('人口1人あたりの税収額の指数')
plt.title('各都道府県の地方税計の人口1人あたりの税収額の指数')
plt.xticks(rotation=90)  # x軸ラベルを90度回転させる
plt.show()
