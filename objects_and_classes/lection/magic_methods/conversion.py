from __future__ import annotations


class AwesomeNumber:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __index__(self):
        return int(self.value)

    def __eq__(self, other: AwesomeNumber):
        return other.value == self.value

    def __le__(self, other: AwesomeNumber):
        return self.value <= other.value

    def __lt__(self, other: AwesomeNumber):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value


class AwesomeString:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)


if __name__ == "__main__":
    number = AwesomeNumber(2)
    default_int = int(2)
    print(number)
    print(default_int)
    # Slices
    some_list = ["Den", "Alex", "Vitalka", "Oksana"]
    print(some_list[number])

    # Comparing values
    first_number = AwesomeNumber(2)
    second_number = AwesomeNumber(9)

    print(first_number > second_number)
