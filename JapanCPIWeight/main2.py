import matplotlib.pyplot as plt

#データの取得年
Years = [2020, 2021, 2022]
#総合したデータ
Total = [100000, 100000, 100000]

#各品目の割合のデータ
Food = [2661, 2628, 2614]
Redidence = [2199, 2227, 2166]
Utility = [704, 694, 764]
Furniture = [413, 394, 389]
Clothing = [325, 317, 319]
Medical = [490, 488, 484]
TransportationAndCommunication = [1451, 1439, 1447]
Education = [311, 362, 337]
Entertainment = [851, 856, 881]
Other = [595, 594, 600]

# 折れ線グラフのプロット
plt.plot(Years, Food, label='Food')
plt.plot(Years, Redidence, label='Redidence')
plt.plot(Years, Utility, label='Utility')
plt.plot(Years, Furniture, label='Furniture')
plt.plot(Years, Clothing, label='Clothing')
plt.plot(Years, Medical, label='Medical')
plt.plot(Years, TransportationAndCommunication, label='Transportation and Communication')
plt.plot(Years, Education, label='Education')
plt.plot(Years, Entertainment, label='Entertainment')
plt.plot(Years, Other, label='Other')

# グラフの設定
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Line Graph')
plt.legend()

# グラフの表示
plt.show()