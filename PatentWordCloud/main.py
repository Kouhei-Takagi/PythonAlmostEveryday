import requests

endpoint = "https://developer.uspto.gov/ibd-api/v1/application/publications"
params = {
    "searchText": "Machine Learning",
    "publicationFromDate": "2022-12-01",
    "PublicationToDate": "2023-01-01"
}

# APIリクエストを送信
response = requests.get(endpoint, params=params, verify=False)

claims = []

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのJSONデータを取得
    data = response.json()
    # 結果が存在することを確認
    if 'results' in data:
        # レスポンスの処理
        for result in data['results']:
            # 'inventionTitle'が存在することを確認
            if 'inventionTitle' in result:
                inventionTitle = result['inventionTitle']
            # 'publicationDate'が存在することを確認
            if 'publicationDate' in result:
                publicationDate = result['publicationDate']
            # 'abstractText'が存在することを確認
            if 'abstractText' in result:
                abstractText = result['abstractText']
            # 'claims'が存在することを確認
            if 'claimText' in result:
                claims.append(result['claimText'])

else:
    print("エラーが発生しました。")

# 特許請求の範囲を取得
for sublist in claims:
    claim_texts = str(sublist[0])
print(claim_texts)

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    # 小文字化
    text = text.lower()

    # 句読点と特殊文字の削除
    text = re.sub(r"[^\w\s]", "", text)

    # ストップワードの除去
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word not in stop_words]

    # 前処理後のテキストを返す
    return " ".join(filtered_text)

# テキストの前処理
preprocessed_claims = [preprocess_text(claim) for claim in claim_texts]

# 前処理後のテキストを表示
preprocessed_text = " ".join(preprocessed_claims)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(text):
    # ワードクラウドの作成
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # ワードクラウドの表示
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# ワードクラウドの作成と表示
create_wordcloud(preprocessed_text)
