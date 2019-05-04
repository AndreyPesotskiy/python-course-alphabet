from copy import deepcopy

from lesson.some_data import DATA

import pickle


if __name__ == "__main__":
    # Lets dump object to pickle
    with open("data.txt", "wb") as file:
        pickle.dump(DATA, file)

    # Lets load it
    with open("data.txt", "rb") as file:
        restore_obj = pickle.load(file)
        print(restore_obj)

    # # Lets add set to pickle
    data_2 = set(range(15))
    with open("data_with_set.txt", "wb") as file:
        pickle.dump(data_2, file)

    # # Lets load it again
    with open("data_with_set.txt", "rb") as file:
        restore_obj = pickle.load(file)
        print(type(data_2), restore_obj)
