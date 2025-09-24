class Rational:
    def __init__(self,numerator, demonator):
        self.numerator = numerator
        self.demonator = demonator

    def __str__(self):
        return f"{self.numerator}/{self.demonator}"
    
    def __add__(self, right):
        """n1/d1 + n2/d2 = (n1d2 + n2d1)/d1d2"""
        n = self.numerator * right.demonator + right.numerator * self.demonator
        d = self.demonator * right.demonator
        return Rational(n,d)
    
    def __sub__(self,right):
        n = right.numerator * - 1
        return self + Rational(n,right.demonator)
    
    def __mul__(self, right):
        n = self.numerator * right.numerator
        d = self.demonator * right.demonator
        return Rational(n,d)
    
    def __div__(self, right):
        n = right.demonator
        d = right.numerator
        return self * Rational(n,d)
    
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            n1 = self.numerator * other.demonator
            n2 = other.numerator * self.demonator
            return n1 == n2