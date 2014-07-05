# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

import unittest
from measures import Pressure
from measures import Rainfall
from measures import Temperature
from measures import WindDirection
from measures import WindSpeed
from units import PressureUnit
from units import RainfallUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit


class TestPressure(unittest.TestCase):

    def test_hectopascals(self):
        testee = Pressure(0)
        self.assertEqual(0, testee.get_value(PressureUnit.HECTOPASCALS))
        testee = Pressure(1017.7)
        self.assertEqual(1017.7, testee.get_value(PressureUnit.HECTOPASCALS))

    def test_millibars(self):
        testee = Pressure(0)
        self.assertEqual(0, testee.get_value(PressureUnit.MILLIBARS))
        testee = Pressure(1017.7)
        self.assertEqual(1017.7, testee.get_value(PressureUnit.MILLIBARS))

    def test_kilopascals(self):
        testee = Pressure(0)
        self.assertEqual(0, testee.get_value(PressureUnit.KILOPASCALS))
        testee = Pressure(1017.7)
        self.assertEqual(101.77, testee.get_value(PressureUnit.KILOPASCALS))

    def test_inches_of_mercury(self):
        testee = Pressure(0)
        self.assertEqual(0, testee.get_value(PressureUnit.INCHES_OF_MERCURY))
        testee = Pressure(1017.7)
        self.assertEqual(30.05268, testee.get_value(PressureUnit.INCHES_OF_MERCURY))

    def test_millimetres_of_mercury(self):
        testee = Pressure(0)
        self.assertEqual(0, testee.get_value(PressureUnit.MILLMETRES_OF_MERCURY))
        testee = Pressure(1017.7)
        self.assertEqual(763.3381, testee.get_value(PressureUnit.MILLMETRES_OF_MERCURY))


class TestRainfall(unittest.TestCase):

    def test_millimetres(self):
        testee = Rainfall(0)
        self.assertEqual(0, testee.get_value(RainfallUnit.MILLIMETRES))
        testee = Rainfall(2.5)
        self.assertEqual(2.5, testee.get_value(RainfallUnit.MILLIMETRES))

    def test_inches(self):
        testee = Rainfall(0)
        self.assertEqual(0, testee.get_value(RainfallUnit.INCHES))
        testee = Rainfall(50)
        self.assertEqual(1.968504, testee.get_value(RainfallUnit.INCHES))


class TestTemperature(unittest.TestCase):

    def test_celsius(self):
        testee = Temperature(-25.5)
        self.assertEqual(-25.5, testee.get_value(TemperatureUnit.CELSIUS))
        testee = Temperature(0)
        self.assertEqual(0, testee.get_value(TemperatureUnit.CELSIUS))
        testee = Temperature(25.5)
        self.assertEqual(25.5, testee.get_value(TemperatureUnit.CELSIUS))

    def test_fahrenheit(self):
        testee = Temperature(-50.5)
        self.assertEqual(-58.9, testee.get_value(TemperatureUnit.FAHRENHEIT))
        testee = Temperature(0)
        self.assertEqual(32, testee.get_value(TemperatureUnit.FAHRENHEIT))
        testee = Temperature(50.5)
        self.assertEqual(122.9, testee.get_value(TemperatureUnit.FAHRENHEIT))


class TestWindDirection(unittest.TestCase):

    def test_compass_degrees(self):
        testee = WindDirection(0)
        self.assertEqual(0, testee.get_value(WindDirectionUnit.COMPASS_DEGREES))
        testee = WindDirection(180)
        self.assertEqual(180, testee.get_value(WindDirectionUnit.COMPASS_DEGREES))

    def test_cardinal_direction(self):
        testee = WindDirection(0)
        self.assertEqual("N", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(22)
        self.assertEqual("NNE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(45)
        self.assertEqual("NE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(68)
        self.assertEqual("ENE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(90)
        self.assertEqual("E", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(112)
        self.assertEqual("ESE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(135)
        self.assertEqual("SE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(158)
        self.assertEqual("SSE", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(180)
        self.assertEqual("S", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(202)
        self.assertEqual("SSW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(225)
        self.assertEqual("SW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(248)
        self.assertEqual("WSW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(270)
        self.assertEqual("W", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(292)
        self.assertEqual("WNW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(315)
        self.assertEqual("NW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirection(338)
        self.assertEqual("NNW", testee.get_value(WindDirectionUnit.CARDINAL_DIRECTION))


class TestWindSpeed(unittest.TestCase):

    def test_knots(self):
        testee = WindSpeed(0)
        self.assertEqual(0, testee.get_value(WindSpeedUnit.KNOTS))
        testee = WindSpeed(5)
        self.assertEqual(5, testee.get_value(WindSpeedUnit.KNOTS))

    def test_metres_per_second(self):
        testee = WindSpeed(0)
        self.assertEqual(0, testee.get_value(WindSpeedUnit.METRES_PER_SECOND))
        testee = WindSpeed(5)
        self.assertEqual(2.57222, testee.get_value(WindSpeedUnit.METRES_PER_SECOND))

    def test_kilometeres_per_hour(self):
        testee = WindSpeed(0)
        self.assertEqual(0, testee.get_value(WindSpeedUnit.KILOMETRES_PER_HOUR))
        testee = WindSpeed(5)
        self.assertEqual(9.26, testee.get_value(WindSpeedUnit.KILOMETRES_PER_HOUR))

    def test_miles_per_hour(self):
        testee = WindSpeed(0)
        self.assertEqual(0, testee.get_value(WindSpeedUnit.MILES_PER_HOUR))
        testee = WindSpeed(5)
        self.assertEqual(5.7539, testee.get_value(WindSpeedUnit.MILES_PER_HOUR))

    def test_beaufort_scale(self):
        self.assertEqual(0, WindSpeed(0).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(0, WindSpeed(0.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(1, WindSpeed(0.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(1, WindSpeed(3.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(2, WindSpeed(3.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(2, WindSpeed(6.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(3, WindSpeed(6.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(3, WindSpeed(10.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(4, WindSpeed(10.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(4, WindSpeed(16.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(5, WindSpeed(16.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(5, WindSpeed(21.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(6, WindSpeed(21.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(6, WindSpeed(27.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(7, WindSpeed(27.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(7, WindSpeed(33.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(8, WindSpeed(33.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(8, WindSpeed(40.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(9, WindSpeed(40.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(9, WindSpeed(47.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(10, WindSpeed(47.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(10, WindSpeed(55.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(11, WindSpeed(55.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(11, WindSpeed(63.4).get_value(WindSpeedUnit.BEAUFORT_SCALE))
        self.assertEqual(12, WindSpeed(63.5).get_value(WindSpeedUnit.BEAUFORT_SCALE))

if __name__ == '__main__':
    unittest.main()
