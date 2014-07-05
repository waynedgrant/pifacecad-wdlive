# Copyright 2014 Wayne D Grant (www.waynedgrant.com)

import unittest
from settings import Settings
from units import PressureUnit
from units import RainfallUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit
from weatheritems import WeatherItemType


class TestSettings(unittest.TestCase):

    def test_weather_item_type(self):
        testee = Settings()
        self.assertEqual(WeatherItemType.SUMMARY, testee.get_weather_item_type())
        testee.next_weather_item_type()
        self.assertEqual(WeatherItemType.FORECAST, testee.get_weather_item_type())
        testee.previous_weather_item_type()
        self.assertEqual(WeatherItemType.SUMMARY, testee.get_weather_item_type())

    def test_pressure_unit(self):
        testee = Settings()
        self.assertEqual(PressureUnit.HECTOPASCALS, testee.get_pressure_unit())
        testee.change_pressure_unit()
        self.assertEqual(PressureUnit.INCHES_OF_MERCURY, testee.get_pressure_unit())

    def test_rainfall_unit(self):
        testee = Settings()
        self.assertEqual(RainfallUnit.MILLIMETRES, testee.get_rainfall_unit())
        testee.change_rainfall_unit()
        self.assertEqual(RainfallUnit.INCHES, testee.get_rainfall_unit())

    def test_temperature_unit(self):
        testee = Settings()
        self.assertEqual(TemperatureUnit.CELSIUS, testee.get_temperature_unit())
        testee.change_temperature_unit()
        self.assertEqual(TemperatureUnit.FAHRENHEIT, testee.get_temperature_unit())

    def test_wind_direction_unit(self):
        testee = Settings()
        self.assertEqual(WindDirectionUnit.CARDINAL_DIRECTION, testee.get_wind_direction_unit())
        testee.change_wind_direction_unit()
        self.assertEqual(WindDirectionUnit.COMPASS_DEGREES, testee.get_wind_direction_unit())

    def test_wind_speed_unit(self):
        testee = Settings()
        self.assertEqual(WindSpeedUnit.MILES_PER_HOUR, testee.get_wind_speed_unit())
        testee.change_wind_speed_unit()
        self.assertEqual(WindSpeedUnit.BEAUFORT_SCALE, testee.get_wind_speed_unit())
