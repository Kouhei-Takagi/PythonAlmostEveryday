import yfinance as yf
import pandas as pd

class Data:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
    
    def get_data(self):
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return data

# カカオのデータの取得
cacao_instance = Data("CC=F", "1990-01-01", "2024-03-31")
cacao_data = cacao_instance.get_data()

# 銅のデータの取得
copper_instance = Data("HG=F", "1990-01-01", "2024-03-31")
copper_data = copper_instance.get_data()

# 砂糖のデータ取得
sugar_instance = Data("SB=F", "1990-01-01", "2024-03-31")
sugar_data = sugar_instance.get_data()

# ナスダックのデータの取得
nasdaq_instance = Data("^IXIC", "1990-01-01", "2024-03-31")
nasdaq_data = nasdaq_instance.get_data()

# 終値の列のみを抽出してデータフレームに結合
merged_data = pd.concat([
    cacao_data["Close"].rename("Cacao_Close"),
    copper_data["Close"].rename("Copper_Close"),
    sugar_data["Close"].rename("Sugar_Close"),
    nasdaq_data["Close"].rename("Nasdaq_Close")
], axis=1).dropna()

# 相関係数を計算
correlation_matrix = merged_data.corr()

""""
# ナスダックと他の商品の相関係数を表示
print("ナスダックとカカオの相関係数:", correlation_matrix.loc["Cacao_Close", "Nasdaq_Close"])
print("ナスダックと銅の相関係数:", correlation_matrix.loc["Copper_Close", "Nasdaq_Close"])
print("ナスダックと砂糖の相関係数:", correlation_matrix.loc["Sugar_Close", "Nasdaq_Close"])
"""

# 列名を変数として定義
cacao_close_col = "Cacao_Close"
copper_close_col = "Copper_Close"
sugar_close_col = "Sugar_Close"
nasdaq_close_col = "Nasdaq_Close"

# 終値の列のみを抽出してデータフレームに結合
merged_data = pd.concat([
    cacao_data["Close"].rename(cacao_close_col),
    copper_data["Close"].rename(copper_close_col),
    sugar_data["Close"].rename(sugar_close_col),
    nasdaq_data["Close"].rename(nasdaq_close_col)
], axis=1).dropna()

#print(merged_data.tail())

# 列の各要素を正規化
merged_data["cacao_close_col_normal"] = merged_data[cacao_close_col] * 2
merged_data["copper_close_col_normal"] = merged_data[copper_close_col] * 400
merged_data["sugar_close_col_normal"] = merged_data[sugar_close_col] * 800

# 列の各要素を処理
merged_data[f"{cacao_close_col}_processed"] = merged_data["cacao_close_col_normal"] ** 0.475
merged_data[f"{copper_close_col}_processed"] = merged_data["copper_close_col_normal"] ** 0.595
merged_data[f"{sugar_close_col}_processed"] = merged_data["sugar_close_col_normal"] ** 0.395

# 新しい混合要素を作成
merged_data["mixed_close"] = merged_data[f"{cacao_close_col}_processed"] + merged_data[f"{copper_close_col}_processed"] - merged_data[f"{sugar_close_col}_processed"]

# 新しい混合要素とナスダックの相関係数を表示
correlation_matrix = merged_data.corr()
print("ナスダックと混合要素の相関係数:", correlation_matrix.loc["mixed_close", "Nasdaq_Close"])

import numpy as np
from scipy.optimize import minimize
from scipy.stats import pearsonr

# 既に取得したデータフレーム merged_data を使用
# merged_data には Cacao_Close, Copper_Close, Sugar_Close, Nasdaq_Close が含まれているとします

# 目的関数の定義: 相関係数を最大化
def objective(params):
    a, b, c = params  # 各商品価格に対する係数
    # 混合要素の計算: ここでは単純化のため、係数を乗算していますが、冪乗等の処理も可能
    mixed_close = (merged_data['Cacao_Close'] * a) * (merged_data['Copper_Close'] ** b) - (merged_data['Sugar_Close'] ** c)
    # ナスダック終値との相関係数
    corr, _ = pearsonr(mixed_close, merged_data['Nasdaq_Close'])
    return -corr  # 最大化のための負の相関係数

# 初期係数
initial_params = [1, 1, 1]  # 仮の初期値

# 最適化の実行: 方法は 'Powell' など、問題に適したものを選択
result = minimize(objective, initial_params, method='Powell')

# 最適化された係数の表示
print(f"Optimized Coefficients: {result.x}")
print(f"Maximum Correlation: {-result.fun}")