from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                                'Argument {} must be {}'.format(name, bound_types[name])
                                )
            return func(*args, **kwargs)
        return wrapper
    return decorate


# @typeassert(int, float, z=int)
# def spam(x, y, z=42):
#     print(x, y, z)

# spam(1, 2, 3)
#
# spam(1, 'hello', 3)
#
# spam(1, 'hello', 'world')

# def spam(x, y, z=42):
#     pass
# sig = signature(spam)
# bound_types = sig.bind_partial(int, z=int)
# print(bound_types.arguments)
# bound_values = sig.bind(1, 2, 3)
# print(bound_values.arguments)
# for name, value in bound_values.arguments.items():
#     if name in bound_types.arguments:
#         if not isinstance(value, bound_types.arguments[name]):
#             raise TypeError()


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = ''
    items.append(x)
    return items

print(bar(2, 3))
