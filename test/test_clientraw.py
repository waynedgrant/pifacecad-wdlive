# Copyright 2014 Wayne D Grant (www.waynedgrant.com)

import unittest
from clientraw import ClientRaw
from measures import Trend
from units import RainfallUnit
from units import PressureUnit
from units import TemperatureUnit
from units import WindDirectionUnit
from units import WindSpeedUnit


class TestClientRaw(unittest.TestCase):

    #################################
    # Emptiness
    #################################
    def test_empty(self):
        testee = ClientRaw("")
        self.assertTrue(testee.is_empty())

    def test_non_empty(self):
        testee = ClientRaw("-")
        self.assertFalse(testee.is_empty())

    #################################
    # Header Validation
    #################################

    def test_header_field_populated_with_valid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HEADER, "12345"))
        self.assertTrue(testee.is_valid())

    def test_header_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HEADER, "54321"))
        self.assertFalse(testee.is_valid())

    def test_header_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HEADER))
        self.assertFalse(testee.is_valid())

    def test_no_field_for_header(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HEADER-1))
        self.assertFalse(testee.is_valid())

    #################################
    # Average Wind Speed
    #################################

    def test_average_wind_speed_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.AVERAGE_WIND_SPEED_KNOTS, "4.3"))
        self.assertEqual(4.3, testee.get_average_wind_speed().get_value(WindSpeedUnit.KNOTS))

    def test_average_wind_speed_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.AVERAGE_WIND_SPEED_KNOTS, "blah"))
        self.assertEqual(None, testee.get_average_wind_speed())

    def test_average_wind_speed_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.AVERAGE_WIND_SPEED_KNOTS))
        self.assertEqual(None, testee.get_average_wind_speed())

    def test_no_field_for_average_wind_speed(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.AVERAGE_WIND_SPEED_KNOTS-1))
        self.assertEqual(None, testee.get_average_wind_speed())

    #################################
    # Gust Speed
    #################################

    def test_gust_speed_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.GUST_SPEED_KNOTS, "5.8"))
        self.assertEqual(5.8, testee.get_gust_speed().get_value(WindSpeedUnit.KNOTS))

    def test_gust_speed_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.GUST_SPEED_KNOTS, "blah"))
        self.assertEqual(None, testee.get_gust_speed())

    def test_gust_speed_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.GUST_SPEED_KNOTS))
        self.assertEqual(None, testee.get_gust_speed())

    def test_no_field_for_gust_speed(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.GUST_SPEED_KNOTS-1))
        self.assertEqual(None, testee.get_gust_speed())

    #################################
    # Wind Direction
    #################################

    def test_wind_direction_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.WIND_DIRECTION_COMPASS_DEGREES, "128"))
        self.assertEqual(128, testee.get_wind_direction().get_value(WindDirectionUnit.COMPASS_DEGREES))

    def test_wind_direction_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.WIND_DIRECTION_COMPASS_DEGREES, "blah"))
        self.assertEqual(None, testee.get_wind_direction())

    def test_wind_direction_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.WIND_DIRECTION_COMPASS_DEGREES))
        self.assertEqual(None, testee.get_wind_direction())

    def test_no_field_for_wind_direction(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.WIND_DIRECTION_COMPASS_DEGREES-1))
        self.assertEqual(None, testee.get_wind_direction())

    #################################
    # Outdoor Temperature
    #################################

    def test_outdoor_temperature_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_CELSIUS, "-15.5"))
        self.assertEqual(-15.5, testee.get_outdoor_temperature().get_value(TemperatureUnit.CELSIUS))

    def test_outdoor_temperature_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_outdoor_temperature())

    def test_outdoor_temperature_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_CELSIUS))
        self.assertEqual(None, testee.get_outdoor_temperature())

    def test_no_field_for_outdoor_temperature(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_CELSIUS-1))
        self.assertEqual(None, testee.get_outdoor_temperature())

    #################################
    # Outdoor Humidity
    #################################

    def test_outdoor_humidity_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY, "79"))
        self.assertEqual(79, testee.get_outdoor_humidity())

    def test_outdoor_humidity_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY, "blah"))
        self.assertEqual(None, testee.get_outdoor_humidity())

    def test_outdoor_humidity_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY))
        self.assertEqual(None, testee.get_outdoor_humidity())

    def test_no_field_for_outdoor_humidity(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY-1))
        self.assertEqual(None, testee.get_outdoor_humidity())

    #################################
    # Surface Pressure
    #################################

    def test_surface_pressure_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_HECTOPASCALS, "1021.7"))
        self.assertEqual(1021.7, testee.get_surface_pressure().get_value(PressureUnit.HECTOPASCALS))

    def test_surface_pressure_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_HECTOPASCALS, "blah"))
        self.assertEqual(None, testee.get_surface_pressure())

    def test_surface_pressure_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.SURFACE_PRESSURE_HECTOPASCALS))
        self.assertEqual(None, testee.get_surface_pressure())

    def test_no_field_for_surface_pressure(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.SURFACE_PRESSURE_HECTOPASCALS-1))
        self.assertEqual(None, testee.get_surface_pressure())

    #################################
    # Daily Rainfall
    #################################

    def test_daily_rainfall_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.DAILY_RAINFALL_MILLIMETRES, "10.21"))
        self.assertEqual(10.21, testee.get_daily_rainfall().get_value(RainfallUnit.MILLIMETRES))

    def test_daily_rainfall_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.DAILY_RAINFALL_MILLIMETRES, "blah"))
        self.assertEqual(None, testee.get_daily_rainfall())

    def test_daily_rainfall_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.DAILY_RAINFALL_MILLIMETRES))
        self.assertEqual(None, testee.get_daily_rainfall())

    def test_no_field_for_daily_rainfall(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.DAILY_RAINFALL_MILLIMETRES-1))
        self.assertEqual(None, testee.get_daily_rainfall())

    #################################
    # Rainfall Rate
    #################################

    def test_rainfall_rate_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.RAINFALL_RATE_MILLIMETRES_PER_MINUTE, "0.12"))
        self.assertEqual(0.12, testee.get_rainfall_rate().get_value(RainfallUnit.MILLIMETRES))

    def test_rainfall_rate_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.RAINFALL_RATE_MILLIMETRES_PER_MINUTE, "blah"))
        self.assertEqual(None, testee.get_rainfall_rate())

    def test_rainfall_rate_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.RAINFALL_RATE_MILLIMETRES_PER_MINUTE))
        self.assertEqual(None, testee.get_rainfall_rate())

    def test_no_field_for_rainfall_rate(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.RAINFALL_RATE_MILLIMETRES_PER_MINUTE-1))
        self.assertEqual(None, testee.get_rainfall_rate())

    #################################
    # Indoor Temperature
    #################################

    def test_indoor_temperature_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.INDOOR_TEMPERATURE_CELSIUS, "18.9"))
        self.assertEqual(18.9, testee.get_indoor_temperature().get_value(TemperatureUnit.CELSIUS))

    def test_indoor_temperature_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.INDOOR_TEMPERATURE_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_indoor_temperature())

    def test_indoor_temperature_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.INDOOR_TEMPERATURE_CELSIUS))
        self.assertEqual(None, testee.get_indoor_temperature())

    def test_no_field_for_indoor_temperature(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.INDOOR_TEMPERATURE_CELSIUS-1))
        self.assertEqual(None, testee.get_indoor_temperature())

    #################################
    # Indoor Humidity
    #################################

    def test_indoor_humidity_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.INDOOR_HUMIDITY, "45"))
        self.assertEqual(45, testee.get_indoor_humidity())

    def test_indoor_humidity_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.INDOOR_HUMIDITY, "blah"))
        self.assertEqual(None, testee.get_indoor_humidity())

    def test_indoor_humidity_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.INDOOR_HUMIDITY))
        self.assertEqual(None, testee.get_indoor_humidity())

    def test_no_field_for_indoor_humidity(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.INDOOR_HUMIDITY-1))
        self.assertEqual(None, testee.get_indoor_humidity())

    #################################
    # Forecast
    #################################

    def test_forecast_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.FORECAST, "1"))
        self.assertEqual("Clear Night", testee.get_forecast())

    def test_forecast_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.FORECAST, "666"))
        self.assertEqual(None, testee.get_forecast())

    def test_forecast_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.FORECAST))
        self.assertEqual(None, testee.get_forecast())

    def test_no_field_for_forecast(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.FORECAST-1))
        self.assertEqual(None, testee.get_forecast())

    #################################
    # Hour
    #################################

    def test_hour_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HOUR, "23"))
        self.assertEqual(23, testee.get_hour())

    def test_hour_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HOUR, "blah"))
        self.assertEqual(None, testee.get_hour())

    def test_hour_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HOUR))
        self.assertEqual(None, testee.get_hour())

    def test_no_field_for_hour(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HOUR-1))
        self.assertEqual(None, testee.get_hour())

    #################################
    # Minute
    #################################

    def test_minute_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.MINUTE, "59"))
        self.assertEqual(59, testee.get_minute())

    def test_minute_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.MINUTE, "blah"))
        self.assertEqual(None, testee.get_minute())

    def test_minute_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.MINUTE))
        self.assertEqual(None, testee.get_minute())

    def test_no_field_for_minute(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.MINUTE-1))
        self.assertEqual(None, testee.get_minute())

    #################################
    # Wind Chill
    #################################

    def test_wind_chill_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.WIND_CHILL_CELSIUS, "-3.4"))
        self.assertEqual(-3.4, testee.get_wind_chill().get_value(TemperatureUnit.CELSIUS))

    def test_wind_chill_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.WIND_CHILL_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_wind_chill())

    def test_wind_chill_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.WIND_CHILL_CELSIUS))
        self.assertEqual(None, testee.get_wind_chill())

    def test_no_field_for_wind_chill(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.WIND_CHILL_CELSIUS-1))
        self.assertEqual(None, testee.get_wind_chill())

    #################################
    # Humidex
    #################################

    def test_humidex_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HUMIDEX_CELSIUS, "15.5"))
        self.assertEqual(15.5, testee.get_humidex().get_value(TemperatureUnit.CELSIUS))

    def test_humidex_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HUMIDEX_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_humidex())

    def test_humidex_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HUMIDEX_CELSIUS))
        self.assertEqual(None, testee.get_humidex())

    def test_no_field_for_humidex(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HUMIDEX_CELSIUS-1))
        self.assertEqual(None, testee.get_humidex())

    #################################
    # Surface Pressure Trend
    #################################

    def test_surface_pressure_trend_field_populated_rising(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND, "1.5"))
        self.assertEqual(Trend.RISING, testee.get_surface_pressure_trend())

    def test_surface_pressure_trend_field_populated_falling(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND, "-2.5"))
        self.assertEqual(Trend.FALLING, testee.get_surface_pressure_trend())

    def test_surface_pressure_trend_field_populated_steady(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND, "0"))
        self.assertEqual(Trend.STEADY, testee.get_surface_pressure_trend())

    def test_surface_pressure_trend_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND, "blah"))
        self.assertEqual(None, testee.get_surface_pressure_trend())

    def test_surface_pressure_trend_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND))
        self.assertEqual(None, testee.get_surface_pressure_trend())

    def test_no_field_for_surface_pressure_trend(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.SURFACE_PRESSURE_TREND-1))
        self.assertEqual(None, testee.get_surface_pressure_trend())

    #################################
    # Dew Point
    #################################

    def test_dew_point_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.DEW_POINT_CELSIUS, "-5.5"))
        self.assertEqual(-5.5, testee.get_dew_point().get_value(TemperatureUnit.CELSIUS))

    def test_dew_point_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.DEW_POINT_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_dew_point())

    def test_dew_point_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.DEW_POINT_CELSIUS))
        self.assertEqual(None, testee.get_dew_point())

    def test_no_field_for_dew_point(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.DEW_POINT_CELSIUS-1))
        self.assertEqual(None, testee.get_dew_point())

    #################################
    # UV Index
    #################################

    def test_uv_index_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.UV_INDEX, "5.1"))
        self.assertEqual(5.1, testee.get_uv_index())

    def test_uv_index_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.UV_INDEX, "blah"))
        self.assertEqual(None, testee.get_uv_index())

    def test_uv_index_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.UV_INDEX))
        self.assertEqual(None, testee.get_uv_index())

    def test_no_field_for_uv_index(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.UV_INDEX-1))
        self.assertEqual(None, testee.get_uv_index())

    #################################
    # Heat Index
    #################################

    def test_heat_index_field_populated(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HEAT_INDEX_CELSIUS, "16.5"))
        self.assertEqual(16.5, testee.get_heat_index().get_value(TemperatureUnit.CELSIUS))

    def test_heat_index_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.HEAT_INDEX_CELSIUS, "blah"))
        self.assertEqual(None, testee.get_heat_index())

    def test_heat_index_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HEAT_INDEX_CELSIUS))
        self.assertEqual(None, testee.get_heat_index())

    def test_no_field_for_heat_index(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.HEAT_INDEX_CELSIUS-1))
        self.assertEqual(None, testee.get_heat_index())

    #################################
    # Outdoor Temperature Trend
    #################################

    def test_outdoor_temperature_trend_field_populated_rising(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND, "1"))
        self.assertEqual(Trend.RISING, testee.get_outdoor_temperature_trend())

    def test_outdoor_temperature_trend_field_populated_falling(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND, "-1"))
        self.assertEqual(Trend.FALLING, testee.get_outdoor_temperature_trend())

    def test_outdoor_temperature_trend_field_populated_steady(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND, "0"))
        self.assertEqual(Trend.STEADY, testee.get_outdoor_temperature_trend())

    def test_outdoor_temperature_trend_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND, "blah"))
        self.assertEqual(None, testee.get_outdoor_temperature_trend())

    def test_outdoor_temperature_trend_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND))
        self.assertEqual(None, testee.get_outdoor_temperature_trend())

    def test_no_field_for_outdoor_temperature_trend(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_TEMPERATURE_TREND-1))
        self.assertEqual(None, testee.get_outdoor_temperature_trend())

    #################################
    # Outdoor Humidity Trend
    #################################

    def test_outdoor_humidity_trend_field_populated_rising(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND, "1"))
        self.assertEqual(Trend.RISING, testee.get_outdoor_humidity_trend())

    def test_outdoor_humidity_trend_field_populated_falling(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND, "-1"))
        self.assertEqual(Trend.FALLING, testee.get_outdoor_humidity_trend())

    def test_outdoor_humidity_trend_field_populated_steady(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND, "0"))
        self.assertEqual(Trend.STEADY, testee.get_outdoor_humidity_trend())

    def test_outdoor_humidity_trend_field_populated_with_invalid_value(self):
        testee = ClientRaw(self.__gen_populated_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND, "blah"))
        self.assertEqual(None, testee.get_outdoor_humidity_trend())

    def test_outdoor_humidity_trend_field_empty(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND))
        self.assertEqual(None, testee.get_outdoor_humidity_trend())

    def test_no_field_for_outdoor_humidity_trend(self):
        testee = ClientRaw(self.__gen_empty_client_raw_str(ClientRaw.OUTDOOR_HUMIDITY_TREND-1))
        self.assertEqual(None, testee.get_outdoor_humidity_trend())

    def __gen_populated_client_raw_str(self, position, value):
        if position > 0:
            return self.__gen_empty_client_raw_str(position-1) + " " + value
        else:
            return value

    def __gen_empty_client_raw_str(self, position):
        clientraw_string_list = []
        for i in range(0, position+1):
            clientraw_string_list.append("-")
        return ' '.join(clientraw_string_list)

if __name__ == '__main__':
    unittest.main()
