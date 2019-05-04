from functools import wraps


def my_decorator(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func.__dict__)
        new_args = [x + 1 for x in args]
        if len(args) < 5:
            raise TypeError
        print("Something is happening before the function is called.")
        res = func(*new_args, **kwargs)
        print(res)
        print("Something is happening after the function is called.")
        return res
    return wrapper


@my_decorator
def our_awesome_function(*args, **kwargs):
    print("Call our function")
    print(*args)
    print("End of our function")


our_awesome_function(*range(10))