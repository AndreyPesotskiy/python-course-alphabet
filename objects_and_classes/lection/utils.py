import inspect


def describe_object(name, obj):
    return f"{name} :  Type: {type(obj)}; Repr : {obj}; Id: {id(obj)} "


def print_me(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is called ")
        func(*args, **kwargs)
    return wrapper


def print_me_for_class(cls):
    for name, method in inspect.getmembers(cls, inspect.ismethod):
        setattr(cls, name, print_me(method))
    return cls