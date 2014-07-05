# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

import unittest
from formatters import ForecastFormatter
from formatters import HumidityFormatter
from formatters import PressureFormatter
from formatters import RainfallFormatter
from formatters import RainfallRateFormatter
from formatters import TemperatureFormatter
from formatters import TimeFormatter
from formatters import TrendFormatter
from formatters import UvIndexFormatter
from formatters import WindDirectionFormatter
from formatters import WindSpeedFormatter
from measures import Pressure
from measures import Rainfall
from measures import Temperature
from measures import WindDirection
from measures import WindSpeed
from measures import Trend
from units import PressureUnit
from units import RainfallUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit


class TestForecastFormatter(unittest.TestCase):

    def test_none_forecast(self):
        testee = ForecastFormatter(None)
        self.assertEqual("-----", testee.format())

    def test_non_none_forecast(self):
        testee = ForecastFormatter("Clear Night")
        self.assertEqual("Clear Night", testee.format())


class TestHumidityFormatter(unittest.TestCase):

    def test_none_humidity(self):
        testee = HumidityFormatter(None)
        self.assertEqual("--%", testee.format())

    def test_non_none_humidity(self):
        testee = HumidityFormatter(0)
        self.assertEqual("0%", testee.format())
        testee = HumidityFormatter(100)
        self.assertEqual("100%", testee.format())


class TestPressureFormatter(unittest.TestCase):

    def test_none_pressure_hectopascals(self):
        testee = PressureFormatter(None)
        self.assertEqual("----.- hPa", testee.format(PressureUnit.HECTOPASCALS))

    def test_non_none_pressure_hectopascals(self):
        testee = PressureFormatter(Pressure(1015.66))
        self.assertEqual("1015.7 hPa", testee.format(PressureUnit.HECTOPASCALS))

    def test_none_pressure_millibars(self):
        testee = PressureFormatter(None)
        self.assertEqual("----.- mb", testee.format(PressureUnit.MILLIBARS))

    def test_non_none_pressure_millibars(self):
        testee = PressureFormatter(Pressure(1015.66))
        self.assertEqual("1015.7 mb", testee.format(PressureUnit.MILLIBARS))

    def test_none_pressure_kilopascals(self):
        testee = PressureFormatter(None)
        self.assertEqual("---.-- kPa", testee.format(PressureUnit.KILOPASCALS))

    def test_non_none_pressure_kilopascals(self):
        testee = PressureFormatter(Pressure(1015.66))
        self.assertEqual("101.57 kPa", testee.format(PressureUnit.KILOPASCALS))
        
    def test_none_pressure_inches_of_mercury(self):
        testee = PressureFormatter(None)
        self.assertEqual("--.-- inHg", testee.format(PressureUnit.INCHES_OF_MERCURY))

    def test_non_none_pressure_inches_of_mercury(self):
        testee = PressureFormatter(Pressure(1013.75))  # == 29.93604 inHg
        self.assertEqual("29.94 inHg", testee.format(PressureUnit.INCHES_OF_MERCURY))

    def test_none_pressure_millimetres_of_mercury(self):
        testee = PressureFormatter(None)
        self.assertEqual("---.- mmHg", testee.format(PressureUnit.MILLMETRES_OF_MERCURY))

    def test_non_none_pressure_millimetres_of_mercury(self):
        testee = PressureFormatter(Pressure(1013.75))  # == 760.3754 mmHg
        self.assertEqual("760.4 mmHg", testee.format(PressureUnit.MILLMETRES_OF_MERCURY))


class TestRainfallFormatter(unittest.TestCase):

    def test_none_rainfall_millimetres(self):
        testee = RainfallFormatter(None)
        self.assertEqual("-.-- mm", testee.format(RainfallUnit.MILLIMETRES))

    def test_non_null_rainfall_millimetres(self):
        testee = RainfallFormatter(Rainfall(0))
        self.assertEqual("0.00 mm", testee.format(RainfallUnit.MILLIMETRES))
        testee = RainfallFormatter(Rainfall(5.666))
        self.assertEqual("5.67 mm", testee.format(RainfallUnit.MILLIMETRES))

    def test_none_rainfall_inches(self):
        testee = RainfallFormatter(None)
        self.assertEqual("-.-- in", testee.format(RainfallUnit.INCHES))

    def test_non_null_rainfall_inches(self):
        testee = RainfallFormatter(Rainfall(0))
        self.assertEqual("0.00 in", testee.format(RainfallUnit.INCHES))
        testee = RainfallFormatter(Rainfall(3))  # == 0.11811 in
        self.assertEqual("0.12 in", testee.format(RainfallUnit.INCHES))


class TestRainfallRateFormatter(unittest.TestCase):

    def test_none_rainfall_rate_millimetres(self):
        testee = RainfallRateFormatter(None)
        self.assertEqual("-.-- mm/min", testee.format(RainfallUnit.MILLIMETRES))

    def test_non_null_rainfall_rate_millimetres(self):
        testee = RainfallRateFormatter(Rainfall(0))
        self.assertEqual("0.00 mm/min", testee.format(RainfallUnit.MILLIMETRES))
        testee = RainfallRateFormatter(Rainfall(5.666))
        self.assertEqual("5.67 mm/min", testee.format(RainfallUnit.MILLIMETRES))

    def test_none_rainfall_rate_inches(self):
        testee = RainfallRateFormatter(None)
        self.assertEqual("-.--- in/min", testee.format(RainfallUnit.INCHES))

    def test_non_null_rainfall_rate_inches(self):
        testee = RainfallRateFormatter(Rainfall(0))
        self.assertEqual("0.000 in/min", testee.format(RainfallUnit.INCHES))
        testee = RainfallRateFormatter(Rainfall(8.6))  # == 0.338583 in
        self.assertEqual("0.339 in/min", testee.format(RainfallUnit.INCHES))


class TestTemperatureFormatter(unittest.TestCase):

    def test_none_temperature_celsius(self):
        testee = TemperatureFormatter(None)
        self.assertEqual("--.-°C", testee.format(TemperatureUnit.CELSIUS))

    def test_non_none_temperature_celsius(self):
        testee = TemperatureFormatter(Temperature(-15.66))
        self.assertEqual("-15.7°C", testee.format(TemperatureUnit.CELSIUS))
        testee = TemperatureFormatter(Temperature(0))
        self.assertEqual("0.0°C", testee.format(TemperatureUnit.CELSIUS))
        testee = TemperatureFormatter(Temperature(15.66))
        self.assertEqual("15.7°C", testee.format(TemperatureUnit.CELSIUS))

    def test_none_temperature_fahrenheit(self):
        testee = TemperatureFormatter(None)
        self.assertEqual("--.-°F", testee.format(TemperatureUnit.FAHRENHEIT))

    def test_non_none_temperature_fahrenheit(self):
        testee = TemperatureFormatter(Temperature(-25.12))  # == -13.216°F
        self.assertEqual("-13.2°F", testee.format(TemperatureUnit.FAHRENHEIT))
        testee = TemperatureFormatter(Temperature(-17.77))
        self.assertEqual("0.0°F", testee.format(TemperatureUnit.FAHRENHEIT))
        testee = TemperatureFormatter(Temperature(-9.072))  # == 15.6704°F
        self.assertEqual("15.7°F", testee.format(TemperatureUnit.FAHRENHEIT))


class TestTimeFormatter(unittest.TestCase):

    def test_none_time(self):
        testee = TimeFormatter(None, 59)
        self.assertEqual("--:--", testee.format())
        testee = TimeFormatter(23, None)
        self.assertEqual("--:--", testee.format())
        testee = TimeFormatter(None, None)
        self.assertEqual("--:--", testee.format())

    def test_non_none_time(self):
        testee = TimeFormatter(23, 59)
        self.assertEqual("23:59", testee.format())


class TestTrendFormatter(unittest.TestCase):

    def test_none_trend(self):
        testee = TrendFormatter(None)
        self.assertEqual("-", testee.format())

    def test_rising_trend(self):
        testee = TrendFormatter(Trend.RISING)
        self.assertEqual("➚", testee.format())

    def test_steady_trend(self):
        testee = TrendFormatter(Trend.STEADY)
        self.assertEqual("➙", testee.format())

    def test_falling_trend(self):
        testee = TrendFormatter(Trend.FALLING)
        self.assertEqual("➘", testee.format())


class TestUvIndexFormatter(unittest.TestCase):

    def test_none_uv_index(self):
        testee = UvIndexFormatter(None)
        self.assertEqual("-.- -----", testee.format())

    def test_non_none_uv_index(self):
        testee = UvIndexFormatter(0)
        self.assertEqual("0.0 low", testee.format())
        testee = UvIndexFormatter(2.5)
        self.assertEqual("2.5 low", testee.format())
        testee = UvIndexFormatter(2.6)
        self.assertEqual("2.6 moderate", testee.format())
        testee = UvIndexFormatter(5.5)
        self.assertEqual("5.5 moderate", testee.format())
        testee = UvIndexFormatter(5.6)
        self.assertEqual("5.6 high", testee.format())
        testee = UvIndexFormatter(7.5)
        self.assertEqual("7.5 high", testee.format())
        testee = UvIndexFormatter(7.6)
        self.assertEqual("7.6 very high", testee.format())
        testee = UvIndexFormatter(10.5)
        self.assertEqual("10.5 very high", testee.format())
        testee = UvIndexFormatter(10.6)
        self.assertEqual("10.6 extreme", testee.format())


class TestWindDirectionFormatter(unittest.TestCase):

    def test_none_wind_direction_compass_degrees(self):
        testee = WindDirectionFormatter(None)
        self.assertEqual("---°", testee.format(WindDirectionUnit.COMPASS_DEGREES))

    def test_non_none_wind_direction_compass_degrees(self):
        testee = WindDirectionFormatter(WindDirection(0))
        self.assertEqual("0°", testee.format(WindDirectionUnit.COMPASS_DEGREES))
        testee = WindDirectionFormatter(WindDirection(338))
        self.assertEqual("338°", testee.format(WindDirectionUnit.COMPASS_DEGREES))

    def test_none_wind_direction_cardinal_direction(self):
        testee = WindDirectionFormatter(None)
        self.assertEqual("---", testee.format(WindDirectionUnit.CARDINAL_DIRECTION))

    def test_non_none_wind_direction_cardinal_direction(self):
        testee = WindDirectionFormatter(WindDirection(0))
        self.assertEqual("N", testee.format(WindDirectionUnit.CARDINAL_DIRECTION))
        testee = WindDirectionFormatter(WindDirection(338))
        self.assertEqual("NNW", testee.format(WindDirectionUnit.CARDINAL_DIRECTION))


class TestWindSpeedFormatter(unittest.TestCase):

    def test_none_wind_speed_knots(self):
        testee = WindSpeedFormatter(None)
        self.assertEqual("--.- kts", testee.format(WindSpeedUnit.KNOTS))

    def test_non_none_wind_speed_knots(self):
        testee = WindSpeedFormatter(WindSpeed(0))
        self.assertEqual("0.0 kts", testee.format(WindSpeedUnit.KNOTS))
        testee = WindSpeedFormatter(WindSpeed(15.66))
        self.assertEqual("15.7 kts", testee.format(WindSpeedUnit.KNOTS))

    def test_none_wind_speed_metres_per_second(self):
        testee = WindSpeedFormatter(None)
        self.assertEqual("--.- m/s", testee.format(WindSpeedUnit.METRES_PER_SECOND))

    def test_non_none_wind_speed_metres_per_second(self):
        testee = WindSpeedFormatter(WindSpeed(0))
        self.assertEqual("0.0 m/s", testee.format(WindSpeedUnit.METRES_PER_SECOND))
        testee = WindSpeedFormatter(WindSpeed(14.5))  # == 7.459 m/s
        self.assertEqual("7.5 m/s", testee.format(WindSpeedUnit.METRES_PER_SECOND))

    def test_none_wind_speed_kilometres_per_hour(self):
        testee = WindSpeedFormatter(None)
        self.assertEqual("--.- kph", testee.format(WindSpeedUnit.KILOMETRES_PER_HOUR))

    def test_non_none_wind_speed_kilometres_per_hour(self):
        testee = WindSpeedFormatter(WindSpeed(0))
        self.assertEqual("0.0 kph", testee.format(WindSpeedUnit.KILOMETRES_PER_HOUR))
        testee = WindSpeedFormatter(WindSpeed(1))  # == 1.852 kph
        self.assertEqual("1.9 kph", testee.format(WindSpeedUnit.KILOMETRES_PER_HOUR))

    def test_none_wind_speed_miles_per_hour(self):
        testee = WindSpeedFormatter(None)
        self.assertEqual("--.- mph", testee.format(WindSpeedUnit.MILES_PER_HOUR))

    def test_non_none_wind_speed_miles_per_hour(self):
        testee = WindSpeedFormatter(WindSpeed(0))
        self.assertEqual("0.0 mph", testee.format(WindSpeedUnit.MILES_PER_HOUR))
        testee = WindSpeedFormatter(WindSpeed(13.55))  # == 15.593 mph
        self.assertEqual("15.6 mph", testee.format(WindSpeedUnit.MILES_PER_HOUR))

    def test_none_wind_speed_beaufort_scale(self):
        testee = WindSpeedFormatter(None)
        self.assertEqual("-- Bft", testee.format(WindSpeedUnit.BEAUFORT_SCALE))

    def test_non_none_beaufort_scale(self):
        testee = WindSpeedFormatter(WindSpeed(0))
        self.assertEqual("0 Bft", testee.format(WindSpeedUnit.BEAUFORT_SCALE))
        testee = WindSpeedFormatter(WindSpeed(64))
        self.assertEqual("12 Bft", testee.format(WindSpeedUnit.BEAUFORT_SCALE))

if __name__ == '__main__':
    unittest.main()
