from math import gcd

class Rational:
    def __init__(self,numerator, demonator):
        i = 0
        if type(i) != type(numerator):
            raise TypeError("Numerator is not an int type")
        if type(i) != type(demonator):
            raise TypeError("Demonator is not an int type")
        if demonator == 0:
            raise ZeroDivisionError("Demonator cannot be 0")
        
        self.numerator = numerator
        self.demonator = demonator

    def __str__(self):
        return f"{self.numerator}/{self.demonator}"
    
    def __add__(self, right):
        """n1/d1 + n2/d2 = (n1d2 + n2d1)/d1d2"""
        n = self.numerator * right.demonator + right.numerator * self.demonator
        d = self.demonator * right.demonator
        x = gcd(n,d)
        n = n // x
        d = d // x
        return Rational(n,d)
    
    def __sub__(self,right):
        n = right.numerator * - 1
        return self + Rational(n,right.demonator)
    
    def __mul__(self, right):
        n = self.numerator * right.numerator
        d = self.demonator * right.demonator
        x = gcd(n,d)
        n = n // x
        d = d // x
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