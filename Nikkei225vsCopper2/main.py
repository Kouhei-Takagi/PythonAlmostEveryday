import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# copper価格のデータの取得
symbol = "HG=F"
start_date = "2015-01-01"
end_date = "2023-05-26"
copperData = yf.download(symbol, start=start_date, end=end_date)

# 日経平均株価のデータの取得
symbol = "^N225"
start_date = copperData.index[0].strftime("%Y-%m-%d")  # copperデータの最初の日付を取得
nikkeiData = yf.download(symbol, start=start_date, end=end_date)

# USD/JPYの為替レートのデータの取得
symbol = "JPY=X"  # Yahoo FinanceではJPY=XがUSD/JPYを表す
start_date = copperData.index[0].strftime("%Y-%m-%d")  # copperデータの最初の日付を取得
exchangeData = yf.download(symbol, start=start_date, end=end_date)

# 終値の列のみを抽出
copper_close = copperData["Close"]
nikkei_close = nikkeiData["Close"]
exchange_rate = exchangeData["Close"]

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

# 銅価格を6乗に正規化
copper_closePow6 = copper_close ** 6

# データをプロット
plt.figure(figsize=(14,8))
plt.plot(copper_closePow6.index, copper_closePow6, label='Copper Close Pow 6')
plt.plot(dollar_nikkei_close.index, dollar_nikkei_close, label='Nikkei Close (USD)')

plt.title('Copper Pow 6 vs Nikkei (in USD)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Save the figure as a PNG file
plt.savefig("./Nikkei225vsCopper2/copperPow6vsNikkei225USdollar.png")

plt.show()
