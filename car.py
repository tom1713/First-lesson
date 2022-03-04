

from asyncore import read
from turtle import update
from venv import create


class Car:
    def __init__(self, engin_number) -> None:
        self.__engin_number = engin_number
        self.__mark = None
        self.door_number = None
        self.color = None

    def set_engin_number(self, engin_number):
        self.__engin_number = engin_number

    def get_engin_number(self):
        return self.__engin_number


class BMW(Car):
    def __init__(self) -> None:
        self.__mark = "BMW"


class Toyota(Car):
    def __init__(self) -> None:
        self.__mark = "Toyota"


class Bens(Car):
    def __init__(self) -> None:
        self.__mark = "Bens"


# factory template
def manufacture(branch, engin_number):
    if "BMW":
        result = BMW()
        result.set_engin_number = 1111
        return result
    if "Toyota":
        result = Toyota()
        result.set_engin_number = 1111
        return result
    pass
