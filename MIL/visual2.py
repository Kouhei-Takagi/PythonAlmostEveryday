import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 正しいファイルパス
file_paths = [
    './data/20240426_indexfut_oi_by_tp.xlsx',
    './data/20240502_indexfut_oi_by_tp.xlsx',
    './data/20240510_indexfut_oi_by_tp.xlsx',
    './data/20240517_indexfut_oi_by_tp.xlsx',
    './data/20240524_indexfut_oi_by_tp.xlsx'
]

# データを読み込み、各ファイルのデータに日付を付加
data_frames = []
for file_path in file_paths:
    df = pd.read_excel(file_path)
    # Excelファイルの名前から日付を抽出
    date = file_path.split('/')[-1].split('_')[0]
    df['Date'] = pd.to_datetime(date, format='%Y%m%d')
    data_frames.append(df)

# 全てのデータフレームを結合
all_data = pd.concat(data_frames, ignore_index=True)

# DataFrame内の全てのテキストカラムで全角「ＳＢＩ」を半角「SBI」に置換
for column in all_data.select_dtypes(include=['object']).columns:
    all_data[column] = all_data[column].str.replace('ＳＢＩ証券', 'SBI証券', regex=False)

# データフレームのカラム名の整理と必要な情報の抽出
broker_filter = all_data['Unnamed: 6'].isin(['SBI証券', '楽天証券', '松井証券']) | \
                all_data['Unnamed: 15'].isin(['SBI証券', '楽天証券', '松井証券']) | \
                all_data['Unnamed: 16'].isin(['SBI証券', '楽天証券', '松井証券'])

# 必要なカラムのみを選択
selected_data = all_data[broker_filter][['Date', 'Unnamed: 6', 'Unnamed: 5', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 14']]

# カラム名をわかりやすくリネーム
selected_data.columns = ['Date', 'Broker', 'Sell_Position', 'Buy_Position', 'Broker_2', 'Position_2']

# 各行で適切なブローカーとポジションのデータを抽出し、統合する
def extract_correct_data(row):
    if row['Broker'] in ['SBI証券', '楽天証券', '松井証券']:
        return pd.Series([row['Broker'], row['Sell_Position'], row['Buy_Position']])
    elif row['Broker_2'] in ['SBI証券', '楽天証券', '松井証券']:
        return pd.Series([row['Broker_2'], row['Position_2'], row['Buy_Position']])
    else:
        return pd.Series([None, None, None])

selected_data[['Broker_Final', 'Sell_Final', 'Buy_Final']] = selected_data.apply(extract_correct_data, axis=1)

# 不要なカラムを削除
selected_data = selected_data[['Date', 'Broker_Final', 'Sell_Final', 'Buy_Final']].dropna()

# データ型の修正
selected_data['Sell_Final'] = pd.to_numeric(selected_data['Sell_Final'], errors='coerce')
selected_data['Buy_Final'] = pd.to_numeric(selected_data['Buy_Final'], errors='coerce')

# データの集計
grouped_data = selected_data.groupby(['Date', 'Broker_Final'])[['Sell_Final', 'Buy_Final']].sum().reset_index()

# グラフの作成
plt.figure(figsize=(14, 7))
for broker in grouped_data['Broker_Final'].unique():
    broker_data = grouped_data[grouped_data['Broker_Final'] == broker]
    plt.plot(broker_data['Date'], broker_data['Buy_Final'], marker='o', label=f'{broker} 買い建玉')
    plt.plot(broker_data['Date'], broker_data['Sell_Final'], marker='x', linestyle='--', label=f'{broker} 売り建玉')

# Matplotlibのフォントをヒラギノ角ゴ ProN W3に設定
mpl.rcParams['font.family'] = 'Hiragino Sans'
mpl.rcParams['font.sans-serif'] = ['Hiragino Sans W3']

plt.title('SBI証券、楽天証券、松井証券の週ごとの建玉変化')
plt.xlabel('日付')
plt.ylabel('建玉量')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()