import pandas as pd
import matplotlib.pyplot as plt

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

# データフレームの最初の数行を確認とカラムの確認
all_data.head(), all_data.columns

# データフレームの先頭と末尾を組み合わせて全体のデータ構造を確認
pd.concat([all_data.head(), all_data.tail()])

# データフレームのカラム名の整理と必要な情報の抽出
# ここでは 'Unnamed: 6', 'Unnamed: 15', 'Unnamed: 16' に証券会社名が含まれている可能性が高いため、これらを対象とします

# SBI証券、楽天証券、松井証券に関連する行をフィルタリング
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

# 適用して新しいカラムを作成
selected_data[['Broker_Final', 'Sell_Final', 'Buy_Final']] = selected_data.apply(extract_correct_data, axis=1)

# 不要なカラムを削除
selected_data = selected_data[['Date', 'Broker_Final', 'Sell_Final', 'Buy_Final']].dropna()

selected_data.head(), selected_data.groupby(['Date', 'Broker_Final']).sum()

# データ型の修正
selected_data['Sell_Final'] = pd.to_numeric(selected_data['Sell_Final'], errors='coerce')
selected_data['Buy_Final'] = pd.to_numeric(selected_img['']Final'], errors='coerce')

# データの集計
grouped_data = selected_data.groupby(['Date', 'Broker_Final'])['Sell_Final', 'Buy_Final'].sum().reset_index()

# グラフの作成
plt.figure(figsize=(14, 7))
for broker in grouped_data['Broker_Final'].unique():
    broker_data = grouped_data[grouped_data['Broker_Final'] == broker]
    plt.plot(broker_data['Date'], broker_data['Buy_Final'], marker='o', label=f'{broker} 買い建玉')
    plt.plot(broker_data['Date'], broker_data['Sell_Final'], marker='x', linestyle='--', label=f'{broker} 売り建玉')

plt.title('SBI証券、楽天証券、松井証券の週ごとの建玉変化')
plt.xlabel('日付')
plt.ylabel('建玉量')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
