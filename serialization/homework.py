"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from typing import List, Dict
import json
from ruamel.yaml import YAML
import pickle
from abc import ABC, abstractmethod
import uuid
import random


class IncorrectValueException(Exception):
    pass


class Helper:
    @staticmethod
    def value_in_list_without_case(value: str, data: List[str]):
        return value.lower() in [item.lower() for item in data]


class Serialization(ABC):
    yaml = YAML()

    @classmethod
    def instance_from_json_file(cls, file_path):
        with open(file_path, 'r') as read_file:
            data = json.load(read_file)
            return cls.instance_from_dict(data)

    @classmethod
    def instance_from_yaml_file(cls, file_path):
        with open(file_path, 'r') as read_file:
            data = cls.yaml.load(read_file)
            return cls.instance_from_dict(data)

    @classmethod
    def instance_from_pickle_file(cls, file_path):
        with open(file_path, 'rb') as read_file:
            data = pickle.load(read_file)
            return cls.instance_from_dict(data)

    @classmethod
    def instance_from_json_str(cls, value: str):
        data = json.loads(value)
        return cls.instance_from_dict(data)

    @classmethod
    def instance_from_pickle_str(cls, value: str):
        data = pickle.loads(value)
        return cls.instance_from_dict(data)

    def to_json_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file)

    def to_yaml_file(self, file_path):
        with open(file_path, 'w') as file:
            self.yaml.dump(self.to_dict(), file)

    def to_pickle_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.to_dict(), file)

    def to_json_str(self):
        return json.dumps(self.to_dict())

    def to_pickle_str(self):
        return pickle.dumps(self.to_dict())

    @classmethod
    @abstractmethod
    def instance_from_dict(cls, data: Dict):
        pass

    @abstractmethod
    def to_dict(self):
        pass


class Car(Serialization):
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
        return f"Car: price - {self.price}, type - {self.type}, producer - {self.producer}, mileage - {self.mileage}"

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

    @classmethod
    def instance_from_dict(cls, data: Dict):
        return cls(data.get('price'), data.get('type'), data.get('producer'), data.get('mileage'))

    def to_dict(self):
        return {
            'price': self.price,
            'type': self.type,
            'producer': self.producer,
            'mileage': self.mileage,
        }


class Garage(Serialization):
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

    def __repr__(self):
        return f"Garage: town - {self.town}, places - {self.places}, owner - {self.owner}, cars - {self.cars}"

    @classmethod
    def instance_from_dict(cls, data: Dict):
        cars_data = data.get('cars', [])
        cars = []
        if cars_data:
            cars = [Car(car.get('price'), car.get('type'), car.get('producer'), car.get('mileage')) for car
                    in
                    cars_data]

        return cls(data.get('town'), data.get('places'), data.get('owner'), cars)

    def to_dict(self):
        return {
            'town': self.town,
            'places': self.places,
            'owner': str(self.owner),
            'cars': [car.to_dict() for car in self.cars] if self.cars else [],
        }


class Cesar(Serialization):
    def __init__(self, name: str, garages=None, register_id=None):
        self.name = name
        self.garages = garages if garages is not None else []
        self.register_id = register_id if isinstance(register_id, uuid.UUID) else uuid.uuid4()

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

    def __repr__(self):
        return f"Cesar: name - {self.name}, register_id - {self.register_id}, garages - {self.garages}"

    @classmethod
    def instance_from_dict(cls, data: Dict):
        garage_data = data.get('garages', [])
        garages = []
        if garage_data:
            for garage in garage_data:
                cars_data = garage.get('cars', [])
                cars = []
                if cars_data:
                    cars = [Car(car.get('price'), car.get('type'), car.get('producer'), car.get('mileage')) for car
                            in cars_data]
                garages.append(Garage(garage.get('town'), garage.get('places'), garage.get('owner'), cars))

        return cls(data.get('name'), garages)

    def to_dict(self):
        return {
            'name': self.name,
            'register_id': str(self.register_id),
            'garages': [garage.to_dict() for garage in self.garages] if self.garages else [],
        }


if __name__ == "__main__":
    car = Car(
        round(random.uniform(1, 100), 2),
        random.choice(CARS_TYPES),
        random.choice(CARS_PRODUCER),
        round(random.uniform(1, 100), 2),
    )

    register_id = uuid.uuid4()
    garage = Garage(
        random.choice(TOWNS),
        3,
        register_id,
        [car],
    )

    cesar = Cesar('cesar', [garage], register_id)

    # json
    car_json_str = car.to_json_str()
    garage_json_str = garage.to_json_str()
    cesar_json_str = cesar.to_json_str()
    print(car_json_str)
    print(garage_json_str)
    print(cesar_json_str)

    print('-' * 50)

    new_car = car.instance_from_json_str(car_json_str)
    new_garage = garage.instance_from_json_str(garage_json_str)
    new_cesar = cesar.instance_from_json_str(cesar_json_str)
    print(new_car)
    print(new_garage)
    print(new_cesar)

    print('-' * 50)

    # pickle
    car_pickle_str = car.to_pickle_str()
    garage_pickle_str = garage.to_pickle_str()
    cesar_pickle_str = cesar.to_pickle_str()
    print(car_pickle_str)
    print(garage_pickle_str)
    print(cesar_pickle_str)

    print('-' * 50)

    new_car = car.instance_from_pickle_str(car_pickle_str)
    new_garage = garage.instance_from_pickle_str(garage_pickle_str)
    new_cesar = cesar.instance_from_pickle_str(cesar_pickle_str)
    print(new_car)
    print(new_garage)
    print(new_cesar)

    # to files
    car.to_json_file('./data/json/car.json')
    garage.to_json_file('./data/json/garage.json')
    cesar.to_json_file('./data/json/cesar.json')

    car.to_yaml_file('./data/yaml/car.yaml')
    garage.to_yaml_file('./data/yaml/garage.yaml')
    cesar.to_yaml_file('./data/yaml/cesar.yaml')

    car.to_pickle_file('./data/pickle/car.txt')
    garage.to_pickle_file('./data/pickle/garage.txt')
    cesar.to_pickle_file('./data/pickle/cesar.txt')

    print('-' * 50)

    # from files
    car_from_json_file = car.instance_from_json_file('./data/json/car.json')
    garage_from_json_file = garage.instance_from_json_file('./data/json/garage.json')
    cesar_from_json_file = cesar.instance_from_json_file('./data/json/cesar.json')
    print(car_from_json_file)
    print(garage_from_json_file)
    print(cesar_from_json_file)

    print('-' * 50)

    car_from_yaml_file = car.instance_from_yaml_file('./data/yaml/car.yaml')
    garage_from_yaml_file = garage.instance_from_yaml_file('./data/yaml/garage.yaml')
    cesar_from_yaml_file = cesar.instance_from_yaml_file('./data/yaml/cesar.yaml')
    print(car_from_yaml_file)
    print(garage_from_yaml_file)
    print(cesar_from_yaml_file)

    print('-' * 50)

    car_from_pickle_file = car.instance_from_pickle_file('./data/pickle/car.txt')
    garage_from_pickle_file = garage.instance_from_pickle_file('./data/pickle/garage.txt')
    cesar_from_pickle_file = cesar.instance_from_pickle_file('./data/pickle/cesar.txt')
    print(car_from_pickle_file)
    print(garage_from_pickle_file)
    print(cesar_from_pickle_file)
