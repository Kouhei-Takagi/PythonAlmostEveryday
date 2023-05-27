import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Gold価格のデータの取得
symbol = "GC=F"
start_date = "2015-01-01"
end_date = "2023-05-26"
goldData = yf.download(symbol, start=start_date, end=end_date)

# 日経平均株価のデータの取得
symbol = "^N225"
start_date = goldData.index[0].strftime("%Y-%m-%d")  # Goldデータの最初の日付を取得
nikkeiData = yf.download(symbol, start=start_date, end=end_date)

# USD/JPYの為替レートのデータの取得
symbol = "JPY=X"  # Yahoo FinanceではJPY=XがUSD/JPYを表す
start_date = goldData.index[0].strftime("%Y-%m-%d")  # Goldデータの最初の日付を取得
exchangeData = yf.download(symbol, start=start_date, end=end_date)

# 終値の列のみを抽出
gold_close = goldData["Close"]
nikkei_close = nikkeiData["Close"]
exchange_rate = exchangeData["Close"]

# データの長さ確認
print("Gold Close:", len(gold_close))
print("Nikkei Close:", len(nikkei_close))
print("Exchange Rate:", len(exchange_rate))

# データの結合と欠損値の除去
merged_data = pd.concat([gold_close, nikkei_close, exchange_rate], axis=1, join="inner")
merged_data.columns = ["Gold Close", "Nikkei Close", "Exchange Rate"]

# 終値データを再取得
gold_close = merged_data["Gold Close"]
nikkei_close = merged_data["Nikkei Close"]
exchange_rate = merged_data["Exchange Rate"]

# データの長さの再確認
print("Gold Close:", len(gold_close))
print("Nikkei Close:", len(nikkei_close))
print("Exchange Rate:", len(exchange_rate))

# ドル建て価格の計算
dollar_nikkei_close = nikkei_close / exchange_rate

# 終値データの相関係数を計算
correlation = gold_close.corr(dollar_nikkei_close)

# グラフ化
plt.scatter(gold_close, dollar_nikkei_close)
plt.xlabel("Gold Close Price")
plt.ylabel("Dollar Nikkei Close Price")
plt.title(f"Correlation: {correlation:.2f}")
plt.show()

print("相関係数:", correlation)
