import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class CorrelationAnalysis:
    def __init__(self, nikkei_symbol, exchange_symbol, gold_symbol, silver_symbol, copper_symbol, start_date, end_date):
        self.nikkei_symbol = nikkei_symbol
        self.exchange_symbol = exchange_symbol
        self.gold_symbol = gold_symbol
        self.silver_symbol = silver_symbol
        self.copper_symbol = copper_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.nikkei_dollar_close = None
        self.gold_close = None
        self.silver_close = None
        self.copper_close = None
        self.correlations = {}

    def fetch_data(self):
        # 日経平均株価のドル建て価格のデータを取得
        nikkei_data = yf.download(self.nikkei_symbol, start=self.start_date, end=self.end_date)
        exchange_data = yf.download(self.exchange_symbol, start=self.start_date, end=self.end_date)
        self.nikkei_dollar_close = nikkei_data["Close"] / exchange_data["Close"]

        # 金、銀、銅の価格データを取得
        gold_data = yf.download(self.gold_symbol, start=self.start_date, end=self.end_date)
        silver_data = yf.download(self.silver_symbol, start=self.start_date, end=self.end_date)
        copper_data = yf.download(self.copper_symbol, start=self.start_date, end=self.end_date)
        self.gold_close = gold_data["Close"]
        self.silver_close = silver_data["Close"]
        self.copper_close = copper_data["Close"]

    def calculate_correlations(self):
        # 相関係数を計算
        self.correlations["Gold"] = self.nikkei_dollar_close.corr(self.gold_close)
        self.correlations["Silver"] = self.nikkei_dollar_close.corr(self.silver_close)
        self.correlations["Copper"] = self.nikkei_dollar_close.corr(self.copper_close)

    def plot_correlations(self):
        # 相関係数のグラフ化
        labels = list(self.correlations.keys())
        values = list(self.correlations.values())

        plt.bar(labels, values)
        plt.xlabel("Commodity")
        plt.ylabel("Correlation with Nikkei Dollar Close")
        plt.title("Correlation Analysis")
        plt.show()

    def run_analysis(self):
        self.fetch_data()
        self.calculate_correlations()
        self.plot_correlations()

# 使用例
nikkei_symbol = "^N225"
exchange_symbol = "JPY=X"
gold_symbol = "GC=F"
silver_symbol = "SI=F"
copper_symbol = "HG=F"
start_date = "2015-01-01"
end_date = "2023-05-26"

correlation_analysis = CorrelationAnalysis(nikkei_symbol, exchange_symbol, gold_symbol, silver_symbol, copper_symbol, start_date, end_date)
correlation_analysis.run_analysis()
