import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

base_url = "https://求人ボックス.com/Pythonエンジニア-未経験の仕事-東京都"
start_page = 2
end_page = 5

conn = sqlite3.connect('./KyujinBoxScraping/kyujinbox.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS scraped_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             result_name TEXT,
             date TEXT)''')

for page_number in range(start_page, end_page+1):
    url = base_url + "?pg=" + str(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # スクレイピングの処理をここに記述する
    results = soup.find_all('span', class_='p-result_name')
    for result in results:
        #print(result.text)
        c.execute("INSERT INTO scraped_data (result_name, date) VALUES (?, ?)", (result.text, datetime.date.today()))
        conn.commit()

conn.close()
