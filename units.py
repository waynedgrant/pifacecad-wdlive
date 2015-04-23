# Copyright 2015 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License


class PressureUnit:

    HECTOPASCALS = 1
    INCHES_OF_MERCURY = 2
    KILOPASCALS = 3
    MILLIBARS = 4
    MILLMETRES_OF_MERCURY = 5

    def get_all(self):
        return [self.KILOPASCALS, self.MILLIBARS, self.MILLMETRES_OF_MERCURY,
                self.HECTOPASCALS, self.INCHES_OF_MERCURY, ]


class RainfallUnit:

    INCHES = 1
    MILLIMETRES = 2

    def get_all(self):
        return [self.MILLIMETRES, self.INCHES]


class TemperatureUnit:

    CELSIUS = 1
    FAHRENHEIT = 2

    def get_all(self):
        return [self.CELSIUS, self.FAHRENHEIT]


class WindDirectionUnit:

    CARDINAL_DIRECTION = 1
    COMPASS_DEGREES = 2

    def get_all(self):
        return [self.CARDINAL_DIRECTION, self.COMPASS_DEGREES]


class WindSpeedUnit:

    BEAUFORT_SCALE = 1
    KILOMETRES_PER_HOUR = 2
    KNOTS = 3
    METRES_PER_SECOND = 4
    MILES_PER_HOUR = 5

    def get_all(self):
        return [self.MILES_PER_HOUR, self.BEAUFORT_SCALE, self.KILOMETRES_PER_HOUR,
                self.KNOTS, self.METRES_PER_SECOND]
