from Data.data import Data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 銅のデータの取得
symbol = "HG=F"
start_date = "2015-01-01"
end_date = "2023-06-06"
copper_instance = Data(symbol, start_date, end_date)

# 日経平均株価のデータの取得
symbol = "^N225"
start_date = "2015-01-01"
end_date = "2023-06-06"
nikkei225_instance = Data(symbol, start_date, end_date)

# USD/JPYの為替レートのデータの取得
symbol = "JPY=X"
start_date = "2015-01-01"
end_date = "2023-06-06"
exchange_instance = Data(symbol, start_date, end_date)

# 終値の列のみを抽出
copper_close = copper_instance.get_data()["Close"]
nikkei_close = nikkei225_instance.get_data()["Close"]
exchange_rate = exchange_instance.get_data()["Close"]

# データの長さ確認
print("copper Close:", len(copper_close))
print("Nikkei Close:", len(nikkei_close))
print("Exchange Rate:", len(exchange_rate))

# データの結合と欠損値の除去
merged_data = pd.concat([copper_close, nikkei_close, exchange_rate], axis=1, join="inner")
merged_data.columns = ["copper Close", "Nikkei Close", "Exchange Rate"]

# 終値データを再取得
copper_close = merged_data["copper Close"]
nikkei_close = merged_data["Nikkei Close"]
exchange_rate = merged_data["Exchange Rate"]

# データの長さの再確認
print("copper Close:", len(copper_close))
print("Nikkei Close:", len(nikkei_close))
print("Exchange Rate:", len(exchange_rate))

# ドル建て価格の計算
dollar_nikkei_close = nikkei_close / exchange_rate

# 日経平均株価のドル建て価格のプロット
fig, axs = plt.subplots(3, 1, figsize=(8, 16))

axs[0].plot(dollar_nikkei_close, label="Nikkei225 Price")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("Nikkei225 Price")
axs[0].legend()

# 銅価格のプロット
axs[1].plot(copper_close, label="Copper Price", color="orange")
axs[1].set_xlabel("Date")
axs[1].set_ylabel("Copper Price")
axs[1].legend()

# 銅価格を80倍に正規化
copper_closex80 = copper_close * 80

# 終値データの相関係数を計算
correlation = copper_closex80.corr(dollar_nikkei_close)
print("Correlation:", correlation)

# データのプロット
axs[2].scatter(copper_closex80, dollar_nikkei_close, label="Data", color="green")
axs[2].set_xlabel("Copper Price x 80")
axs[2].set_ylabel("Nikkei225 Price")
axs[2].legend()

plt.tight_layout()
plt.savefig("./Nikkei225vsCopper4/main.png")
plt.show()

# copper_close, dollar_nikkei_close を合わせたデータフレームを作成
df = pd.DataFrame({
    'copper_price': copper_closex80,
    'nikkei_price': dollar_nikkei_close
})

# クラスタリングを実施
kmeans = KMeans(n_clusters=3, random_state=42).fit(df)

# クラスタリングの結果を取得
df['cluster'] = kmeans.labels_

# クラスタごとに色を分けてプロット
colors = ['blue', 'green', 'red']
for i, color in enumerate(colors):
    subset = df[df['cluster'] == i]
    plt.scatter(subset['copper_price'], subset['nikkei_price'], c=color, label=f'cluster {i}')

plt.xlabel('Copper Price x 80')
plt.ylabel('Nikkei Price')
plt.legend()
plt.savefig("./Nikkei225vsCopper4/main2.png")
plt.show()
