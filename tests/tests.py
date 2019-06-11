import unittest
from serialization.homework import (
    Car,
    Garage,
    Cesar,
    IncorrectValueException
)
import uuid
import json
import pickle
from os.path import isfile


def is_json(json_str):
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True


def is_pickle(pickle_str):
    try:
        pickle.loads(pickle_str)
    except ValueError:
        return False
    return True


car = Car(
    81.96,
    'Sedan',
    'BENTLEY',
    24.3,
)
register_id = uuid.uuid4()
garage = Garage(
    'Kiev',
    3,
    register_id,
    [car],
)
cesar = Cesar('cesar', [garage], register_id)


class TestCar(unittest.TestCase):
    car_json_file = './data/json/car.json'

    def test_car_init_error(self):
        with self.assertRaises(IncorrectValueException):
            Car(81.96, 'Cabriolet', 'LADA', 24.3)

    def test_car_eq(self):
        car_other = Car(
            81.96,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertEqual(car, car_other)

    def test_car_ne(self):
        car_other = Car(
            43.65,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertNotEqual(car, car_other)

    def test_car_gt(self):
        car_other = Car(
            43.65,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertGreater(car, car_other)

    def test_car_ge(self):
        car_other = Car(
            81.96,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertGreaterEqual(car, car_other)

    def test_car_lt(self):
        car_other = Car(
            120.41,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertLess(car, car_other)

    def test_car_le(self):
        car_other = Car(
            81.96,
            'Coupe',
            'BMW',
            52.1,
        )
        self.assertLessEqual(car, car_other)

    def test_car_change_number(self):
        car_number = car.number
        car.change_number()
        car_number_2 = car.number
        self.assertNotEqual(str(car_number), str(car_number_2))

    def test_car_to_json_str(self):
        self.assertTrue(is_json(car.to_json_str()))

    def test_car_instance_from_json_str(self):
        car_dict = {
            'price': 81.96,
            'type': 'Sedan',
            'producer': 'Buick',
            'mileage': 85.07,
            'number': str(uuid.uuid4())
        }
        self.assertIsInstance(
            car.instance_from_json_str(json.dumps(car_dict)),
            Car
        )

    def test_car_to_json_file(self):
        car.to_json_file(self.car_json_file)
        self.assertTrue(isfile(self.car_json_file))

    def test_car_instance_from_json_file(self):
        self.assertIsInstance(
            car.instance_from_json_file(self.car_json_file),
            Car
        )


class TestGarage(unittest.TestCase):
    garage_pickle_file = './data/pickle/garage.txt'

    def test_garage_init_error(self):
        with self.assertRaises(IncorrectValueException):
            Garage('Krivoy Rog', 2, uuid.uuid4())

    def test_garage_add_car(self):
        garage = Garage(
            'Kiev',
            1,
            uuid.uuid4()
        )
        garage.add(car)
        self.assertEqual(len(garage.cars), 1)

    def test_garage_add_car_error(self):
        garage = Garage(
            'Kiev',
            1,
            uuid.uuid4(),
            [car],
        )
        car_other = Car(
            120.41,
            'Coupe',
            'BMW',
            52.1,
        )
        with self.assertRaises(IncorrectValueException):
            garage.add(car_other)

    def test_garage_remove_car(self):
        garage = Garage(
            'Kiev',
            3,
            uuid.uuid4(),
            [car]
        )
        garage.remove(car)
        self.assertEqual(len(garage.cars), 0)

    def test_garage_hit_hat(self):
        self.assertEqual(garage.hit_hat(), 81.96)

    def test_garage_exist_car(self):
        self.assertTrue(garage.exist_car(car))

    def test_garage_to_pickle_str(self):
        self.assertTrue(is_pickle(garage.to_pickle_str()))

    def test_garage_instance_from_pickle_str(self):
        garage_dict = {
            'town': 'Kiev',
            'places': 3,
        }
        self.assertIsInstance(
            garage.instance_from_pickle_str(pickle.dumps(garage_dict)),
            Garage
        )

    def test_garage_to_pickle_file(self):
        garage.to_pickle_file(self.garage_pickle_file)
        self.assertTrue(isfile(self.garage_pickle_file))

    def test_garage_instance_from_pickle_file(self):
        self.assertIsInstance(
            garage.instance_from_pickle_file(self.garage_pickle_file),
            Garage
        )


class TestCesar(unittest.TestCase):
    cesar_yaml_file = './data/yaml/cesar.yaml'

    def test_cesar_hit_hat(self):
        self.assertEqual(cesar.hit_hat(), 81.96)

    def test_cesar_garages_count(self):
        self.assertEqual(cesar.garages_count(), 1)

    def test_cesar_cars_count(self):
        self.assertEqual(cesar.cars_count(), 1)

    def test_cesar_add_car(self):
        register_id = uuid.uuid4()
        garage = Garage(
            'Rome',
            2,
            register_id,
        )
        cesar = Cesar('Qwerty', [garage], register_id)
        cesar.add_car(car, garage)
        self.assertEqual(cesar.cars_count(), 1)

    def test_cesar_eq(self):
        cesar_other = Cesar(
            'Griffin',
            [garage]
        )
        self.assertEqual(cesar, cesar_other)

    def test_cesar_ne(self):
        cesar_other = Cesar(
            'Griffin',
        )
        self.assertNotEqual(cesar, cesar_other)

    def test_cesar_gt(self):
        cesar_other = Cesar(
            'Griffin',
        )
        self.assertGreater(cesar, cesar_other)

    def test_cesar_ge(self):
        cesar_other = Cesar(
            'Griffin',
            [garage]
        )
        self.assertGreaterEqual(cesar, cesar_other)

    def test_cesar_lt(self):
        cesar_other = Cesar(
            'Griffin',
        )
        self.assertLess(cesar_other, cesar)

    def test_cesar_le(self):
        cesar_other = Cesar(
            'Griffin',
            [garage]
        )
        self.assertLessEqual(cesar_other, cesar)

    def test_cesar_to_yaml_file(self):
        cesar.to_yaml_file(self.cesar_yaml_file)
        self.assertTrue(isfile(self.cesar_yaml_file))

    def test_cesar_instance_from_yaml_file(self):
        self.assertIsInstance(
            cesar.instance_from_yaml_file(self.cesar_yaml_file),
            Cesar
        )
