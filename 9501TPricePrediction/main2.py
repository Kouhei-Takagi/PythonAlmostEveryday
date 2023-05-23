import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

class StockPricePredictor:
    def __init__(self, symbol, start_date, end_date, order=(1, 1, 1)):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.order = order
        self.data = None
        self.forecast = None

    def download_data(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)

    def fit_arima(self):
        series = self.data['Close']
        model = ARIMA(series, order=self.order)
        model_fit = model.fit()
        self.forecast = model_fit.forecast(steps=30)

    def plot_forecast(self):
        forecast_values = self.forecast
        last_date = self.data.index[-1]
        index = pd.date_range(start=last_date, periods=len(forecast_values), freq='B')

        plt.plot(self.data['Close'], label='Actual Price')
        plt.plot(index, forecast_values, label='Forecasted Price')
        plt.title("Stock Price of {}".format(self.symbol))
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        plt.show()

# 使用例
symbol = "9501.T"
start_date = "2022-05-23"
end_date = "2023-05-22"

predictor = StockPricePredictor(symbol, start_date, end_date)
predictor.download_data()
predictor.fit_arima()
predictor.plot_forecast()
