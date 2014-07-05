# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

from decimal import *
from measures import Trend
from units import PressureUnit
from units import RainfallUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit


class ForecastFormatter:

    def __init__(self, forecast):
        self.__forecast = forecast

    def format(self):
        if self.__forecast is not None:
            return self.__forecast
        else:
            return "-----"


class HumidityFormatter:

    def __init__(self, humidity):
        self.__humidity = humidity

    def format(self):
        if self.__humidity is not None:
            return str(self.__humidity) + "%"
        else:
            return "--%"


class PressureFormatter:

    def __init__(self, pressure):
        self.__pressure = pressure

    def format(self, pressure_unit):
        if self.__pressure is not None:
            if pressure_unit is PressureUnit.HECTOPASCALS:
                return "{:.1f}".format(round(self.__pressure.get_value(pressure_unit), 1)) + " hPa"
            elif pressure_unit is PressureUnit.MILLIBARS:
                return "{:.1f}".format(round(self.__pressure.get_value(pressure_unit), 1)) + " mb"
            elif pressure_unit is PressureUnit.KILOPASCALS:
                return "{:.2f}".format(round(self.__pressure.get_value(pressure_unit), 2)) + " kPa"
            elif pressure_unit is PressureUnit.INCHES_OF_MERCURY:
                return "{:.2f}".format(round(self.__pressure.get_value(pressure_unit), 2)) + " inHg"
            else:
                return "{:.1f}".format(round(self.__pressure.get_value(pressure_unit), 1)) + " mmHg"
        else:
            if pressure_unit is PressureUnit.HECTOPASCALS:
                return "----.- hPa"
            elif pressure_unit is PressureUnit.MILLIBARS:
                return "----.- mb"
            elif pressure_unit is PressureUnit.KILOPASCALS:
                return "---.-- kPa"
            elif pressure_unit is PressureUnit.INCHES_OF_MERCURY:
                return "--.-- inHg"
            else:
                return "---.- mmHg"


class RainfallFormatter:

    def __init__(self, rainfall):
        self.__rainfall = rainfall

    def format(self, rainfall_unit):
        if self.__rainfall is not None:
            if rainfall_unit is RainfallUnit.MILLIMETRES:
                suffix = "mm"
            else:
                suffix = "in"
            return "{:.2f}".format(round(self.__rainfall.get_value(rainfall_unit), 2)) + " " + suffix
        else:
            if rainfall_unit is RainfallUnit.MILLIMETRES:
                return "-.-- mm"
            else:
                return "-.-- in"


class RainfallRateFormatter:

    def __init__(self, rainfall_rate):
        self.__rainfall_rate = rainfall_rate

    def format(self, rainfall_unit):
        if self.__rainfall_rate is not None:
            if rainfall_unit is RainfallUnit.MILLIMETRES:
                return "{:.2f}".format(round(self.__rainfall_rate.get_value(rainfall_unit), 2)) + " mm/min"
            else:
                return "{:.3f}".format(round(self.__rainfall_rate.get_value(rainfall_unit), 3)) + " in/min"
        else:

            if rainfall_unit is RainfallUnit.MILLIMETRES:
                return "-.-- mm/min"
            else:
                return "-.--- in/min"


class TemperatureFormatter:

    def __init__(self, temperature):
        self.__temperature = temperature

    def format(self, temperature_unit):
        if self.__temperature is not None:
            if temperature_unit is TemperatureUnit.CELSIUS:
                suffix = "°C"
            else:
                suffix = "°F"
            return "{:.1f}".format(round(self.__temperature.get_value(temperature_unit), 1)) + suffix
        else:
            if temperature_unit is TemperatureUnit.CELSIUS:
                return "--.-°C"
            else:
                return "--.-°F"


class TimeFormatter:

    def __init__(self, hour, minute):
        self.__hour = hour
        self.__minute = minute

    def format(self):
        if self.__hour is not None and self.__minute is not None:
            return "{0:02d}".format(self.__hour) + ":" + "{0:02d}".format(self.__minute)
        else:
            return "--:--"


class TrendFormatter:

    def __init__(self, trend):
        self.__trend = trend

    def format(self):

        if self.__trend is not None:
            if self.__trend is Trend.RISING:
                return "➚"
            elif self.__trend is Trend.STEADY:
                return "➙"
            else:
                return "➘"
        else:
            return "-"


class UvIndexFormatter:

    def __init__(self, uv_index):
        self.__uv_index = uv_index

    def format(self):
        if self.__uv_index is not None:
            index = "{:.1f}".format(round(self.__uv_index, 1))
            return index + " " + self.__get_uv_index_description()
        else:
            return "-.- -----"

    def __get_uv_index_description(self):
        with localcontext() as context:
            context.rounding = ROUND_HALF_DOWN
            uv_index_rounded = round(Decimal(self.__uv_index), 0)
            if uv_index_rounded < 3:
                return "low"
            elif 3 <= uv_index_rounded <= 5:
                return "moderate"
            elif 6 <= uv_index_rounded <= 7:
                return "high"
            elif 8 <= uv_index_rounded <= 10:
                return "very high"
            else:
                return "extreme"


class WindDirectionFormatter:

    def __init__(self, wind_direction):
        self.__wind_direction = wind_direction

    def format(self, wind_direction_unit):
        if self.__wind_direction is not None:
            if wind_direction_unit is WindDirectionUnit.COMPASS_DEGREES:
                return str(self.__wind_direction.get_value(wind_direction_unit)) + "°"
            else:
                return self.__wind_direction.get_value(wind_direction_unit)
        else:
            if wind_direction_unit is WindDirectionUnit.COMPASS_DEGREES:
                return "---°"
            else:
                return "---"


class WindSpeedFormatter:

    def __init__(self, wind_speed):
        self.__wind_speed = wind_speed

    def format(self, wind_speed_unit):
        if self.__wind_speed is not None:
            if wind_speed_unit is WindSpeedUnit.BEAUFORT_SCALE:
                return str(self.__wind_speed.get_value(wind_speed_unit)) + " Bft"
            elif wind_speed_unit is WindSpeedUnit.KNOTS:
                suffix = "kts"
            elif wind_speed_unit is WindSpeedUnit.METRES_PER_SECOND:
                suffix = "m/s"
            elif wind_speed_unit is WindSpeedUnit.KILOMETRES_PER_HOUR:
                suffix = "kph"
            else:
                suffix = "mph"
            return "{:.1f}".format(round(self.__wind_speed.get_value(wind_speed_unit), 1)) + " " + suffix
        else:
            if wind_speed_unit is WindSpeedUnit.KNOTS:
                return "--.- kts"
            elif wind_speed_unit is WindSpeedUnit.METRES_PER_SECOND:
                return "--.- m/s"
            elif wind_speed_unit is WindSpeedUnit.KILOMETRES_PER_HOUR:
                return "--.- kph"
            elif wind_speed_unit is WindSpeedUnit.MILES_PER_HOUR:
                return "--.- mph"
            else:
                return "-- Bft"
