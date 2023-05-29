import requests
from bs4 import BeautifulSoup

url = "https://www.reuters.com/"
response = requests.get(url)

# 応答が成功したかを確認します（ステータスコード200は成功を意味します）
if response.status_code == 200:
    html_content = response.text
else:
    print("リクエストが失敗しました。ステータスコード: ", response.status_code)

# BeautifulSoupを使用してHTMLを解析します
soup = BeautifulSoup(html_content, "html.parser")
heading_element = soup.find('a', {"data-testid":'Heading'})
text = heading_element.get_text()

print(text)
