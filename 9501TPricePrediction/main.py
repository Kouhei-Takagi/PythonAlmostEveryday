import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 東京電力の株価データの取得
symbol = "9501.T"
start_date = "2022-05-23"
end_date = "2023-05-22"
data = yf.download(symbol, start=start_date, end=end_date)

# ARIMAモデルによる株価予測
series = data['Close']
model = ARIMA(series, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=30)

# 予測結果の値とインデックスを取得
forecast_values = forecast
last_date = data.index[-1]
index = pd.date_range(start=last_date, periods=len(forecast_values), freq='B')

# グラフの描画
plt.plot(data['Close'], label='Actual Price')
plt.plot(index, forecast_values, label='Forecasted Price')
plt.title("Stock Price of {}".format(symbol))
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.show()
