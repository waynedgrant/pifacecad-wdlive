# Copyright 2015 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

from measures import Pressure
from measures import Rainfall
from measures import Temperature
from measures import Trend
from measures import WindDirection
from measures import WindSpeed


class ClientRaw:

    VALID_HEADER_VALUE = "12345"
    HEADER = 0
    AVERAGE_WIND_SPEED_KNOTS = 1
    GUST_SPEED_KNOTS = 2
    WIND_DIRECTION_COMPASS_DEGREES = 3
    OUTDOOR_TEMPERATURE_CELSIUS = 4
    OUTDOOR_HUMIDITY = 5
    SURFACE_PRESSURE_HECTOPASCALS = 6
    DAILY_RAINFALL_MILLIMETRES = 7
    RAINFALL_RATE_MILLIMETRES_PER_MINUTE = 10
    INDOOR_TEMPERATURE_CELSIUS = 12
    INDOOR_HUMIDITY = 13
    FORECAST = 15
    HOUR = 29
    MINUTE = 30
    WIND_CHILL_CELSIUS = 44
    HUMIDEX_CELSIUS = 45
    SURFACE_PRESSURE_TREND = 50
    DEW_POINT_CELSIUS = 72
    UV_INDEX = 79
    HEAT_INDEX_CELSIUS = 112
    OUTDOOR_TEMPERATURE_TREND = 143
    OUTDOOR_HUMIDITY_TREND = 144

    FORECASTS = ["Sunny", "Clear Night", "Cloudy", "Cloudy", "Cloudy Night", "Dry Clear", "Fog", "Hazy", "Heavy Rain",
                 "Mainly Fine", "Misty", "Night Fog", "Night Heavy Rain", "Night Overcast", "Night Rain",
                 "Night Showers", "Night Snow", "Night Thunder", "Overcast", "Partly Cloudy", "Rain", "Hard Rain",
                 "Showers", "Sleet", "Sleet Showers", "Snow", "Snow Melt", "Snow Showers", "Sunny", "Thunder Showers",
                 "Thunder Showers", "Thunderstorms", "Tornado Warning", "Windy", "Stopped Raining", "Windy Rain"]

    def __init__(self, clientraw):
        if len(clientraw) == 0:
            self.__fields = []
        else:
            self.__fields = clientraw.split(' ')

    def is_empty(self):
        return len(self.__fields) == 0

    def is_valid(self):
        if len(self.__fields) > self.HEADER:
            return self.__get_field_value_as_string(self.HEADER) == self.VALID_HEADER_VALUE
        else:
            return False

    def get_average_wind_speed(self):
        return self.__get_field_value_as_wind_speed(self.AVERAGE_WIND_SPEED_KNOTS)

    def get_gust_speed(self):
        return self.__get_field_value_as_wind_speed(self.GUST_SPEED_KNOTS)

    def get_wind_direction(self):
        return self.__get_field_value_as_wind_direction(self.WIND_DIRECTION_COMPASS_DEGREES)

    def get_outdoor_temperature(self):
        return self.__get_field_value_as_temperature(self.OUTDOOR_TEMPERATURE_CELSIUS)

    def get_outdoor_humidity(self):
        return self.__get_field_value_as_int(self.OUTDOOR_HUMIDITY)

    def get_surface_pressure(self):
        return self.__get_field_value_as_pressure(self.SURFACE_PRESSURE_HECTOPASCALS)

    def get_daily_rainfall(self):
        return self.__get_field_value_as_rainfall(self.DAILY_RAINFALL_MILLIMETRES)

    def get_rainfall_rate(self):
        return self.__get_field_value_as_rainfall(self.RAINFALL_RATE_MILLIMETRES_PER_MINUTE)

    def get_indoor_temperature(self):
        return self.__get_field_value_as_temperature(self.INDOOR_TEMPERATURE_CELSIUS)

    def get_indoor_humidity(self):
        return self.__get_field_value_as_int(self.INDOOR_HUMIDITY)

    def get_forecast(self):
        forecast_icon = self.__get_field_value_as_int(self.FORECAST)
        if forecast_icon is not None:
            if forecast_icon < len(self.FORECASTS):
                return self.FORECASTS[forecast_icon]

    def get_hour(self):
        return self.__get_field_value_as_int(self.HOUR)

    def get_minute(self):
        return self.__get_field_value_as_int(self.MINUTE)

    def get_wind_chill(self):
        return self.__get_field_value_as_temperature(self.WIND_CHILL_CELSIUS)

    def get_humidex(self):
        return self.__get_field_value_as_temperature(self.HUMIDEX_CELSIUS)

    def get_surface_pressure_trend(self):
        return self.__get_field_value_as_trend(self.SURFACE_PRESSURE_TREND)

    def get_dew_point(self):
        return self.__get_field_value_as_temperature(self.DEW_POINT_CELSIUS)

    def get_uv_index(self):
        return self.__get_field_value_as_float(self.UV_INDEX)

    def get_heat_index(self):
        return self.__get_field_value_as_temperature(self.HEAT_INDEX_CELSIUS)

    def get_outdoor_temperature_trend(self):
        return self.__get_field_value_as_trend(self.OUTDOOR_TEMPERATURE_TREND)

    def get_outdoor_humidity_trend(self):
        return self.__get_field_value_as_trend(self.OUTDOOR_HUMIDITY_TREND)

    def __get_field_value_as_pressure(self, field_position):
        hectopascals = self.__get_field_value_as_float(field_position)
        if hectopascals is not None:
            return Pressure(hectopascals)

    def __get_field_value_as_rainfall(self, field_position):
        millimetres = self.__get_field_value_as_float(field_position)
        if millimetres is not None:
            return Rainfall(millimetres)

    def __get_field_value_as_temperature(self, field_position):
        celsius = self.__get_field_value_as_float(field_position)
        if celsius is not None:
            return Temperature(celsius)

    def __get_field_value_as_trend(self, field_position):
        trend = self.__get_field_value_as_float(field_position)
        if trend is not None:
            if trend < 0:
                return Trend.FALLING
            elif trend > 0:
                return Trend.RISING
            else:
                return Trend.STEADY

    def __get_field_value_as_wind_direction(self, field_position):
        compass_degrees = self.__get_field_value_as_int(field_position)
        if compass_degrees is not None:
            return WindDirection(compass_degrees)

    def __get_field_value_as_wind_speed(self, field_position):
        knots = self.__get_field_value_as_float(field_position)
        if knots is not None:
            return WindSpeed(knots)

    def __get_field_value_as_float(self, field_position):
        if len(self.__fields) > field_position:
            try:
                return float(self.__fields[field_position])
            except ValueError:
                return None

    def __get_field_value_as_int(self, field_position):
        if len(self.__fields) > field_position:
            try:
                return int(self.__fields[field_position])
            except ValueError:
                return None

    def __get_field_value_as_string(self, field_position):
        if len(self.__fields) > field_position:
            return self.__fields[field_position]
