import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import tkinter as tk

class StockPricePredictor:
    def __init__(self):
        self.symbol = None
        self.start_date = None
        self.end_date = None
        self.features = ['Open', 'High', 'Low', 'Volume']
        self.target = 'Close'
        self.model = RandomForestRegressor()
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def fetch_data(self):
        # 株価データを取得
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
        
    def run(self):
        # GUIウィンドウの作成
        window = tk.Tk()
        window.title("Stock Price Predictor")
        
        # シンボル入力のラベルとエントリーボックス
        symbol_label = tk.Label(window, text="Symbol:")
        symbol_label.pack()
        symbol_entry = tk.Entry(window)
        symbol_entry.pack()
        
        # 開始日入力のラベルとエントリーボックス
        start_date_label = tk.Label(window, text="Start Date:")
        start_date_label.pack()
        start_date_entry = tk.Entry(window)
        start_date_entry.pack()
        
        # 終了日入力のラベルとエントリーボックス
        end_date_label = tk.Label(window, text="End Date:")
        end_date_label.pack()
        end_date_entry = tk.Entry(window)
        end_date_entry.pack()
        
        # ボタンクリック時の処理
        def predict_button_click():
            # 入力値の取得
            self.symbol = symbol_entry.get()
            self.start_date = start_date_entry.get()
            self.end_date = end_date_entry.get()
            
            # データの取得と準備
            self.fetch_data()
            self.prepare_data()
            
            # モデルの学習
            self.train_model()
            
            # 予測期間の特徴量データを用意
            prediction_data = self.data[self.features].tail(30)
            
            # 未来の株価を予測
            forecast = self.predict(prediction_data)
            
            # 予測結果の可視化
            self.plot_forecast(prediction_data, forecast)
            
            # モデルの精度の計算と表示
            mse = self.calculate_rmse()
            print("Mean Squared Error (MSE):", mse)
        
        # 予測ボタン
        predict_button = tk.Button(window, text="Predict", command=predict_button_click)
        predict_button.pack()
        
        # GUIのメインループ
        window.mainloop()

# StockPricePredictorクラスのインスタンス化
predictor = StockPricePredictor()

# GUIの実行
predictor.run()
