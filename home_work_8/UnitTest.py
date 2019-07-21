import os
import openweather
import unittest

name_of_db = 'test_weather.db'
path_to_weather_db = os.path.join(os.getcwd(), name_of_db)
json_example_for_single_city = {
    "coord": {"lon": 82.93, "lat": 55.04},
    "weather": [
        {"id": 800, "main": "Clear",
         "description": "clear sky",
         "icon": "01n"}],
    "base": "stations",
    "main": {"temp": 19, "pressure": 1013,
             "humidity": 63,
             "temp_min": 19,
             "temp_max": 19},
    "visibility": 10000,
    "wind": {"speed": 2, "deg": 20},
    "clouds": {"all": 0}, "dt": 1563034038,
    "sys": {"type": 1, "id": 8958,
            "message": 0.0071,
            "country": "RU",
            "sunrise": 1562969137,
            "sunset": 1563030112},
    "timezone": 25200, "id": 1496747,
    "name": "Novosibirsk", "cod": 200}
country = 'RU'
city = ['Moscow']
cities = ['Moscow', 'Ufa']
if os.path.exists(path_to_weather_db):
    os.remove(path_to_weather_db)
weather_db = openweather.WeatherDb(name_of_db)
weather_db.make_db()
weather_finder = openweather.FindWeather()


class TestWeatherDb(unittest.TestCase):

    def test_make_db(self):
        name_db_for_test = 'make_db_test.db'
        if os.path.exists(name_db_for_test):
            os.remove(name_db_for_test)
        weather_db_for_make_db = openweather.WeatherDb(name_db_for_test)
        self.assertTrue(weather_db_for_make_db.make_db())
        os.remove(name_db_for_test)

    def test_make_db_when_db_exist(self):
        name_of_db_for_make_db = 'test_make_db_when_db_exist.db'
        db_for_make_db_test = openweather.WeatherDb(name_of_db_for_make_db)
        db_for_make_db_test.make_db()
        self.assertFalse(db_for_make_db_test.make_db())
        os.remove(name_of_db_for_make_db)

    def test_insert_data(self):
        self.assertTrue(weather_db.insert_data(json_example_for_single_city))

    def test_update_data(self):
        weather_db.cur.execute("""SELECT * FROM project""")
        old_time = weather_db.cur.fetchall()[0][2]
        json_example_for_single_city['dt'] = 7777
        weather_db.update_data(json_example_for_single_city)
        weather_db.cur.execute("""SELECT * FROM project""")
        new_time = weather_db.cur.fetchall()[0][2]
        self.assertTrue(old_time != new_time)

    def test_str_weather_db(self):
        self.assertTrue(len(weather_db.__str__()) != 0)

    def test_close_db(self):
        name_for_test_close_db = 'test_for_close_db.db'
        weather_db_for_test_close = openweather.WeatherDb(
            name_for_test_close_db)
        self.assertTrue(weather_db_for_test_close.close_db())
        os.remove(name_for_test_close_db)

    def test_make_list_of_countries(self):
        self.assertTrue(len(weather_finder.make_list_of_countries()) > 0)

    def test_make_response_json(self):
        self.assertTrue(
            weather_finder.make_response_json(country, city)['name'] ==
            cities[0])
        self.assertTrue(len(
            weather_finder.make_response_json(country, cities)['list'])
                        >= len(cities))
        with self.assertRaises(IndexError):
            weather_finder.make_response_json('No country', ['No city'])

    def test_make_response(self):
        make_response = openweather.make_response(weather_finder)
        self.assertTrue(type(make_response) is dict)

    def test_operation_with_weather_bd(self):
        name_for_test_operation = 'test_for_operation_db.db'
        weather_db_for_test_operation = openweather.WeatherDb(
            name_for_test_operation)
        weather_db_for_test_operation.make_db()
        weather_finder.make_response_json(country, city)
        openweather.operation_with_weather_bd(weather_db_for_test_operation,
                                              weather_finder)
        weather_db_for_test_operation.cur.execute("select * from project")
        sql_tab = weather_db_for_test_operation.cur.fetchall()
        self.assertTrue(len(sql_tab) == 1)
        weather_finder.make_response_json(country, city)
        openweather.operation_with_weather_bd(weather_db_for_test_operation,
                                              weather_finder)
        weather_db_for_test_operation.cur.execute("select * from project")
        sql_tab = weather_db_for_test_operation.cur.fetchall()
        self.assertTrue(len(sql_tab) == 1)
        weather_finder.make_response_json(country, cities)
        openweather.operation_with_weather_bd(weather_db_for_test_operation,
                                              weather_finder)
        weather_db_for_test_operation.cur.execute("select * from project")
        sql_tab = weather_db_for_test_operation.cur.fetchall()
        self.assertTrue(len(sql_tab) == 2)
        os.remove(name_for_test_operation)


if __name__ == '__main__':
    unittest.main()
