import datetime
from dateutil.relativedelta import relativedelta
import requests
import os

# 基準日を設定
current_week = datetime.datetime.strptime('20240524', '%Y%m%d')

# 5週間前までの日付を生成
dates = [current_week - relativedelta(weeks=i) for i in range(5)]

# ダウンロードしたファイルを保存するディレクトリ
save_directory = "./data/"
os.makedirs(save_directory, exist_ok=True)

# ダウンロードと保存処理
for date in dates:
    file_name = f"{date.strftime('%Y%m%d')}_indexfut_oi_by_tp.xlsx"
    url = f"https://www.jpx.co.jp/markets/derivatives/open-interest/mklp770000007ovn-att/{file_name}"
    
    # ファイルの存在を確認
    response = requests.head(url)  # HEADリクエストでファイルの存在を確認
    if response.status_code == 200:
        # ファイルのダウンロード
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーがあれば例外を投げる

        # ファイルを保存
        save_path = os.path.join(save_directory, file_name)
        with open(save_path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded {file_name} to {save_path}")
    else:
        print(f"File not found: {file_name}")
