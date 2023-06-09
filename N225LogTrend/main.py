import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt

# NIKKEI225のデータを取得
df = web.DataReader("NIKKEI225", 'fred', '1990-01-01', '2023-06-08')

# 対数変換を行う
df['LogReturn'] = np.log(df['NIKKEI225']).diff()

# プロット
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['LogReturn'], label='NIKKEI225 Log Returns')
plt.title('NIKKEI225 Log Returns')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.legend()
plt.grid(True)
plt.show()
