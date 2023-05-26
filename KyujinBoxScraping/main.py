import requests
from bs4 import BeautifulSoup

BASE_URL = "https://求人ボックス.com/Pythonエンジニア-未経験の仕事-東京都"
page_number = 2

URL = BASE_URL + "?page=" + str(page_number)

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

title = soup.find('title').text
print(title)

'''
elements = soup.select('')
for element in elements:
    print(element.text)
'''

results = soup.find_all('span', class_='p-result_name')

for result in results:
    print(result.text)