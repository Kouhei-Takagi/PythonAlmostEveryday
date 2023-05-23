import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

class StockPricePredictor:
    def __init__(self, symbol, start_date, end_date, features, target):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.features = features
        self.target = target
        self.model = RandomForestRegressor()
        
    def fetch_data(self):
        # 日経平均の株価データを取得
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return data
    
    def prepare_data(self, data):
        # 特徴量とターゲットの準備
        X = data[self.features]
        y = data[self.target]
        
        # データの分割
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        # ランダムフォレスト回帰モデルの構築と学習
        self.model.fit(X_train, y_train)
    
    def predict(self, prediction_data):
        # 予測結果の取得
        return self.model.predict(prediction_data)
    
    def calculate_rmse(self, y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        return rmse
    
    def plot_forecast(self, data, forecast):
        # 予測結果のインデックスを作成
        last_date = data.index[-1]
        index = pd.date_range(start=last_date + pd.DateOffset(days=1), periods=len(forecast), freq='B')
        
        # グラフの描画
        plt.plot(data.index, data[self.target], label='Actual Price')
        plt.plot(index, forecast, label='Forecasted Price')
        plt.title("Stock Price of {}".format(self.symbol))
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        plt.show()

# 使用例
symbol = "^N225"
start_date = "2015-01-01"
end_date = "2023-05-21"
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# StockPricePredictorクラスのインスタンス化
predictor = StockPricePredictor(symbol, start_date, end_date, features, target)

# 株価データの取得
data = predictor.fetch_data()

# データの準備
X_train, X_test, y_train, y_test = predictor.prepare_data(data)

# モデルの学習
predictor.train_model(X_train, y_train)

# 予測期間の特徴量データを取得
prediction_data = data[features].tail(30)

# 予測結果の取得
forecast = predictor.predict(prediction_data)

# 予測結果の可視化
predictor.plot_forecast(data, forecast)

# テストデータでの予測精度（RMSE）の計算と表示
y_true = data[target][-len(y_test):]
y_pred = predictor.predict(X_test)
rmse = predictor.calculate_rmse(y_true, y_pred)
print("Test RMSE:", rmse)
