from Data.data import Data
import pandas as pd

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

# ナスダックのデータの取得
symbol = "^IXIC"
start_date = "1990-01-01"
end_date = "2024-03-31"
nasdaq_instance = Data(symbol, start_date, end_date)

# 終値の列のみを抽出
cacao_close = cacao_instance.get_data()["Close"]
copper_close = copper_instance.get_data()["Close"]
suger_close = sugar_instance.get_data()["Close"]
nasdaq_close = nasdaq_instance.get_data()["Close"]

"""
# データの末尾確認
print(cacao_close.tail())
print(copper_close.tail())
print(suger_close.tail())
print(nasdaq_close.tail())

# データの長さ確認
print("cacao Close:", len(cacao_close))
print("copper Close:", len(copper_close))
print("suger Close:", len(suger_close))
print("nasdaq Close:", len(nasdaq_close))
"""

# データの結合と欠損値の除去
merged_data = pd.concat([cacao_close, copper_close, suger_close,nasdaq_close], axis=1, join="inner")
merged_data.columns = ["Cacao Close", "Copper Close", "Suger Close","nasdaq Close"]


# 終値データを再取得
cacao_close = merged_data["Cacao Close"]
copper_close = merged_data["Copper Close"]
suger_close = merged_data["Suger Close"]
nasdaq_close = merged_data["nasdaq Close"]

# データの長さ再確認
print("cacao Close:", len(cacao_close))
print("copper Close:", len(copper_close))
print("suger Close:", len(suger_close))
print("nasdaq Close:", len(nasdaq_close))

# 正規化
cacao_close = cacao_close * 5
copper_close = copper_close * 1000
suger_close = suger_close * 200

# 終値データの相関係数を計算
correlationCacao = cacao_close.corr(nasdaq_close)
correlationCopper = copper_close.corr(nasdaq_close)
correlationSuger = suger_close.corr(nasdaq_close)

# 計算した相関係数を出力
print("Correlation Cacao and nasdaq:", correlationCacao)
print("Correlation Copper and nasdaq:", correlationCopper)
print("Correlation Suger and nasdaq:", correlationSuger)

# 混合した終値データの相関係数を計算
mixed = copper_close ** (5 / 13)
correlationMixed5and13 = mixed.corr(nasdaq_close)
print(correlationMixed5and13)

mixed2 = copper_close ** (6 / 13)
correlationMixed2 = mixed2.corr(nasdaq_close)
print(correlationMixed2)

mixed3 = copper_close ** (7 / 13)
correlationMixed3 = mixed3.corr(nasdaq_close)
print(correlationMixed3)

mixed4 = copper_close ** 0.46
correlationMixed4 = mixed4.corr(nasdaq_close)
print(correlationMixed4)

mixed5 = copper_close ** 0.48
correlationMixed5 = mixed5.corr(nasdaq_close)
print(correlationMixed5)

mixed6 = copper_close ** 0.47
correlationMixed6 = mixed6.corr(nasdaq_close)
print(correlationMixed6)

mixed7 = (cacao_close ** 0.31) * (copper_close ** 0.46)
correlationMixed7 = mixed7.corr(nasdaq_close)
print(correlationMixed7)

mixed8 = (cacao_close ** 0.31) + (copper_close ** 0.46)
correlationMixed8 = mixed8.corr(nasdaq_close)
print(correlationMixed8)

mixed9 = (cacao_close ** 0.31) + (copper_close ** 0.46) - (suger_close ** 0.37)
correlationMixed9 = mixed9.corr(nasdaq_close)
print(correlationMixed9)