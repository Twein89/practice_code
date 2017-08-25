from functools import wraps, partial
import time
import logging

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('countdown: ', end-start)
        return result

    return wrapper



def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        # @attach_wrapper(wrapper)
        # def get_level():
        #     return level
        wrapper.get_level = lambda: level
        return wrapper
    return decorate

def logged_adj(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.log.log(wrapper.level, wrapper.logmsg)
            return func(*args, **kwargs)

        wrapper.level = level
        wrapper.logmsg = logmsg
        wrapper.log = log
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

import logging
logging.basicConfig(level=logging.DEBUG)
# print(add(2, 3))
# add.set_message('Add called')
# print(add(2, 3))
# add.set_level(logging.WARNING)
# print(add(2, 3))

@timethis
@logged_adj(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1

#countdown(1000000)
#countdown.set_level(logging.WARNING)
#countdown.set_message('Counting down to zero')
#print(countdown.get_level())
#countdown(100000)

countdown(1000000)
#print(countdown.level)
countdown.level = logging.WARNING
countdown(1000000)
