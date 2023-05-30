import numpy as np
from sklearn.linear_model import LinearRegression

Years = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
RemainingGovtBond = np.array([814.3, 848.1, 873.1, 901.5, 926.8, 947.7, 966.3, 977.8, 1105.2, 1129.9])
MeimokuGDP = np.array([512.5, 523.4, 540.7, 544.8, 555.7, 556.6, 556.8, 537.6, 550.7, 561.2])

# 線形回帰モデルの作成と予測
model_balance = LinearRegression()
model_balance.fit(Years.reshape(-1, 1), RemainingGovtBond)
predicted_balance = model_balance.predict(Years.reshape(-1, 1))

model_gdp = LinearRegression()
model_gdp.fit(Years.reshape(-1, 1), MeimokuGDP)
predicted_gdp = model_gdp.predict(Years.reshape(-1, 1))

# 2022年から2028年までの国債残高÷名目GDPの割合の予測値を計算
years_future = np.array(range(2022, 2029))
predicted_balance_future = model_balance.predict(years_future.reshape(-1, 1))
predicted_gdp_future = model_gdp.predict(years_future.reshape(-1, 1))
predicted_balance_gdp_ratio_future = predicted_balance_future / predicted_gdp_future

# 2022年から2028年までの予測結果の表示
for year, ratio in zip(years_future, predicted_balance_gdp_ratio_future):
    print(year, "年の国債残高÷名目GDPの予測値:", ratio)
