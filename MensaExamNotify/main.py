import requests
from bs4 import BeautifulSoup
import os
import json

# 対象のURL
url = 'https://mensa.jp/exam/'
# 前回のテキスト
filename = './MensaExamNotify/prev_text.txt'

# ページの情報を取得
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 関東地方のテキストを取得
kanto_region_text = soup.find('h3', text='関東地方').find_next('p').get_text(strip=True)

# 前回のテキストと比較
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        prev_text = file.read().strip()
else:
    prev_text = ""

# 前回のテキストと異なる場合はLINEに通知
if kanto_region_text != prev_text:
    print("NO")
    LINE_API_URL = 'https://notify-api.line.me/api/notify'
    LINE_API_TOKEN = '***'

    headers = {
        'Authorization': 'Bearer ' + LINE_API_TOKEN,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'message': "Mensa Exam!+ {}".format(url)
    }

    response = requests.post(LINE_API_URL, headers=headers, data=data)
    if response.status_code != 200:
        print('Failed to send message')

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(kanto_region_text)
else:
    print("YES")
