# ParserFromMetanit_Guides

Кратко: Парсер на Python для сбора списка тем/уроков с metanit.com и сохранения их в папки и `.txt` файлы.

## ✨ Возможности
- Получение списка разделов и тем с metanit.com
- Создание папок под разделы и `.txt` файлов с заголовками уроков
- Очистка имён файлов/папок от запрещённых символов

## 🚀 Быстрый старт
```bash
git clone https://github.com/alekcmirniy/ParserFromMetanit_Guides.git
```
```bash
cd ParserFromMetanit_Guides
```
```bash
pip install -r requirements.txt
python index.py
```

## 🛠 Технологии
- Python 3, requests, BeautifulSoup4, os, re

## 📁 Структура
```text
ParserFromMetanit_Guides/
├── index.py
├── requirements.txt
└── ...outputs/    # созданные папки, в них .txt
```

## 📄 Лицензия
Смотрите файл LICENSE в репозитории.

## 👨‍💻 Автор
Alexey Miroshnichenko (alekcmirniy)