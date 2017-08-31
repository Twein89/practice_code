from time import localtime

class Date:
    def __init__(self, year, month, day):
        print('init:')
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        print('cls method:')
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

    @classmethod
    def json2date(cls, data):
        d = cls.__new__(cls)
        for key, value in data.items():
            setattr(d, key, value)
        return d

a = Date.today()
print(a.year)

data = {'year': 2012, 'month': 1, 'day': 2}
a = Date.json2date(data)
print(a.day)
