import requests

endpoint = "https://developer.uspto.gov/ibd-api/v1/application/publications"
params = {
    "searchText": "Machine Learning",
    "publicationFromDate": "2022-12-29",
    "PublicationToDate": "2023-01-01"
}

# APIリクエストを送信
response = requests.get(endpoint, params=params, verify=False)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのJSONデータを取得
    data = response.json()
    print(data)
    # 結果が存在することを確認
    if 'results' in data:
        # レスポンスの処理
        for result in data['results']:
            # 'inventionTitle'が存在することを確認
            if 'inventionTitle' in result:
                inventionTitle = result['inventionTitle']
                print(f"Title: {inventionTitle}")
            # 'publicationDate'が存在することを確認
            if 'publicationDate' in result:
                publicationDate = result['publicationDate']
                print(f"PublicationDate: {publicationDate}")
            # 'abstractText'が存在することを確認
            if 'abstractText' in result:
                abstractText = result['abstractText']
                print(f"Abstract: {abstractText}")
            # 'claims'が存在することを確認
            if 'claimText' in result:
                claims = result['claimText']
                print(f"Claim: {claims}")
else:
    print("エラーが発生しました。")
