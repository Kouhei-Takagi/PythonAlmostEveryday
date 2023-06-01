import pandas as pd
import matplotlib.pyplot as plt

# エクセルファイルを読み込む
df = pd.read_excel('./JapanCPIWeight/rensa-wt_2020.xlsx', header=3, skiprows=1, usecols="H:P747")
print(df.head())
print(df)
print(df.tail())

# 2020年のデータのみを抽出
df_2020 = df[['類・品目', '2020年']]

# 欠損値を削除
df_2020 = df_2020.dropna()

# グラフのプロット
plt.pie(df_2020['2020年'], labels=df_2020['類・品目'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('2020年の円グラフ')
plt.show()