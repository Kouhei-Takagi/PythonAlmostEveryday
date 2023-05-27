import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class CorrelationAnalysis:
    def __init__(self, gold_symbol, nikkei_symbol, exchange_symbol, start_date, end_date):
        self.gold_symbol = gold_symbol
        self.nikkei_symbol = nikkei_symbol
        self.exchange_symbol = exchange_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.gold_close = None
        self.nikkei_close = None
        self.exchange_rate = None
        self.correlation = None

    def fetch_data(self):
        gold_data = yf.download(self.gold_symbol, start=self.start_date, end=self.end_date)
        nikkei_data = yf.download(self.nikkei_symbol, start=gold_data.index[0].strftime("%Y-%m-%d"), end=self.end_date)
        exchange_data = yf.download(self.exchange_symbol, start=gold_data.index[0].strftime("%Y-%m-%d"), end=self.end_date)

        self.gold_close = gold_data["Close"]
        self.nikkei_close = nikkei_data["Close"]
        self.exchange_rate = exchange_data["Close"]

    def calculate_correlation(self):
        merged_data = pd.concat([self.gold_close, self.nikkei_close, self.exchange_rate], axis=1, join="inner")
        merged_data.columns = ["Gold Close", "Nikkei Close", "Exchange Rate"]
        self.gold_close = merged_data["Gold Close"]
        self.nikkei_close = merged_data["Nikkei Close"]
        self.exchange_rate = merged_data["Exchange Rate"]
        self.correlation = self.gold_close.corr(self.nikkei_close)

    def plot_correlation(self):
        plt.scatter(self.gold_close, self.nikkei_close)
        plt.xlabel("Gold Close Price")
        plt.ylabel("Dollar Nikkei Close Price")
        plt.title(f"Correlation: {self.correlation:.2f}")
        plt.show()

    def run_analysis(self):
        self.fetch_data()
        self.calculate_correlation()
        self.plot_correlation()
        print("相関係数:", self.correlation)

# 使用例
gold_symbol = "GC=F"
nikkei_symbol = "^N225"
exchange_symbol = "JPY=X"
start_date = "2013-01-01"
end_date = "2023-05-26"

correlation_analysis = CorrelationAnalysis(gold_symbol, nikkei_symbol, exchange_symbol, start_date, end_date)
correlation_analysis.run_analysis()
