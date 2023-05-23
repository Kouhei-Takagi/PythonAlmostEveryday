import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import tkinter as tk

class StockPricePredictor:
    def __init__(self):
        self.symbol = "9501.T"
        self.start_date = "2015-01-01"
        self.end_date = None
        self.features = ['Open', 'High', 'Low', 'Volume']
        self.target = 'Close'
        self.model = RandomForestRegressor()
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def run(self):
        # Tkinterウィンドウの作成
        self.root = tk.Tk()
        
        # シンボルのエントリーボックス
        symbol_label = tk.Label(self.root, text="Symbol:")
        symbol_label.pack()
        symbol_entry = tk.Entry(self.root)
        symbol_entry.insert(tk.END, self.symbol)  # 初期値を設定
        symbol_entry.pack()

        # 開始日のエントリーボックス
        start_date_label = tk.Label(self.root, text="Start Date:")
        start_date_label.pack()
        start_date_entry = tk.Entry(self.root)
        start_date_entry.insert(tk.END, self.start_date)  # 初期値を設定
        start_date_entry.pack()

        # 実行ボタン
        button = tk.Button(self.root, text="Run", command=self.run_prediction)
        button.pack()

        # Tkinterウィンドウのメインループ
        self.root.mainloop()

    def run_prediction(self):
        # 入力値の取得
        self.symbol = symbol_entry.get()
        self.start_date = start_date_entry.get()

        # 東京電力の株価データの取得
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)

        # 特徴量として使用するデータの選択
        features = ['Open', 'High', 'Low', 'Volume']
        target = 'Close'

        # データをトレーニングセットとテストセットに分割
        X_train, X_test, y_train, y_test = train_test_split(self.data[features], self.data[target], test_size=0.2, shuffle=False)

        # 予測モデルの選択と学習
        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        # 予測期間の特徴量データを用意
        prediction_data = self.data[features].tail(30)

        # 未来の株価を予測
        forecast = model.predict(prediction_data)

        # グラフの描画
        plt.plot(self.data.index, self.data[target], label='Actual Price')
        plt.plot(prediction_data.index, forecast, label='Forecasted Price')
        plt.title("Stock Price of {}".format(self.symbol))
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        plt.show()

# StockPricePredictorクラスのインスタンス化
predictor = StockPricePredictor()

# GUIの実行
predictor.run()
