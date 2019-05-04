from pprint import pprint
from copy import deepcopy
from lesson.json_example.json_utils import JsonEncoder, json_hook
import json

from lesson.some_data import DATA


def show_me(data: dict) -> None:
    for key, value in data.items():
        pprint(f"Key {key}; Type : {type(value)}; Value : {value}")


def print_separator() -> None:
    print("\n" * 3)
    print("-" * 20)


if __name__ == "__main__":
    # Lets see what we have in DATA
    print("GIVEN DATA")
    # show_me(DATA)
    print(type(DATA))
    print_separator()
    # Lets see how json like string will look like
    json_formatted_str = json.dumps(DATA)
    print("JSON formatted string")
    print(type(json_formatted_str), json_formatted_str)
    print_separator()

    restored_data = eval(json_formatted_str)

    print(type(restored_data))
    print_separator()

    # Lets dump json data to file
    with open("data.json", 'w') as file:
        json.dump(DATA, file)

    print_separator()
    # # Lets save json data with params
    with open("formatted_data.json", 'w') as file:
        json.dump(DATA, file, indent=4)

    with open("formatted_data.json", 'r') as file:
        restored_data = json.load(file)
        print(restored_data)
    #
    # # Lets see restored data from string
    restored_data = json.loads(json_formatted_str)
    print("Restored data")
    show_me(restored_data)
    print_separator()
    #
    # # Lets add not serializable type
    data_2 = deepcopy(DATA)
    data_2['set'] = set(range(10))
    #
    print_separator()
    print("Serialized data")
    data_as_string = ""
    try:
        data_as_string = json.dumps(data_2)
    except TypeError as e:
        print(e)
    #
    try:
        data_as_string = json.dumps(data_2, cls=JsonEncoder)
    except TypeError as e:
        print(e)
    else:
        print(data_as_string)
    #
    print_separator()
    # # Without hook
    restored_data = json.loads(data_as_string)

    # # With hook
    print_separator()
    print("With hook")
    restored_data_with_hook = json.loads(data_as_string, object_hook=json_hook)
    print("Something")
