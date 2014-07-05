# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

from cyclical import Cyclical
from units import PressureUnit
from units import TemperatureUnit
from units import RainfallUnit
from units import WindDirectionUnit
from units import WindSpeedUnit
from weatheritems import WeatherItemType


class Settings:

    def __init__(self):
        self.__weather_item_types = Cyclical(WeatherItemType().get_all())
        self.__pressure_units = Cyclical(PressureUnit().get_all())
        self.__rainfall_units = Cyclical(RainfallUnit().get_all())
        self.__temperature_units = Cyclical(TemperatureUnit().get_all())
        self.__wind_direction_units = Cyclical(WindDirectionUnit().get_all())
        self.__wind_speed_units = Cyclical(WindSpeedUnit().get_all())

    def next_weather_item_type(self):
        self.__weather_item_types.next()

    def previous_weather_item_type(self):
        self.__weather_item_types.previous()

    def get_weather_item_type(self):
        return self.__weather_item_types.current()

    def change_pressure_unit(self):
        self.__pressure_units.next()

    def get_pressure_unit(self):
        return self.__pressure_units.current()

    def change_rainfall_unit(self):
        self.__rainfall_units.next()

    def get_rainfall_unit(self):
        return self.__rainfall_units.current()

    def change_temperature_unit(self):
        self.__temperature_units.next()

    def get_temperature_unit(self):
        return self.__temperature_units.current()

    def change_wind_direction_unit(self):
        self.__wind_direction_units.next()

    def get_wind_direction_unit(self):
        return self.__wind_direction_units.current()

    def change_wind_speed_unit(self):
        self.__wind_speed_units.next()

    def get_wind_speed_unit(self):
        return self.__wind_speed_units.current()
