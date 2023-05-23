import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 東京電力の株価データの取得
symbol = "9501.T"
start_date = "2015-01-01"
end_date = "2023-05-22"
data = yf.download(symbol, start=start_date, end=end_date)

# 特徴量とターゲットの準備
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

X = data[features]
y = data[target]

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# ランダムフォレスト回帰モデルの構築と学習
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 予測期間の特徴量データを取得
prediction_data = data[features].tail(90)

# 予測結果の取得
forecast = model.predict(prediction_data)

# 予測結果のインデックスを作成
last_date = data.index[-1]
index = pd.date_range(start=last_date + pd.DateOffset(days=1), periods=len(forecast), freq='B')

# グラフの描画
plt.plot(data.index, data['Close'], label='Actual Price')
plt.plot(index, forecast, label='Forecasted Price')
plt.title("Stock Price of {}".format(symbol))
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.show()
