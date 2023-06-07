from Data.data import Data
from Analysis.analysis import PricePredictor

# データの取得
symbol = "HG=F"
start_date = "2015-01-01"
end_date = "2023-06-06"
data_instance = Data(symbol, start_date, end_date)

# データの取得と表示
data = data_instance.get_data()
print(data)

# データの分析
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# PricePredictorクラスのインスタンス化
predictor = PricePredictor(data, symbol, start_date, end_date, features, target)

# データの準備
predictor.prepare_data()

# モデルの学習
predictor.train_model()

# 予測期間の特徴量データを取得
prediction_data = predictor.data[features].tail(30)

# 未来の価格を予測
forecast = predictor.predict(prediction_data)

# 予測結果の可視化
predictor.plot_forecast(prediction_data, forecast)

# モデルの精度（MSE）の計算と表示
mse = predictor.calculate_rmse()
print("Mean Squared Error (MSE):", mse)