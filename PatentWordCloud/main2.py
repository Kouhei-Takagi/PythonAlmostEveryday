import requests
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class PatentAnalyzer:
    def __init__(self):
        self.endpoint = "https://developer.uspto.gov/ibd-api/v1/application/publications"
        self.params = {
            "searchText": "Machine Learning",  # 検索キーワード
            "publicationFromDate": "2022-01-01",  # 公開日の範囲（開始日）
            "PublicationToDate": "2023-01-01"  # 公開日の範囲（終了日）
        }
        self.claims = []

    def fetch_patent_data(self):
        response = requests.get(self.endpoint, params=self.params, verify=False)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                for result in data['results']:
                    if 'inventionTitle' in result:
                        inventionTitle = result['inventionTitle']  # 発明のタイトル
                    if 'publicationDate' in result:
                        publicationDate = result['publicationDate']  # 公開日
                    if 'abstractText' in result:
                        abstractText = result['abstractText']  # アブストラクトのテキスト
                    if 'claimText' in result and result['claimText'] is not None:
                        self.claims.append(result['claimText'])  # 特許請求のテキスト
            else:
                print("検索結果が見つかりませんでした。")
        else:
            print("エラーが発生しました。")

    def preprocess_text(self, text):
        text = text.lower()  # 小文字化
        text = re.sub(r"[^\w\s]", "", text)  # 句読点と特殊文字の削除
        stop_words = set(stopwords.words("english"))  # ストップワードのリスト
        tokens = word_tokenize(text)  # 単語にトークン化
        filtered_text = [word for word in tokens if word not in stop_words]  # ストップワードの除去
        return " ".join(filtered_text)  # 前処理後のテキストを返す

    def preprocess_claims(self):
        claim_texts = ""
        for sublist in self.claims:
            if sublist is not None and len(sublist) > 0:
                claim_texts += str(sublist[0])  # 特許請求のテキストを結合
        preprocessed_claims = [self.preprocess_text(claim) for claim in claim_texts]  # 前処理を適用
        self.preprocessed_text = " ".join(preprocessed_claims)  # 前処理後のテキストを結合

    def create_wordcloud(self):
        wordcloud = WordCloud(width=800, height=400).generate(self.preprocessed_text)  # ワードクラウドの作成
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def run(self):
        self.fetch_patent_data()  # 特許データを取得
        self.preprocess_claims()  # 特許請求を前処理
        self.create_wordcloud()  # ワードクラウドを作成して表示

# PatentAnalyzerのインスタンスを作成して実行する
analyzer = PatentAnalyzer()
analyzer.run()
