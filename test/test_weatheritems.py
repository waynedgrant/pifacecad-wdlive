# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

import unittest
from clientraw import ClientRaw
from settings import Settings
from weatheritems import WeatherItemFactory
from weatheritems import WeatherItemType


class TestWeatherItems(unittest.TestCase):

    def __get_weather_item(self, weather_item_type):
        settings = Settings()
        while settings.get_weather_item_type() != weather_item_type:
            settings.next_weather_item_type()
        return WeatherItemFactory(ClientRaw(self.__gen_populated_client_raw_str()), settings).get_weather_item()

    def __gen_populated_client_raw_str(self):
        return\
            "- 11.2 12.3 180 25.4 97 1019.7 15.67 - - 1.23 - 20.4 45 - 35 - - - - " +\
            "- - - - - - - - - 23 59 - - - - - - - - - " +\
            "- - - - 23.2 30.5 - - - - 0 - - - - - - - - - " +\
            "- - - - - - - - - - - - -13.2 - - - - - - 4.2 " +\
            "- - - - - - - - - - - - - - - - - - - - " +\
            "- - - - - - - - - - - - 31.6 - - - - - - - " +\
            "- - - - - - - - - - - - - - - - - - - - " +\
            "- - - -1 1"

    def test_summary(self):
        weather_item = self.__get_weather_item(WeatherItemType.SUMMARY)
        self.assertEqual("25.4°C ➘ 97% ➚", weather_item.get_line1())
        self.assertEqual("1019.7 hPa ➙", weather_item.get_line2())

    def test_average_wind(self):
        weather_item = self.__get_weather_item(WeatherItemType.AVERAGE_WIND)
        self.assertEqual("Average Wind", weather_item.get_line1())
        self.assertEqual("12.9 mph S", weather_item.get_line2())

    def test_daily_rainfall(self):
        weather_item = self.__get_weather_item(WeatherItemType.DAILY_RAINFALL)
        self.assertEqual("Daily Rainfall", weather_item.get_line1())
        self.assertEqual("15.67 mm", weather_item.get_line2())

    def test_dew_point(self):
        weather_item = self.__get_weather_item(WeatherItemType.DEW_POINT)
        self.assertEqual("Dew Point", weather_item.get_line1())
        self.assertEqual("-13.2°C", weather_item.get_line2())

    def test_forecast(self):
        weather_item = self.__get_weather_item(WeatherItemType.FORECAST)
        self.assertEqual("Forecast", weather_item.get_line1())
        self.assertEqual("Windy Rain", weather_item.get_line2())

    def test_gust_speed(self):
        weather_item = self.__get_weather_item(WeatherItemType.GUST_SPEED)
        self.assertEqual("Gust Speed", weather_item.get_line1())
        self.assertEqual("14.2 mph", weather_item.get_line2())

    def test_heat_index(self):
        weather_item = self.__get_weather_item(WeatherItemType.HEAT_INDEX)
        self.assertEqual("Heat Index", weather_item.get_line1())
        self.assertEqual("31.6°C", weather_item.get_line2())

    def test_humidex(self):
        weather_item = self.__get_weather_item(WeatherItemType.HUMIDEX)
        self.assertEqual("Humidex", weather_item.get_line1())
        self.assertEqual("30.5°C", weather_item.get_line2())

    def test_humidity(self):
        weather_item = self.__get_weather_item(WeatherItemType.HUMIDITY)
        self.assertEqual("Humidity", weather_item.get_line1())
        self.assertEqual("97% ➚", weather_item.get_line2())

    def test_indoor(self):
        weather_item = self.__get_weather_item(WeatherItemType.INDOOR)
        self.assertEqual("Indoor", weather_item.get_line1())
        self.assertEqual("20.4°C 45%", weather_item.get_line2())

    def test_last_update(self):
        weather_item = self.__get_weather_item(WeatherItemType.LAST_UPDATE)
        self.assertEqual("Last Update", weather_item.get_line1())
        self.assertEqual("23:59", weather_item.get_line2())

    def test_rainfall_rate(self):
        weather_item = self.__get_weather_item(WeatherItemType.RAINFALL_RATE)
        self.assertEqual("Rainfall Rate", weather_item.get_line1())
        self.assertEqual("1.23 mm/min", weather_item.get_line2())

    def test_surface_pressure(self):
        weather_item = self.__get_weather_item(WeatherItemType.SURFACE_PRESSURE)
        self.assertEqual("Surface Pressure", weather_item.get_line1())
        self.assertEqual("1019.7 hPa ➙", weather_item.get_line2())

    def test_temperature(self):
        weather_item = self.__get_weather_item(WeatherItemType.TEMPERATURE)
        self.assertEqual("Temperature", weather_item.get_line1())
        self.assertEqual("25.4°C ➘", weather_item.get_line2())

    def test_uv_index(self):
        weather_item = self.__get_weather_item(WeatherItemType.UV_INDEX)
        self.assertEqual("UV Index", weather_item.get_line1())
        self.assertEqual("4.2 moderate", weather_item.get_line2())

    def test_wind_chill(self):
        weather_item = self.__get_weather_item(WeatherItemType.WIND_CHILL)
        self.assertEqual("Wind Chill", weather_item.get_line1())
        self.assertEqual("23.2°C", weather_item.get_line2())

if __name__ == '__main__':
    unittest.main()
