class Fraction:

    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def add(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def sub(self, other):
        num = self.num - other.denum
        denum = self.denum - other.num
        print(num)
        print("-")
        print(denum)

    def div(self, other):
        num = self.num / other.denum
        denum = self.denum / other.num
        print(num)
        print("-")
        print(denum)

    def mul(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)


fraction = Fraction(2, 4)
fraction2 = Fraction(3, 5)
fraction.add(fraction2)
fraction2.sub(fraction)
fraction2.div(fraction)
fraction2.mul(fraction)
