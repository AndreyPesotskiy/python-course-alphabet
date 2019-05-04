class Animal:
    def __init__(self, age):
        self.age = age

    def run(self):
        return "run"


class Bird:
    def fly(self):
        return "I can fly"

    def run(self):
        return "I can't run"


class B(Animal, Bird):
    def run(self):
        return super().run()


cow = Animal(12)

b = B(14)


# print(b.run())


class Figure:
    def draw(self, length):
        return self.__draw_line_size(length)

    def __draw_line_size(self, length):
        return f"our line is such {length}"


fig1 = Figure()


# print(fig1.draw(12))


class Cat:
    def speak(self):
        return "Meow"


class Dog:
    def speak(self):
        return "Wof"


class Cow:
    def speak(self):
        return "Moo"


cat = Cat()
dog = Dog()
cow1 = Cow()


# print(cat.speak(), dog.speak(), cow1.speak())


class A:
    def __init__(self, param):
        self.param = param

    def get_param(self):
        return self.param


class B:
    def create_another_class(self, param):
        result = A(param)
        print(result.get_param())
        return result


# b1 = B()
# b1.create_another_class(12)


from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def important_method(self):
        return "Parent method action"

    @property
    @abstractmethod
    def a(self):
        pass


class ChildAbstractClass(AbstractClass):
    a = 10

    def important_method(self):
        return super().important_method()


ch1 = ChildAbstractClass()
print(ch1.important_method())


class Car:
    def get_speed(self):
        return 12


class SuperCar:
    def get_speed(self):
        return 100


class Truck(Car, SuperCar):
    def get_speed(self):
        return "My speed is %s " % 12


track1 = Truck()
