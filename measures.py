# Copyright 2015 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

from decimal import *
from units import PressureUnit
from units import RainfallUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit


def setup_decimal_context(context):
    context.prec = 7


class Pressure:

    def __init__(self, hectopascals):
        with localcontext() as context:
            setup_decimal_context(context)
            self.__hectopascals = hectopascals
            self.__millibars = hectopascals
            self.__kilopascals = float(Decimal(hectopascals) / 10)
            self.__inches_of_mercury = float(Decimal(hectopascals) * Decimal(0.02953))
            self.__millimeters_of_mercury = float(Decimal(hectopascals) * Decimal(0.750062))

    def get_value(self, pressure_unit):
        if pressure_unit is PressureUnit.HECTOPASCALS:
            return self.__hectopascals
        elif pressure_unit is PressureUnit.MILLIBARS:
            return self.__millibars
        elif pressure_unit is PressureUnit.KILOPASCALS:
            return self.__kilopascals
        elif pressure_unit is PressureUnit.INCHES_OF_MERCURY:
            return self.__inches_of_mercury
        else:
            return self.__millimeters_of_mercury


class Rainfall:

    def __init__(self, millimetres):
        with localcontext() as context:
            setup_decimal_context(context)
            self.__millimetres = millimetres
            self.__inches = float(Decimal(millimetres) * Decimal(1 / 25.4))

    def get_value(self, rainfall_unit):
        if rainfall_unit is RainfallUnit.MILLIMETRES:
            return self.__millimetres
        else:
            return self.__inches


class Temperature:

    def __init__(self, celsius):
        with localcontext() as context:
            setup_decimal_context(context)
            self.__celsius = celsius
            self.__fahrenheit = float((Decimal(celsius) * Decimal(1.8)) + 32)

    def get_value(self, temperature_unit):
        if temperature_unit is TemperatureUnit.CELSIUS:
            return self.__celsius
        else:
            return self.__fahrenheit


class Trend:

    RISING = 1
    FALLING = 2
    STEADY = 3


class WindDirection:

    CARDINAL_DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

    def __init__(self, compass_degrees):
        self.__compass_degrees = compass_degrees
        self.__cardinal_direction = self.CARDINAL_DIRECTIONS[int((compass_degrees + 11) / 22.5) % 16]

    def get_value(self, wind_direction_unit):
        if wind_direction_unit is WindDirectionUnit.COMPASS_DEGREES:
            return self.__compass_degrees
        else:
            return self.__cardinal_direction


class WindSpeed:

    def __init__(self, knots):
        with localcontext() as context:
            setup_decimal_context(context)
            self.__knots = knots
            self.__metres_per_second = float(Decimal(knots) * Decimal(0.514444))
            self.__kilometres_per_hour = float(Decimal(knots) * Decimal(1.852))
            self.__miles_per_hour = float(Decimal(knots) * Decimal(1.15078))
            self.__beaufort_scale = self.__calculate_beaufort_scale()

    def __calculate_beaufort_scale(self):
        with localcontext() as context:
            context.rounding = ROUND_HALF_UP
            rounded_knots = round(Decimal(self.__knots), 0)
            if rounded_knots < 1:
                return 0
            elif 1 <= rounded_knots <= 3:
                return 1
            elif 4 <= rounded_knots <= 6:
                return 2
            elif 7 <= rounded_knots <= 10:
                return 3
            elif 11 <= rounded_knots <= 16:
                return 4
            elif 17 <= rounded_knots <= 21:
                return 5
            elif 22 <= rounded_knots <= 27:
                return 6
            elif 28 <= rounded_knots <= 33:
                return 7
            elif 34 <= rounded_knots <= 40:
                return 8
            elif 41 <= rounded_knots <= 47:
                return 9
            elif 48 <= rounded_knots <= 55:
                return 10
            elif 56 <= rounded_knots <= 63:
                return 11
            else:
                return 12

    def get_value(self, wind_speed_unit):
        if wind_speed_unit is WindSpeedUnit.KNOTS:
            return self.__knots
        elif wind_speed_unit is WindSpeedUnit.METRES_PER_SECOND:
            return self.__metres_per_second
        elif wind_speed_unit is WindSpeedUnit.KILOMETRES_PER_HOUR:
            return self.__kilometres_per_hour
        elif wind_speed_unit is WindSpeedUnit.MILES_PER_HOUR:
            return self.__miles_per_hour
        else:
            return self.__beaufort_scale
