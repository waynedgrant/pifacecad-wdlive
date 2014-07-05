# Copyright 2014 Wayne D Grant (www.waynedgrant.com)


class Cyclical:

    def __init__(self, items):
        if items is None:
            raise RuntimeError('items cannot be None')
        if len(items) == 0:
            raise RuntimeError('items must contain at least one item')
        self.__items = items
        self.__current = 0

    def current(self):
        return self.__items[self.__current]

    def next(self):
        self.__current += 1
        if self.__current >= len(self.__items):
            self.__current = 0

    def previous(self):
        self.__current -= 1
        if self.__current < 0:
            self.__current = len(self.__items)-1
