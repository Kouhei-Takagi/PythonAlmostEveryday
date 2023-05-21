import requests

endpoint = "https://developer.uspto.gov/ibd-api/v1/weeklyarchivedata/searchWeeklyArchiveData"
params = {
    "fromDate": "01-01-2023",
    "toDate": "05-21-2023"
}

# APIリクエストを送信
response = requests.get(endpoint, params=params, verify=False)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのJSONデータを取得
    data = response.json()
    #print(data)
    # レスポンスの処理
    for result in data:
        archiveFileName = result["archiveFileName"]
        fileSize = result["fileSize"]
        fromDate = result["fromDate"]
        toDate = result["toDate"]
        createDateTime = result["createDateTime"]
        archiveDownloadURL = result["archiveDownloadURL"]
        print(archiveFileName)
        print(fileSize)
        print(fromDate)
        print(toDate)
        print(createDateTime)
        print(archiveDownloadURL)
        print("---")
else:
    print("エラーが発生しました。")