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
cacao_instance = Data("CC=F", "1990-01-01", "2024-03-31")
cacao_data = cacao_instance.get_data()

# 銅のデータの取得
copper_instance = Data("HG=F", "1990-01-01", "2024-03-31")
copper_data = copper_instance.get_data()

# 砂糖のデータ取得
sugar_instance = Data("SB=F", "1990-01-01", "2024-03-31")
sugar_data = sugar_instance.get_data()

# コーヒーのデータ取得
coffee_instance = Data("KC=F", "1990-01-01", "2024-03-31")
coffee_data = coffee_instance.get_data()

# ダウのデータの取得
dow_instance = Data("^DJI", "1990-01-01", "2024-03-31")
dow_data = dow_instance.get_data()

# 終値の列のみを抽出してデータフレームに結合
merged_data = pd.concat([
    cacao_data["Close"].rename("Cacao_Close"),
    copper_data["Close"].rename("Copper_Close"),
    sugar_data["Close"].rename("Sugar_Close"),
    coffee_data["Close"].rename("Coffee_Close"),
    dow_data["Close"].rename("Dow_Close")
], axis=1).dropna()

# 相関係数を計算
correlation_matrix = merged_data.corr()

# 列名を変数として定義
cacao_close_col = "Cacao_Close"
copper_close_col = "Copper_Close"
sugar_close_col = "Sugar_Close"
coffee_close_col = "Coffee_Close"
dow_close_col = "Dow_Close"

# 終値の列のみを抽出してデータフレームに結合
merged_data = pd.concat([
    cacao_data["Close"].rename(cacao_close_col),
    copper_data["Close"].rename(copper_close_col),
    sugar_data["Close"].rename(sugar_close_col),
    coffee_data["Close"].rename(coffee_close_col),
    dow_data["Close"].rename(dow_close_col)
], axis=1).dropna()

# 目的関数の定義: 相関係数を最大化
def objective(params):
    a, p_a, b, p_b, c, p_c, d, p_d = params  # 各商品価格に対する係数と冪乗
    # 混合要素の計算
    mixed_close = (merged_data['Cacao_Close'] * a) ** p_a  * \
                  (merged_data['Copper_Close'] * b) ** p_b - \
                  (merged_data['Sugar_Close'] * c) ** p_c * \
                  (merged_data["Coffee_Close"] * d) ** p_d
    # ダウ終値との相関係数
    corr, _ = pearsonr(mixed_close, merged_data['Dow_Close'])
    return -corr  # 最大化のための負の相関係数

# 初期係数と冪乗
initial_params = [1, 1, 1, 1, 1, 1, 1, 1]  # 係数と冪乗の初期値

# 最適化の実行
result = minimize(objective, initial_params, method='BFGS')

# 結果の表示
print(f"Optimized Coefficients and Powers: {result.x}")
print(f"Maximum Correlation: {-result.fun}")