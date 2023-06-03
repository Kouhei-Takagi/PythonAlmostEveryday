import requests
from bs4 import BeautifulSoup

url = "https://www.mlit.go.jp/jidosha/recall_R4.html"  # スクレイピングするURL
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())  # HTMLの構造をインデントして表示

#data = soup.find('div', class_='section')
#print(data.prettify())

links = soup.find_all('a')

for link in links:
    text = link.text.strip()
    href = link.get('href')
    print(f"Company: {text}, URL: {href}")