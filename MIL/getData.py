import requests
import os
import datetime
from dateutil.relativedelta import relativedelta

# 基準日を設定
currentWeek = datetime.datetime.strptime('20240524', '%Y%m%d')

# 5週間前までの日付を生成
dates = [currentWeek - relativedelta(weeks=i) for i in range(5)]

# URLのリストを生成
urls = [
    f"https://www.jpx.co.jp/markets/derivatives/open-interest/mklp770000007ovn-att/{date.strftime('%Y%m%d')}_indexfut_oi_by_tp.xlsx"
    for date in dates
]

# ダウンロードしたファイルを保存するディレクトリ
save_directory = "./DATA/"
os.makedirs(save_directory, exist_ok=True)

for url in urls:
    # URLからファイル名を抽出
    filename = url.split("/")[-1]
    save_path = os.path.join(save_directory, filename)
    
    # ファイルのダウンロード
    response = requests.get(url)
    response.raise_for_status()  # HTTPエラーがあれば例外を投げる
    
    # ファイルを保存
    with open(save_path, 'wb') as f:
        f.write(response.content)

    print(f"Downloaded {filename} to {save_path}")