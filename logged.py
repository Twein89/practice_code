from functools import wraps
import logging

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            log.log(level, logmsg)
            return r
        return wrapper
    return decorate

@logged(logging.INFO, message='add success')
def add(x, y):
    return x + y


logging.basicConfig(level=logging.DEBUG)
add(1, 2)
