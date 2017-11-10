import inspect

#def simple_coroutine():
#    print('-> coroutine started')
#    x = yield
#    print('-> coroutine received:', x)
#
#my_coro = simple_coroutine()
#print(inspect.getgeneratorstate(my_coro))
#
#my_coro.send(None)
#print(inspect.getgeneratorstate(my_coro))
#
#next(my_coro)
#
#my_coro.send(42)
#print(inspect.getgeneratorstate(my_coro))

# def simple_coro2(a):
#     print('-> coroutine started: a=', a)
#     b = yield a
#     print('-> Received: b=', b)
#     c = yield a + b
#     print('-> Received: c=', c)
#
# my_coro2 = simple_coro2(14)
#
# print(inspect.getgeneratorstate(my_coro2))
#
# next(my_coro2)
# print(inspect.getgeneratorstate(my_coro2))
#
# my_coro2.send(28)
# print(inspect.getgeneratorstate(my_coro2))
#
# my_coro2.send(99)

from functools import wraps

def coroutinue(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutinue
def simple_coro(a):
    a = yield

my_coro3 = simple_coro(12)
my_coro3.send(3)

