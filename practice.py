# def log_getattribute(cls):
#     orig_getattribute = cls.__getattribute__
#
#     def new_getattribute(self, name):
#         print('getting', name)
#         return orig_getattribute(self, name)
#     cls.__getattribute__ = new_getattribute
#     return cls
#
# @log_getattribute
# class A:
#     def __init__(self, x):
#         self.x = x
#     def spam(self):
#         pass

class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting', name)
        return super().__getattribute__(name)

class A(LoggedGetattribute):
    def __init__(self, x):
        self.x = x
    def spam(self):
        pass

a = A(42)
print(a.x)
a.spam()
