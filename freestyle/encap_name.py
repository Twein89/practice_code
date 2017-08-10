class A:
    def __init__(self):
        self._internal = 0

    def public_method(self):
        pass

    def _internal_method(self):
        pass

class B:
    def __init__(self):
        self.__private = 0

    def __private_metchod(self):
        pass

    def public_metchod(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        pass


c = C()
print(dir(c))
