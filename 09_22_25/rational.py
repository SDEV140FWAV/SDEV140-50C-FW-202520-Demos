class Rational:
    def __init__(self,numerator, demonator):
        self.numerator = numerator
        self.demonator = demonator
    def __add__(self,other):
        """n1/d1 + n2/d2 = (n1d2 + n2d1)/d1d2"""
        n = self.numerator*other.demonator + other.numerator * self.demonator
        d = self.demonator * other.demonator
        return Rational(n,d)
    def __str__(self):
        return f"{self.numerator}/{self.demonator}"
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.numerator == other.numerator and self.demonator == other.demonator
        

oneHalf = Rational(1,2)
oneSixth = Rational(1,6)
print(oneHalf)
print(oneHalf + oneSixth)
print(oneHalf == oneSixth)
print(oneHalf == .5)
print(oneHalf == oneHalf)
print(oneHalf is oneHalf)
print(oneHalf == Rational(1,2))