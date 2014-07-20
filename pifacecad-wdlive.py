# Copyright 2014 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

import pifacecad
import sys
import threading
import time
import urllib.request
import urllib.error
from clientraw import ClientRaw
from settings import Settings
from weatheritems import WeatherItemFactory

UPDATE_TIME_SECS = 60

DEGREE_BITMAP = 0
RISING_BITMAP = 1
FALLING_BITMAP = 2
STEADY_BITMAP = 3

BUTTON_1_PRESSED = 0
BUTTON_2_PRESSED = 1
BUTTON_3_PRESSED = 2
BUTTON_4_PRESSED = 3
BUTTON_5_PRESSED = 4
TOGGLE_PRESSED = 5
TOGGLE_LEFT = 6
TOGGLE_RIGHT = 7

settings = Settings()
clientraw = None


def setup_bitmaps():
    degree = pifacecad.LCDBitmap([0b01110, 0b01010, 0b01110, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000])
    cad.lcd.store_custom_bitmap(DEGREE_BITMAP, degree)

    rising = pifacecad.LCDBitmap([0b00000, 0b01111, 0b00011, 0b00101, 0b01001, 0b10000, 0b00000, 0b00000])
    cad.lcd.store_custom_bitmap(RISING_BITMAP, rising)

    falling = pifacecad.LCDBitmap([0b00000, 0b10000, 0b01001, 0b00101, 0b00011, 0b01111, 0b00000, 0b00000])
    cad.lcd.store_custom_bitmap(FALLING_BITMAP, falling)

    steady = pifacecad.LCDBitmap([0b00000, 0b00100, 0b00010, 0b11111, 0b00010, 0b00100, 0b00000, 0b00000])
    cad.lcd.store_custom_bitmap(STEADY_BITMAP, steady)


def setup_switch_listeners():
    switch_listener = pifacecad.SwitchEventListener(chip=cad)
    switch_listener.register(TOGGLE_PRESSED, pifacecad.IODIR_ON, toggle_backlight)
    switch_listener.register(TOGGLE_LEFT, pifacecad.IODIR_ON, previous_weather_item)
    switch_listener.register(TOGGLE_RIGHT, pifacecad.IODIR_ON, next_weather_item)
    switch_listener.register(BUTTON_1_PRESSED, pifacecad.IODIR_ON, change_temperature_unit)
    switch_listener.register(BUTTON_2_PRESSED, pifacecad.IODIR_ON, change_pressure_unit)
    switch_listener.register(BUTTON_3_PRESSED, pifacecad.IODIR_ON, change_wind_speed_unit)
    switch_listener.register(BUTTON_4_PRESSED, pifacecad.IODIR_ON, change_wind_direction_unit)
    switch_listener.register(BUTTON_5_PRESSED, pifacecad.IODIR_ON, change_rainfall_unit)
    switch_listener.activate()


def setup_remote_listeners():
    remote_listener = pifacecad.IREventListener(prog="pifacecad-wdlive")
    remote_listener.register("toggle_backlight", toggle_backlight)
    remote_listener.register("previous_weather_item", previous_weather_item)
    remote_listener.register("next_weather_item", next_weather_item)
    remote_listener.register("change_temperature_unit", change_temperature_unit)
    remote_listener.register("change_pressure_unit", change_pressure_unit)
    remote_listener.register("change_wind_speed_unit", change_wind_speed_unit)
    remote_listener.register("change_wind_direction_unit", change_wind_direction_unit)
    remote_listener.register("change_rainfall_unit", change_rainfall_unit)
    remote_listener.activate()


def toggle_backlight(event=None):
    global backlight_on
    if backlight_on:
        backlight_on = False
        cad.lcd.backlight_off()
    else:
        backlight_on = True
        cad.lcd.backlight_on()


def previous_weather_item(event):
    settings.previous_weather_item_type()
    update_display()


def next_weather_item(event):
    settings.next_weather_item_type()
    update_display()


def change_temperature_unit(event):
    settings.change_temperature_unit()
    update_display()


def change_pressure_unit(event):
    settings.change_pressure_unit()
    update_display()


def change_wind_speed_unit(event):
    settings.change_wind_speed_unit()
    update_display()


def change_wind_direction_unit(event):
    settings.change_wind_direction_unit()
    update_display()


def change_rainfall_unit(event):
    settings.change_rainfall_unit()
    update_display()


def fetch_clientraw():
    global clientraw
    try:
        response = urllib.request.urlopen(clientraw_url)
    except urllib.error.URLError:
        clientraw = None
    else:
        content = response.read().decode("UTF-8")
        clientraw = ClientRaw(content)


def update_display():
    if clientraw is None:
        display_message("CLIENTRAW IS\nUNAVAILABLE")
    elif clientraw.is_empty():
        display_message("CLIENTRAW IS\nEMPTY")
    elif not clientraw.is_valid():
        display_message("CLIENTRAW IS\nINVALID")
    else:
        display_weather_item(WeatherItemFactory(clientraw, settings).get_weather_item())


def setup_display():
    global cad, backlight_on
    cad = pifacecad.PiFaceCAD()
    cad.lcd.blink_off()
    cad.lcd.cursor_off()
    cad.lcd.backlight_off()
    backlight_on = False


def display_startup_message():
    toggle_backlight()
    display_message("** PIFACECAD **\n**  WDLIVE   **")
    time.sleep(3)
    toggle_backlight()


def display_weather_item(weather_item):
    display_lock.acquire()
    cad.lcd.clear()
    display_line(weather_item.get_line1())
    cad.lcd.write("\n")
    display_line(weather_item.get_line2())
    display_lock.release()


def display_line(line):
    for c in line:
        if c == "°":
            display_bitmap(DEGREE_BITMAP)
        elif c == "➚":
            display_bitmap(RISING_BITMAP)
        elif c == "➙":
            display_bitmap(STEADY_BITMAP)
        elif c == "➘":
            display_bitmap(FALLING_BITMAP)
        else:
            cad.lcd.write(c)


def display_bitmap(bitmap):
    cad.lcd.write_custom_bitmap(bitmap)


def display_message(message):
    display_lock.acquire()
    cad.lcd.clear()
    cad.lcd.write(message)
    display_lock.release()


if __name__ == '__main__':

    display_lock = threading.Lock()

    setup_display()
    display_startup_message()

    if len(sys.argv) < 2:
        display_message("CLIENTRAW URL\nREQUIRED")
        sys.exit(1)

    clientraw_url = sys.argv[1]
    setup_bitmaps()
    setup_switch_listeners()
    setup_remote_listeners()

    while True:
        display_message("UPDATING...")
        fetch_clientraw()
        update_display()
        time.sleep(UPDATE_TIME_SECS)
