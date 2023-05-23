import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 東京電力の株価データの取得
symbol = "9501.T"
start_date = "2015-01-01"
end_date = "2023-05-23"
data = yf.download(symbol, start=start_date, end=end_date)

# 特徴量と目的変数の準備
features = data[['Open', 'High', 'Low', 'Volume']]  # 使用する特徴量を選択
target = data['Close']

# データの分割
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# ランダムフォレストモデルの構築
model = RandomForestRegressor(n_estimators=100, random_state=42)

# モデルの学習
model.fit(X_train, y_train)

# テストデータを使って予測を実行
y_pred = model.predict(X_test)

# モデルの評価
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R^2):", r2)
