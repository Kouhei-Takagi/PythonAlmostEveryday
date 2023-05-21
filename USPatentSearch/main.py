import requests

# APIエンドポイントとパラメータ
endpoint = "https://api.patentsview.org/patents"
params = {
    "q": "inventor_last_name:jobs",  # 検索クエリ。ここでは"jobs"という発明者の特許を検索しています
    "f": "patent_number,patent_title,patent_date",  # 取得するフィールド
    "o": "patent_date desc",  # 結果のソート順
    "s": 0,  # 開始位置（最初の結果からのオフセット）
    "c": 10  # 取得する結果の数
}

# APIリクエストを送信
response = requests.get(endpoint, params=params)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのJSONデータを取得
    data = response.json()

    # レスポンスの処理
    for result in data["patents"]:
        patent_number = result["patent_number"]
        patent_title = result["patent_title"]
        patent_date = result["patent_date"]
        print(f"特許番号: {patent_number}")
        print(f"特許タイトル: {patent_title}")
        print(f"特許日付: {patent_date}")
        print("---")
else:
    print("エラーが発生しました。")

