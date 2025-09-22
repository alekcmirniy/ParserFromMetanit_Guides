import requests
from bs4 import BeautifulSoup
import os
import re

def safe_name(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|#]', "_", name).strip()

metanit_url = 'https://metanit.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(metanit_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    section_menu = soup.find('div', {"class": "navmenu"})

    for section_url in section_menu.find_all('a', href=True):
        section_name = safe_name(section_url.text)

        if not os.path.exists(section_name):
            os.mkdir(section_name)
        os.chdir(section_name)

        url = section_url['href']
        if url.startswith("//"):
            url = "https:" + url
        elif url.startswith("/"):
            url = metanit_url.rstrip("/") + url

        section_res = requests.get(url, headers=headers)
        if section_res.status_code == 200:
            section_soup = BeautifulSoup(section_res.text, 'html.parser')
            theme_menu = section_soup.find('div', {"class": "navmenu"})
            if theme_menu:
                for theme_url in theme_menu.find_all('a', href=True):
                    theme_name = safe_name(theme_url.text) + ".txt"

                    with open(theme_name, "w", encoding="utf-8") as theme_file:
                        url = theme_url['href']
                        if url.startswith("//"):
                            url = "https:" + url
                        elif url.startswith("/"):
                            url = metanit_url.rstrip("/") + url

                        theme_res = requests.get(url, headers=headers)
                        if theme_res.status_code == 200:
                            theme_soup = BeautifulSoup(theme_res.text, 'html.parser')
                            for e in theme_soup.find_all('ol', {"class": "subsubcontent"}):
                                for child in e.children:
                                    if hasattr(child, "text") and child.text.strip():
                                        theme_file.write(child.text.strip() + '\n')

        os.chdir("..")

    print("Данные записаны в файл")
else:
    print(f"Ошибка запроса: {response.status_code}")