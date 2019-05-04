import json


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
            # Let the base class default method raise the TypeError
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def json_hook(obj):
    if 'set' in obj:
        return set(obj)

    return obj
