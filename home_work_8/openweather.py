
"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import json
import requests
import sqlite3
import datetime


def read_app_id() -> str:
    file_app_id = open('app.id', "r", encoding='utf-8-sig')
    key = file_app_id.readline()
    file_app_id.close()
    return key


def get_request(url: str, payload: dict) -> dict:
    response = requests.get(url, params=payload)
    print(response.url)
    return response.json()


def needed_city(json_city_file: str, count: int) -> list:
    city_list = []
    with open(json_city_file, "r", encoding='utf-8') as read_file:
        city_data = json.load(read_file)
        while len(city_list) < count:
            my_city = input("Введите название города ")
            for city in city_data:
                if city['name'] == my_city:
                    city_list.append(city)
    return city_list


def country_list(json_city_file: str) -> list:
    with open(json_city_file, "r", encoding='utf-8') as read_file:
        city_data = json.load(read_file)
    countries = sorted(set(city['country'] for city in city_data))
    return countries


print("Список стран из файла:\n", country_list("city.list.json"))
count = int(input("Сколько нужно получить городов? "))
city_list = needed_city("city.list.json", count)
print(city_list)
print(len(city_list))
app_id = read_app_id()
# if len(city_list) == 1:
#     url = 'http://api.openweathermap.org/data/2.5/weather'
#     payload = {'id': city_list[0]['id'], 'units': 'metric', 'appid': app_id}
#     json_weather_data = get_request(url, payload)
#     print(json_weather_data)
#     print("id_города {0}, Город {1}, Дата {2}, Температура {3}, id_погоды {4}".format
#               (json_weather_data['id'], json_weather_data['name'],
#                datetime.datetime.fromtimestamp(json_weather_data['dt']), json_weather_data['main']['temp'],
#                json_weather_data['weather'][0]['id']))
# else:
#     url = 'http://api.openweathermap.org/data/2.5/group'
#     city_ids = []
#     for city in city_list:
#         city_ids.append(str(city['id']))
#     str_ids = ','.join(city_ids)
#     payload = {'id': str_ids, 'units': 'metric', 'appid': app_id}
#     json_weather_data = get_request(url, payload)
#     print(json_weather_data)
#     for city in json_weather_data['list']:
#         print("id_города {0}, Город {1}, Дата {2}, Температура {3}, id_погоды {4}".format
#               (city['id'], city['name'], datetime.datetime.fromtimestamp(city['dt']),
#                city['main']['temp'], city['weather'][0]['id']))
def get_json_weather_file(city_list: list):
    if len(city_list) == 1:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        payload = {'id': city_list[0]['id'], 'units': 'metric', 'appid': app_id}
        json_weather_data = get_request(url, payload)
        return json_weather_data
    else:
        url = 'http://api.openweathermap.org/data/2.5/group'
        city_ids = []
        for city in city_list:
            city_ids.append(str(city['id']))
        str_ids = ','.join(city_ids)
        payload = {'id': str_ids, 'units': 'metric', 'appid': app_id}
        json_weather_data = get_request(url, payload)
        return json_weather_data



def get_weather_db(db_filename: str):
    with sqlite3.connect(db_filename) as conn:
        conn.execute("""
            create table project (
                id_города           text primary key,
                Город               varchar(255),
                Дата                date,
                Температура         integer,
                id_погоды           integer
            );
            """)
    print("База данных создана")


def insert_weather_db(db_filename: str, json_data_weather: dict):
    conn = sqlite3.connect(db_filename)
    conn.close()
    with sqlite3.connect(db_filename) as conn:
            conn.execute("""
                    insert into project (id_города, Город, Дата, Температура, id_погоды) VALUES (?,?,?,?,?)""",  (
                    json_data_weather['id'],
                    json_data_weather['name'],
                    datetime.datetime.fromtimestamp(json_data_weather['dt']),
                    json_data_weather['main']['temp'],
                    json_data_weather['weather'][0]['id']
            )
                         )


def print_weather_db(db_filename: str):
    with sqlite3.connect(db_filename) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from project")
        for row in cur.fetchall():
            print(row)
            city_id, city_name, date, temperature, weather_id = row
            print(city_id, city_name, date, temperature, weather_id)


def update_weather_db(db_filename: str, json_data_weather: dict):
        with sqlite3.connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute("update project set Температура=:Температура, Дата=:Дата, id_погоды=:id_погоды"
                        " where id_города=:id_города",
                        {'Температура': json_data_weather['main']['temp'],
                         'Дата': datetime.datetime.fromtimestamp(json_data_weather['dt']),
                         'id_погоды':  json_data_weather['weather'][0]['id'],
                         'id_города': json_data_weather['id']})


json_weather_data = get_json_weather_file(city_list)
if len(city_list) == 1:
    print("id_города {0}, Город {1}, Дата {2}, Температура {3}, id_погоды {4}".format
          (json_weather_data['id'], json_weather_data['name'],
           datetime.datetime.fromtimestamp(json_weather_data['dt']), json_weather_data['main']['temp'],
           json_weather_data['weather'][0]['id']))
else:
    for city in json_weather_data['list']:
        print("id_города {0}, Город {1}, Дата {2}, Температура {3}, id_погоды {4}".format
                (city['id'], city['name'], datetime.datetime.fromtimestamp(city['dt']),
                 city['main']['temp'], city['weather'][0]['id']))


def work_with_weather_db(db_filename: str):
    try:
        get_weather_db(db_filename)
    except sqlite3.OperationalError:
        print("База данных уже есть")
        pass
    if len(city_list) == 1:
        try:
            insert_weather_db(db_filename, json_weather_data)
        except sqlite3.IntegrityError:
            update_weather_db(db_filename, json_weather_data)
    else:
        for city in json_weather_data['list']:
            try:
                insert_weather_db(db_filename, city)
            except sqlite3.IntegrityError:
                update_weather_db(db_filename, city)
    print_weather_db(db_filename)


work_with_weather_db('weather.db')


def json_files_from_country(json_city_file: str, my_country: str):
    country_city_list = []
    with open(json_city_file, "r", encoding='utf-8') as read_file:
        city_data = json.load(read_file)
        for city in city_data:
            if city['country'] == my_country:
                country_city_list.append(city)
    return country_city_list


is_continue = input("Хотите получать файлы по стране? y/n ")
if is_continue == 'Y' or is_continue == 'y':
    my_country = input("Города из какой страны вам нужны? ")
    if my_country not in country_list("city.list.json"):
        print("Такой страны нет в списке")
    else:
        new_city_list = json_files_from_country("city.list.json", my_country)
        for city in new_city_list:
            print(city)
            json_weather_data = get_json_weather_file([city])
            work_with_weather_db("weather.db")
