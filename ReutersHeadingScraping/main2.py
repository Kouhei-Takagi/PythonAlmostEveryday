import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.html_content = None

    def fetch_html_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.html_content = response.text
        else:
            print("リクエストが失敗しました。ステータスコード: ", response.status_code)

    def scrape_heading_element_text(self):
        if self.html_content is None:
            self.fetch_html_content()

        soup = BeautifulSoup(self.html_content, "html.parser")
        heading_element = soup.find('a', {"data-testid": 'Heading'})
        if heading_element:
            text = heading_element.get_text()
            return text
        else:
            return None

# 使用例
url = "https://www.reuters.com/"
scraper = WebScraper(url)
text = scraper.scrape_heading_element_text()
if text:
    print(text)
else:
    print("要素が見つかりませんでした。")
