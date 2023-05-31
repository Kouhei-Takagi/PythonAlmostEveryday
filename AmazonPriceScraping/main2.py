from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chromeドライバーのパスを指定してサービスを作成
webdriver_service = Service('/path/to/chromedriver')

# Chromeオプションを設定
chrome_options = Options()
chrome_options.add_argument('--headless')  # ヘッドレスモードで実行（画面表示なし）

# Chromeドライバーを起動
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = "https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91Dell-SE2722H-3%E5%B9%B4%E9%96%93%E4%BA%A4%E6%8F%9B%E4%BF%9D%E8%A8%BC-D-Sub15%E3%83%94%E3%83%B3-FreeSync%E2%84%A2/dp/B095745ZC8/"

# 指定したURLを開く
driver.get(url)

# ウェブページの要素を取得して価格情報を抽出
price_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
price = price_element.text

print(price)

# ブラウザを終了する
driver.quit()
