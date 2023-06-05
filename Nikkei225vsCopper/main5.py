import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class MarketAnalysis:
    def __init__(self, start_date, end_date, copper_symbol="HG=F", nikkei_symbol="^N225", exchange_symbol="JPY=X"):
        self.start_date = start_date
        self.end_date = end_date
        self.copper_symbol = copper_symbol
        self.nikkei_symbol = nikkei_symbol
        self.exchange_symbol = exchange_symbol
        self.copper_close = None
        self.nikkei_close = None
        self.exchange_rate = None
        self.dollar_nikkei_close = None
        self.copper_closex80 = None

    def fetch_data(self):
        copperData = yf.download(self.copper_symbol, start=self.start_date, end=self.end_date)
        start_date = copperData.index[0].strftime("%Y-%m-%d")
        nikkeiData = yf.download(self.nikkei_symbol, start=start_date, end=self.end_date)
        exchangeData = yf.download(self.exchange_symbol, start=start_date, end=self.end_date)
        merged_data = pd.concat([copperData["Close"], nikkeiData["Close"], exchangeData["Close"]], axis=1, join="inner")
        merged_data.columns = ["copper Close", "Nikkei Close", "Exchange Rate"]
        self.copper_close = merged_data["copper Close"]
        self.nikkei_close = merged_data["Nikkei Close"]
        self.exchange_rate = merged_data["Exchange Rate"]
        self.dollar_nikkei_close = self.nikkei_close / self.exchange_rate
        self.copper_closex80 = self.copper_close * 80

    def plot_data(self, filename):
        plt.figure(figsize=(14,8))
        plt.plot(self.copper_closex80.index, self.copper_closex80, label='Copper Close x 80')
        plt.plot(self.dollar_nikkei_close.index, self.dollar_nikkei_close, label='Nikkei Close (USD)')
        plt.title('Copper x 80 vs Nikkei (in USD)')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.savefig(filename)
        plt.show()


# Use the class
analysis = MarketAnalysis("2015-01-01", "2023-05-26")
analysis.fetch_data()
analysis.plot_data("./Nikkei225vsCopper/copperx80vsNikkei225USdollar.png")
