import matplotlib.pyplot as plt

Years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
RemainingGovtBond = [814.3, 848.1, 873.1, 901.5, 926.8, 947.7, 966.3, 977.8, 1105.2, 1129.9]
NewGovtBond = [251.8, 264.8, 260.4, 263.9, 269.8, 276, 279.3, 282.5, 366.1, 342.4]
RefinancingGovtBond = [442.8, 469.9, 506.1, 535.3, 553.7, 573, 592.1, 601.2, 615.2, 645.5]
MeimokuGDP = [512.5, 523.4, 540.7, 544.8, 555.7, 556.6, 556.8, 537.6, 550.7, 561.2]
Gov2yearsYeild = -0.06
Gov5yearsYeild = 0.112
Gov10yearsYeild = 0.453
Gov20yearsYeild = 1.044

#国債利回りの平均を計算
GovYeild = (Gov2yearsYeild + Gov5yearsYeild + Gov10yearsYeild + Gov20yearsYeild) / 4
print(GovYeild)

#国債利払の計算
GovBondPayment = [bond * GovYeild / 100 for bond in RemainingGovtBond]
print(GovBondPayment)

#名目GDPに占める国債利払の割合の計算
GovBondPaymentRatio = [100 * payment / GDP for payment, GDP in zip(GovBondPayment, MeimokuGDP)]
print(GovBondPaymentRatio)

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

Years = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
RemainingGovtBond = np.array([814.3, 848.1, 873.1, 901.5, 926.8, 947.7, 966.3, 977.8, 1105.2, 1129.9])

# 線形回帰モデルの作成と予測
model = LinearRegression()
model.fit(Years.reshape(-1, 1), RemainingGovtBond)
predicted_balance_2028 = model.predict([[2028]])

print("2028年の国債残高の予測値:", predicted_balance_2028[0])

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

Years = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
MeimokuGDP = np.array([512.5, 523.4, 540.7, 544.8, 555.7, 556.6, 556.8, 537.6, 550.7, 561.2])

# 線形回帰モデルの作成と予測
model = LinearRegression()
model.fit(Years.reshape(-1, 1), MeimokuGDP)
predicted_gdp_2028 = model.predict([[2028]])

print("2028年の名目GDPの予測値:", predicted_gdp_2028[0])

# 2028年の国債利払の予測値を計算
predicttedGovBondPayment2028 = predicted_gdp_2028[0] * GovYeild / 100
print("2028年の国債利払の予測値:", predicttedGovBondPayment2028)

# 2028年の国債利払の予測値を名目GDPに占める割合を計算
predicttedGovBondPaymentRatio2028 = 100 * predicttedGovBondPayment2028 / predicted_gdp_2028[0]
print("2028年の国債利払の予測値を名目GDPに占める割合:", predicttedGovBondPaymentRatio2028)

# 2028年の国債残高÷名目GDPの割合の予測値を計算
print("2028年の国債残高÷名目GDPの予測値:", 100 * predicted_balance_2028[0] / predicted_gdp_2028[0])
