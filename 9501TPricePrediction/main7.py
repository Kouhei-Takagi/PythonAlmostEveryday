import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

class StockPricePredictor:
    def __init__(self, symbol, start_date, end_date, features, target):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.features = features
        self.target = target
        self.model = RandomForestRegressor()
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def fetch_data(self):
        # 東京電力の株価データを取得
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        
    def prepare_data(self):
        # データをトレーニングセットとテストセットに分割
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data[self.features], self.data[self.target], test_size=0.2, shuffle=False)
        
    def train_model(self):
        # 予測モデルの選択と学習
        self.model.fit(self.X_train, self.y_train)
        
    def predict(self, prediction_data):
        # 未来の株価を予測
        return self.model.predict(prediction_data)
        
    def calculate_rmse(self):
        # テストセットを用いて予測を行う
        y_pred = self.model.predict(self.X_test)
        
        # 平均二乗誤差（MSE）の計算
        mse = mean_squared_error(self.y_test, y_pred)
        
        return mse
    
    def plot_forecast(self, prediction_data, forecast):
        # グラフの描画
        plt.plot(self.data.index, self.data[self.target], label='Actual Price')
        plt.plot(prediction_data.index, forecast, label='Forecasted Price')
        plt.title("Stock Price of {}".format(self.symbol))
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        plt.show()

# 使用例
symbol = "9501.T"
start_date = "2015-01-01"
end_date = "2023-05-21"
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# StockPricePredictorクラスのインスタンス化
predictor = StockPricePredictor(symbol, start_date, end_date, features, target)

# 株価データの取得
predictor.fetch_data()

# データの準備
predictor.prepare_data()

# モデルの学習
predictor.train_model()

# 予測期間の特徴量データを取得
prediction_data = predictor.data[features].tail(30)

# 未来の株価を予測
forecast = predictor.predict(prediction_data)

# 予測結果の可視化
predictor.plot_forecast(prediction_data, forecast)

# モデルの精度（MSE）の計算と表示
mse = predictor.calculate_rmse()
print("Mean Squared Error (MSE):", mse)
