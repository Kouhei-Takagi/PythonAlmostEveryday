import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

url = "https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91Dell-SE2722H-3%E5%B9%B4%E9%96%93%E4%BA%A4%E6%8F%9B%E4%BF%9D%E8%A8%BC-D-Sub15%E3%83%94%E3%83%B3-FreeSync%E2%84%A2/dp/B095745ZC8/"
decoded_url = unquote(url)
response = requests.get(decoded_url)

# 応答が成功したかを確認します（ステータスコード200は成功を意味します）
if response.status_code == 200:
    html_content = response.text
else:
    print("リクエストが失敗しました。ステータスコード: ", response.status_code)

# BeautifulSoupを使用してHTMLを解析します
soup = BeautifulSoup(html_content, "html.parser")
price_element = soup.find('span', class_ = 'a-price-whole')
text = price_element.get_text()

print(text)