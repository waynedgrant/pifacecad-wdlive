# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

from formatters import ForecastFormatter
from formatters import HumidityFormatter
from formatters import PressureFormatter
from formatters import RainfallFormatter
from formatters import RainfallRateFormatter
from formatters import TemperatureFormatter
from formatters import TimeFormatter
from formatters import TrendFormatter
from formatters import WindDirectionFormatter
from formatters import WindSpeedFormatter
from formatters import UvIndexFormatter


class WeatherItemType:

    SUMMARY = 0
    AVERAGE_WIND = 1
    DAILY_RAINFALL = 2
    DEW_POINT = 3
    FORECAST = 4
    GUST_SPEED = 5
    HEAT_INDEX = 6
    HUMIDEX = 7
    HUMIDITY = 8
    INDOOR = 9
    LAST_UPDATE = 10
    RAINFALL_RATE = 11
    SURFACE_PRESSURE = 12
    TEMPERATURE = 13
    UV_INDEX = 14
    WIND_CHILL = 15

    def get_all(self):
        return [self.SUMMARY, self.FORECAST, self.TEMPERATURE, self.SURFACE_PRESSURE, self.HUMIDITY,
                self.AVERAGE_WIND, self.GUST_SPEED, self.DAILY_RAINFALL, self.RAINFALL_RATE, self.DEW_POINT,
                self.WIND_CHILL, self.HEAT_INDEX, self.HUMIDEX, self.UV_INDEX, self.INDOOR, self.LAST_UPDATE]


class WeatherItem:

    def __init__(self, line1, line2):
        self.__line1 = line1
        self.__line2 = line2

    def get_line1(self):
        return self.__line1

    def get_line2(self):
        return self.__line2


class WeatherItemFactory:

    def __init__(self, clientraw, settings):
        self.__clientraw = clientraw
        self.__weather_item_type = settings.get_weather_item_type()
        self.__pressure_unit = settings.get_pressure_unit()
        self.__rainfall_unit = settings.get_rainfall_unit()
        self.__temperature_unit = settings.get_temperature_unit()
        self.__wind_direction_unit = settings.get_wind_direction_unit()
        self.__wind_speed_unit = settings.get_wind_speed_unit()

    def get_weather_item(self):

        if self.__weather_item_type is WeatherItemType.SUMMARY:
            line1 = TemperatureFormatter(self.__clientraw.get_outdoor_temperature()).format(self.__temperature_unit) +\
                " " + TrendFormatter(self.__clientraw.get_outdoor_temperature_trend()).format() +\
                " " + HumidityFormatter(self.__clientraw.get_outdoor_humidity()).format() +\
                " " + TrendFormatter(self.__clientraw.get_outdoor_humidity_trend()).format()
            line2 = PressureFormatter(self.__clientraw.get_surface_pressure()).format(self.__pressure_unit) +\
                " " + TrendFormatter(self.__clientraw.get_surface_pressure_trend()).format()

        elif self.__weather_item_type is WeatherItemType.AVERAGE_WIND:
            line1 = "Average Wind"
            line2 = WindSpeedFormatter(self.__clientraw.get_average_wind_speed()).format(self.__wind_speed_unit) +\
                " " + WindDirectionFormatter(self.__clientraw.get_wind_direction()).format(self.__wind_direction_unit)

        elif self.__weather_item_type is WeatherItemType.DAILY_RAINFALL:
            line1 = "Daily Rainfall"
            line2 = RainfallFormatter(self.__clientraw.get_daily_rainfall()).format(self.__rainfall_unit)

        elif self.__weather_item_type is WeatherItemType.DEW_POINT:
            line1 = "Dew Point"
            line2 = TemperatureFormatter(self.__clientraw.get_dew_point()).format(self.__temperature_unit)

        elif self.__weather_item_type is WeatherItemType.FORECAST:
            line1 = "Forecast"
            line2 = ForecastFormatter(self.__clientraw.get_forecast()).format()

        elif self.__weather_item_type is WeatherItemType.GUST_SPEED:
            line1 = "Gust Speed"
            line2 = WindSpeedFormatter(self.__clientraw.get_gust_speed()).format(self.__wind_speed_unit)

        elif self.__weather_item_type is WeatherItemType.HEAT_INDEX:
            line1 = "Heat Index"
            line2 = TemperatureFormatter(self.__clientraw.get_heat_index()).format(self.__temperature_unit)

        elif self.__weather_item_type is WeatherItemType.HUMIDEX:
            line1 = "Humidex"
            line2 = TemperatureFormatter(self.__clientraw.get_humidex()).format(self.__temperature_unit)

        elif self.__weather_item_type is WeatherItemType.HUMIDITY:
            line1 = "Humidity"
            line2 = HumidityFormatter(self.__clientraw.get_outdoor_humidity()).format() +\
                " " + TrendFormatter(self.__clientraw.get_outdoor_humidity_trend()).format()

        elif self.__weather_item_type is WeatherItemType.INDOOR:
            line1 = "Indoor"
            line2 = TemperatureFormatter(self.__clientraw.get_indoor_temperature()).format(self.__temperature_unit) +\
                " " + HumidityFormatter(self.__clientraw.get_indoor_humidity()).format()

        elif self.__weather_item_type is WeatherItemType.LAST_UPDATE:
            line1 = "Last Update"
            line2 = TimeFormatter(self.__clientraw.get_hour(), self.__clientraw.get_minute()).format()

        elif self.__weather_item_type is WeatherItemType.RAINFALL_RATE:
            line1 = "Rainfall Rate"
            line2 = RainfallRateFormatter(self.__clientraw.get_rainfall_rate()).format(self.__rainfall_unit)

        elif self.__weather_item_type is WeatherItemType.SURFACE_PRESSURE:
            line1 = "Surface Pressure"
            line2 = PressureFormatter(self.__clientraw.get_surface_pressure()).format(self.__pressure_unit) +\
                " " + TrendFormatter(self.__clientraw.get_surface_pressure_trend()).format()

        elif self.__weather_item_type is WeatherItemType.TEMPERATURE:
            line1 = "Temperature"
            line2 = TemperatureFormatter(self.__clientraw.get_outdoor_temperature()).format(self.__temperature_unit) +\
                " " + TrendFormatter(self.__clientraw.get_outdoor_temperature_trend()).format()

        elif self.__weather_item_type is WeatherItemType.UV_INDEX:
            line1 = "UV Index"
            line2 = UvIndexFormatter(self.__clientraw.get_uv_index()).format()

        else:
            line1 = "Wind Chill"
            line2 = TemperatureFormatter(self.__clientraw.get_wind_chill()).format(self.__temperature_unit)

        return WeatherItem(line1, line2)
