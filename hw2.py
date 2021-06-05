class Complex:

    def __init__(self, no1, no2, no3, no4):
        self.no1 = no1
        self.no2 = no2
        self.no3 = no3
        self.no4 = no4

    def __add__(self, other):
        _plus_ = self.no1 + other.no2 + self.no3 + other.no4
        return _plus_

    def __sub__(self, other):
        _sub_ = self.no1 - other.no2 - self.no3 - other.no4
        return _sub_

    def __mul__(self, other):
        _mul_ = self.no1 * other.no2 * self.no3 * other.no4
        return _mul_

    def __truediv__(self, other):
        _divi_ = self.no1 / other.no2 / self.no3 / other.no4
        return _divi_


k = complex(input('kod1: '))
a = complex(input('kod2: '))
d = complex(input('kod3: '))
y = complex(input('kod4: '))

complex = (k - a) + (d + y)
print(type(complex))
print(complex)





