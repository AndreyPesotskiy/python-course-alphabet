from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import uuid
from typing import List

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
class IncorrectValueException(Exception):
    pass

class Helper:
    @staticmethod
    def value_in_list_without_case(value: str, data: List[str]):
        return value.lower() in [item.lower() for item in data]

class Car:
    def __init__(self, price: float, type: CARS_TYPES, producer: CARS_PRODUCER, mileage: float):
        self.price = float(price)
        self.mileage = float(mileage)
        self.number = uuid.uuid4()

        if Helper.value_in_list_without_case(type, CARS_TYPES):
            self.type = type
        else:
            raise IncorrectValueException('Type expected one of CARS_TYPES.')
        if Helper.value_in_list_without_case(producer, CARS_PRODUCER):
            self.producer = producer
        else:
            raise IncorrectValueException('Producer expected one of CARS_PRODUCER.')

    def __repr__(self):
        return f"Car: price - {car.price}, type - {car.type}, producer - {car.producer}, mileage - {car.mileage}"

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def change_number(self):
        self.number = uuid.uuid4()


class Garage:
    def __init__(self, town: TOWNS, places: int, owner=None, cars=list()):
        if Helper.value_in_list_without_case(town, TOWNS):
            self.town = town
        else:
            raise IncorrectValueException('Town expected one of TOWNS.')
        self.places = int(places)
        self.owner = owner
        self.cars = cars

    def add(self, car: Car):
        if len(self.cars) < self.places and not self.exist_car(car):
            self.cars.append(car)
        elif self.exist_car(car):
            raise IncorrectValueException('This car is already in the garage.')
        else:
            raise IncorrectValueException('There are no empty seats.')

    def remove(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)

    def hit_hat(self):
        return sum(map(lambda car: car.price, self.cars))

    def exist_car(self, car: Car):
        return car.number in (item.number for item in self.cars)


class Cesar:
    def __init__(self, name: str, garages=None):
        self.name = name
        self.garages = garages if garages is not None else []
        self.register_id = uuid.uuid4()

    def hit_hat(self):
        return sum(garage.hit_hat() for garage in self.garages)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(len(garage.cars) for garage in self.garages)

    def add_car(self, car: Car, garage=None):
        if garage:
            garage.add(car)
        elif self.garages:
            max(self.garages, key=lambda garage: garage.places - len(garage.cars)).add(car)

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()
