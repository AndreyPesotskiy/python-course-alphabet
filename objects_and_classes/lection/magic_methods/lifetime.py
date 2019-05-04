import time

from lection.utils import describe_object


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        # print("Fill out programmer with attributes")
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __new__(cls, *args, **kwargs):
        """
        This methods calls when object is created.
        When new instance if class is created this method is called and return instance

        Returns:
            instance of class
        """

        # print("We create new object that will be map as programmer")
        print("We create new object that will be map as programmer")
        obj = super(Programmer, cls).__new__(cls)
        return obj

    def __enter__(self):
        # print("Get coffee for programmer")
        self.enough_coffee = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("Bring back coffee from this animal")
        self.enough_coffee = False
    #
    # def __del__(self):
    #     print(f"Programmer go to sleep")

    def work(self):
        if not self.enough_coffee:
            print(f"{self.name} need coffee")
            return

        for _ in range(10):
            time.sleep(1)
            print(f" {self.name} is working")

    # def __str__(self):
    #     """
    #     Main goal of __str__ is to be readable
    #     Returns:
    #         Readable string
    #     """
    #     return f"Hello. My name is {self.name} and I am {self.language} {self.position} developer"
    #
    # def __repr__(self):
    #     # C type variant
    #     # return f"{self.__module__}.{type(self)} object at {hex(id(self))}>"
    #     # Variant with eval
    #     return f"Programmer(name='{self.name}')"


if __name__ == "__main__":
    # Create instance of Programmer
    programmer = Programmer(name="Anton")
    # print("Before", programmer.enough_coffee)
    # programmer.work()
    # with programmer:
    #     # our code
    #     programmer.work()
    #     print("Until", programmer.enough_coffee)

    # print("After", programmer.enough_coffee)

    # Lets look what it have
    # print(describe_object("programmer", programmer))

    # Lets see how it is converted to string
    print(str(programmer))
    print(f"{programmer}")
    print(programmer)

    # Lets see repr
    res = repr(programmer)
    print(res)
    # recover_programmer = eval(res)
    # print(recover_programmer.language)
    # print(programmer.position)