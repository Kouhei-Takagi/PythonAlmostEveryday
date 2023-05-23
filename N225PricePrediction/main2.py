import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# 日経平均の株価データの取得
symbol = "^N225"
start_date = "2015-01-01"
end_date = "2023-05-21"
data = yf.download(symbol, start=start_date, end=end_date)

# 特徴量として使用するデータの選択
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# データをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, shuffle=False)

# 予測モデルの選択と学習
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 予測期間の特徴量データを用意
prediction_data = data[features].tail(30)

# 未来の株価を予測
forecast = model.predict(prediction_data)

# グラフの描画
plt.plot(data.index, data[target], label='Actual Price')
plt.plot(prediction_data.index, forecast, label='Forecasted Price')
plt.title("Stock Price of {}".format(symbol))
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.show()

# テストセットを用いて予測を行う
y_pred = model.predict(X_test)

# 平均二乗誤差（MSE）の計算
mse = mean_squared_error(y_test, y_pred)

# モデルの精度を表示
print("Mean Squared Error (MSE):", mse)