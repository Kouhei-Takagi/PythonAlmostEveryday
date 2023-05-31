from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class AmazonPriceScraper:
    def __init__(self, driver_path):
        # Chromeドライバーのパスを指定してサービスを作成
        self.webdriver_service = Service(driver_path)

        # Chromeオプションを設定
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # ヘッドレスモードで実行（画面表示なし）

        # Chromeドライバーを起動
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=chrome_options)

    def get_price(self, url):
        # 指定したURLを開く
        self.driver.get(url)

        # ウェブページの要素を取得して価格情報を抽出
        price_element = self.driver.find_element(By.CLASS_NAME, 'a-price-whole')
        price = price_element.text

        return price

    def quit(self):
        # ブラウザを終了する
        self.driver.quit()

# 使用例
driver_path = '/path/to/chromedriver'  # Chromeドライバーのパスを指定
url = "https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91Dell-SE2722H-3%E5%B9%B4%E9%96%93%E4%BA%A4%E6%8F%9B%E4%BF%9D%E8%A8%BC-D-Sub15%E3%83%94%E3%83%B3-FreeSync%E2%84%A2/dp/B095745ZC8/"

scraper = AmazonPriceScraper(driver_path)
price = scraper.get_price(url)
print(price)
scraper.quit()
