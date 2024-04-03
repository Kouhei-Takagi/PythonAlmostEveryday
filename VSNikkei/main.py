from Data.data import Data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# カカオのデータの取得
symbol = "CC=F"
start_date = "1990-01-01"
end_date = "2024-03-31"
cacao_instance = Data(symbol, start_date, end_date)

# 銅株価のデータの取得
symbol = "HG=F"
start_date = "1990-01-01"
end_date = "2024-03-31"
copper_instance = Data(symbol, start_date, end_date)

# 砂糖価格のデータ取得
symbol = "SB=F"
start_date = "1990-01-01"
end_date = "2024-03-31"
sugar_instance = Data(symbol, start_date, end_date)

# 日経平均株価のデータの取得
symbol = "^N225"
start_date = "1990-01-01"
end_date = "2024-03-31"
nikkei_instance = Data(symbol, start_date, end_date)

# USD/JPYの為替レートのデータの取得
symbol = "JPY=X"
start_date = "1990-01-01"
end_date = "2024-03-31"
exchange_instance = Data(symbol, start_date, end_date)

# 終値の列のみを抽出
cacao_close = cacao_instance.get_data()["Close"]
copper_close = copper_instance.get_data()["Close"]
suger_close = sugar_instance.get_data()["Close"]
nikkei_close = nikkei_instance.get_data()["Close"]
exchange_rate = exchange_instance.get_data()["Close"]

"""
# データの末尾確認
print(cacao_close.tail())
print(copper_close.tail())
print(suger_close.tail())
print(nikkei_close.tail())
print(exchange_rate.tail())

# データの長さ確認
print("cacao Close:", len(cacao_close))
print("copper Close:", len(copper_close))
print("suger Close:", len(suger_close))
print("nikkei Close:", len(nikkei_close))
print("exchange rate:", len(exchange_rate))
"""

# データの結合と欠損値の除去
merged_data = pd.concat([cacao_close, copper_close, suger_close,nikkei_close, exchange_rate], axis=1, join="inner")
merged_data.columns = ["Cacao Close", "Copper Close", "Suger Close","Nikkei Close", "Exchange Rate"]

"""
# 終値データを再取得
cacao_close = merged_data["Cacao Close"]
copper_close = merged_data["Copper Close"]
suger_close = merged_data["Suger Close"]
nikkei_close = merged_data["Nikkei Close"]
exchange_rate = merged_data["Exchange Rate"]

# データの長さ再確認
print("cacao Close:", len(cacao_close))
print("copper Close:", len(copper_close))
print("suger Close:", len(suger_close))
print("nikkei Close:", len(nikkei_close))
print("exchange rate:", len(exchange_rate))
"""

# ドル建て価格の計算
nikkei_close = nikkei_close / exchange_rate

# 正規化
cacao_close = cacao_close * 0.05
copper_close = copper_close * 100
suger_close = suger_close * 15

# 終値データの相関係数を計算
correlationCacao = cacao_close.corr(nikkei_close)
correlationCopper = copper_close.corr(nikkei_close)
correlationSuger = suger_close.corr(nikkei_close)

# 計算した相関係数を出力
print("Correlation Cacao and Nikkei:", correlationCacao)
print("Correlation Copper and Nikkei:", correlationCopper)
print("Correlation Suger and Nikkei:", correlationSuger)

# 混合した終値データの相関係数を計算
mixed = copper_close ** (5 / 13)
correlationMixed5and13 = mixed.corr(nikkei_close)
print(correlationMixed5and13)

mixed2 = copper_close ** (6 / 13)
correlationMixed2 = mixed2.corr(nikkei_close)
print(correlationMixed2)

mixed3 = copper_close ** (7 / 13)
correlationMixed3 = mixed3.corr(nikkei_close)
print(correlationMixed3)

mixed4 = copper_close ** 0.46
correlationMixed4 = mixed4.corr(nikkei_close)
print(correlationMixed4)

mixed5 = copper_close ** 0.48
correlationMixed5 = mixed5.corr(nikkei_close)
print(correlationMixed5)

mixed6 = copper_close ** 0.47
correlationMixed6 = mixed6.corr(nikkei_close)
print(correlationMixed6)

mixed7 = (cacao_close ** 0.31) * (copper_close ** 0.46)
correlationMixed7 = mixed7.corr(nikkei_close)
print(correlationMixed7)

mixed8 = (cacao_close ** 0.31) + (copper_close ** 0.46)
correlationMixed8 = mixed8.corr(nikkei_close)
print(correlationMixed8)

mixed9 = (cacao_close ** 0.31) + (copper_close ** 0.46) - (suger_close ** 0.37)
correlationMixed9 = mixed9.corr(nikkei_close)
print(correlationMixed9)