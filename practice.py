from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

# class Structure:
#     __signature__ = make_sig()
#     def __init__(self, *args, **kwargs):
#         bound_values = self.__signature__.bind(*args, **kwargs)
#         for name, value in bound_values.arguments.items():
#             setattr(self, name, value)
#
# class Stock(Structure):
#     __signature__ = make_sig('name', 'shares', 'price')
#
# class Point(Structure):
#     __signature__ = make_sig('x', 'y')
#
# import inspect
# print(inspect.signature(Stock))
#
# s1 = Stock('ACME', 100, 490.1)
# # s2 = Stock('ACME', 100)
# s3 = Stock('ACME', 100, 490.1, shares=50)

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

import inspect

print(inspect.signature(Stock))
print(inspect.signature(Point))
