from functools import wraps

class A:
    def decorate1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorate2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate 2')
            return func(*args, **kwargs)
        return wrapper

# as an instance method
a = A()
@a.decorate1
def spam():
    pass

# as an class method
@A.decorate2
def grok():
    pass

spam()
grok()
