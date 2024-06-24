import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# ページからHTMLを取得
base_url = 'https://www.jpx.co.jp'
url = base_url + '/markets/derivatives/open-interest/archives-00.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# リンクのリストを抽出
links = soup.find_all('a', href=True)

# 現在の日付から5週間前までのリンクのみを抽出
filtered_links = []
today = datetime.today()
five_weeks_ago = today - timedelta(weeks=6)

for link in links:
    href = link['href']
    if "_indexfut_oi_by_tp.xlsx" in href:
        date_str = href.split('/')[-1][:8]  # URLから日付部分を抽出
        try:
            link_date = datetime.strptime(date_str, '%Y%m%d')
            if five_weeks_ago <= link_date <= today:
                full_url = base_url + href  # 完全なURLを作成
                filtered_links.append(full_url)
        except ValueError:
            continue  # 日付形式が異なる場合はスキップ

# 結果を表示
for link in filtered_links:
    print(link)

# ダウンロードしたファイルを保存するディレクトリ
save_directory = "./DATA/"
os.makedirs(save_directory, exist_ok=True)

for url in filtered_links:
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