import requests
from bs4 import BeautifulSoup

file = open("results.txt", "a")
file.truncate(0)
metanit_url = 'https://metanit.com/web/javascript/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(metanit_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for e in soup.find_all('ol', {"class": "subsubcontent"}):
        for child in e.children:
            if len(child.text.strip()) != 0:
                file.write(child.text + '\n')
    print("Данные записаны в файл");
else:
    print(f"Ошибка запроса: {response.status_code}")