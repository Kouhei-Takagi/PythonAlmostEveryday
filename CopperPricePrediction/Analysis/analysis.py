from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import time

class PricePredictor:
    def __init__(self, data, symbol, start_date, end_date, features, target):
        self.data = data
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.features = features
        self.target = target
        self.model = RandomForestRegressor()

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

        #PNG形式で保存
        date = time.strftime("%Y%m%d")
        plt.savefig(f"./CopperPricePrediction/copperPricePrediction{date}.png")
        
        #グラフの表示
        plt.show()