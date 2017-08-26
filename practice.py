from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument is already defined')
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling: ', func.__name__)
        return func(*args, **kwargs)
    sig = inspect.signature(func)
    parms = list(sig.parameters)
    return wrapper

# @optional_debug
# def spam(x, y, z):
#     print(x, y, z)
#
# spam(1, 2, 3)
# spam(1, 2, {'a': 1, 'b': 2}, debug=True)

@optional_debug
def add(x, y):
    return x + y

print(inspect.signature(add))
