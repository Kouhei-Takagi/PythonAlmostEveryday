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
        return data["Close"].to_frame(name=self.symbol)  # 終値のDataFrameを返す

# インスタンスの作成とデータの取得
cacao_instance = Data("CC=F", "1990-01-01", "2024-03-31")
cacao_close_df = cacao_instance.get_data().rename(columns={"CC=F": "Cacao Close"})

copper_instance = Data("HG=F", "1990-01-01", "2024-03-31")
copper_close_df = copper_instance.get_data().rename(columns={"HG=F": "Copper Close"})

sugar_instance = Data("SB=F", "1990-01-01", "2024-03-31")
sugar_close_df = sugar_instance.get_data().rename(columns={"SB=F": "Sugar Close"})

nikkei_instance = Data("^N225", "1990-01-01", "2024-03-31")
nikkei_close_df = nikkei_instance.get_data().rename(columns={"^N225": "Nikkei Close"})

exchange_instance = Data("JPY=X", "1990-01-01", "2024-03-31")
exchange_rate_df = exchange_instance.get_data().rename(columns={"JPY=X": "Exchange Rate"})

# データフレームの結合とドル建て日経平均株価の計算
merged_data = pd.concat([cacao_close_df, copper_close_df, sugar_close_df, nikkei_close_df, exchange_rate_df], axis=1)
merged_data["Nikkei Close USD"] = merged_data["Nikkei Close"] / merged_data["Exchange Rate"]
merged_data_clean = merged_data.dropna()

# 目的関数
def objective(params):
    a, p_a, b, p_b, c, p_c = params
    mixed_close = (merged_data_clean['Cacao Close'] * a) ** p_a * \
                  (merged_data_clean['Copper Close'] * b) ** p_b - \
                  (merged_data_clean['Sugar Close'] * c) ** p_c
    corr, _ = pearsonr(mixed_close, merged_data_clean['Nikkei Close USD'])
    return -corr

# 初期係数と冪乗、最適化の実行、結果の表示
initial_params = [1, 1, 1, 1, 1, 1]  # 係数と冪乗の初期値
result = minimize(objective, initial_params, method='BFGS')
print(f"Optimized Coefficients and Powers: {result.x}")
print(f"Maximum Correlation: {-result.fun}")