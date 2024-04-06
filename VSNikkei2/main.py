import yfinance as yf
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import pearsonr

class Data:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
    
    def get_data(self):
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return data

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
sugar_close = sugar_instance.get_data()["Close"]
nikkei_close = nikkei_instance.get_data()["Close"]
exchange_rate = exchange_instance.get_data()["Close"]

# データの結合と欠損値の除去
merged_data = pd.concat([cacao_close, copper_close, sugar_close,nikkei_close, exchange_rate], axis=1, join="inner")
merged_data.columns = ["Cacao Close", "Copper Close", "Sugar Close","Nikkei Close", "Exchange Rate"]

# ドル建て価格の計算
nikkei_close = nikkei_close / exchange_rate

# 目的関数の定義: 相関係数を最大化
def objective(params):
    a, p_a, b, p_b, c, p_c = params  # 各商品価格に対する係数と冪乗
    # 混合要素の計算
    mixed_close = (merged_data['Cacao Close'] * a) ** p_a  * \
                  (merged_data['Copper Close'] * b) ** p_b - \
                  (merged_data['Sugar Close'] * c) ** p_c
    # ドル建て日経平均終値との相関係数
    corr, _ = pearsonr(mixed_close, merged_data['Nikkei Close'])
    return -corr  # 最大化のための負の相関係数

# 初期係数と冪乗
initial_params = [1, 1, 1, 1, 1, 1]  # 係数と冪乗の初期値

# 最適化の実行
result = minimize(objective, initial_params, method='BFGS')

# 結果の表示
print(f"Optimized Coefficients and Powers: {result.x}")
print(f"Maximum Correlation: {-result.fun}")