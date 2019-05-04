from __future__ import annotations

import json
from typing import Dict, List


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Postion: {self.position} developer"

    @classmethod
    def from_json(cls, data):
        name = data['name']
        language = data['language']
        position = data['position']
        pr = Programmer(name=name, language=language, position=position)
        pr.enough_coffee = data.get('enough_coffee', False)
        return pr

    @staticmethod
    def to_json(obj: Programmer):
        data = {"name": obj.name, "language": obj.language, "position": obj.position}
        return data


def from_json(data):
    name = data['name']
    language = data['language']
    position = data['position']
    pr = Programmer(name=name, language=language, position=position)
    pr.enough_coffee = data.get('enough_coffee', False)
    return pr


def to_json(obj: Programmer):
    data = {"name": obj.name, "language": obj.language, "position": obj.position}
    return data


if __name__ == "__main__":
    programmer = Programmer("Flash")

    print(programmer)
    ser_pr = ''
    # Should raise TypeError. Json does not know how to work with custom objects
    try:
        ser_pr = json.dumps(programmer)
        print(ser_pr)
    except TypeError as e:
        print(e)

    # # Should work fine. Use custom json decoder
    try:
        ser_pr = json.dumps(programmer, default=to_json)
        print("Success")
        print(type(ser_pr), ser_pr)
    except TypeError as e:
        print(e)
    #
    # # Should not fault. But we will get dict instead of object
    try:
        load_pr = json.loads(ser_pr)
        print(type(load_pr), load_pr)
    except TypeError as e:
        print(e)
    #
    # # Should works fine. Use custom hook
    try:
        load_pr = json.loads(ser_pr, object_hook=from_json)
        print("Look here we have our programmer")
        print(type(load_pr), load_pr)
        print(load_pr.name)
    except TypeError as e:
        print(e)
