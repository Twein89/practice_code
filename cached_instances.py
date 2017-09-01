# class Spam:
#     def __init__(self, name):
#         self.name = name
#
# import weakref
# _spam_cache = weakref.WeakValueDictionary()
#
# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name] = s
#     else:
#         s = _spam_cache[name]
#     return s
#
# a = get_spam('foo')
# b = get_spam('bar')
# c = get_spam('foo')
#
# l = list(_spam_cache)
# print(l)
# del a
# del c
# print(list(_spam_cache))
# del b
# print(list(_spam_cache))

import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]

    def clear(self):
        self._cache.clear()

class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

def get_spam(name):
    return Spam.manager.get_spam(name)

a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
print(a is c)
