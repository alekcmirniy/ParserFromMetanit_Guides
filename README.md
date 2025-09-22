# ParserFromMetanit_Guides

Скрипт на Python для парсинга учебных тем с сайта [metanit.com](https://metanit.com/).  
Парсер автоматически проходит по разделам сайта, создаёт для каждого раздела отдельную папку,  
а для каждой темы сохраняет список названий уроков в `.txt` файлы.

## 🚀 Возможности
- Получение списка разделов с главной страницы **metanit.com**
- Создание папок под каждый раздел (например: `Python`, `Kotlin`, `Java`)
- Создание текстовых файлов под каждую тему внутри раздела
- Очистка от запрещённых символов в названиях файлов/папок
- Сохранение заголовков уроков в структурированном виде

## 🛠️ Используемые технологии
- [Python 3](https://www.python.org/)  
- [requests](https://pypi.org/project/requests/) — для HTTP-запросов  
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) — для парсинга HTML  
- [os](https://docs.python.org/3/library/os.html) — для работы с файловой системой  
- [re](https://docs.python.org/3/library/re.html) — для очистки имён файлов/папок  

ВНИМАНИЕ! Ввиду невозможности добавления спец.символов (#) в названия директорий Windows, некоторые символы были заменены на доступные (_)

## 📦 Установка
Клонируй репозиторий и установи зависимости:

git clone https://github.com/alekcmirniy/ParserFromMetanit_Guides.git

cd ParserFromMetanit_Guides

pip install -r requirements.txt

## Запуск

python index.py
