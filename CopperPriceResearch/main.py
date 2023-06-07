from Data.data import Data
from Research.research import Research
from Analysis.analysis import Analysis

# データの取得
symbol = "HG=F"
start_date = "2015-08-30"
end_date = "2023-06-06"
data_instance = Data(symbol, start_date, end_date)

# データの取得と表示
data = data_instance.get_data()
print(data)

# データの対数変換
research_instance = Research(data)
research = research_instance.calculate_log()
print(research)

# データのプロット
research_instance.plot_data()

# データの解析と予測
analysis_instance = Analysis(research)
forecast = analysis_instance.predict(steps=10)
print(forecast)

# データと予測のプロット
research_instance.plot_data(forecast)
