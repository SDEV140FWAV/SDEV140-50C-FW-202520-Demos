import rational
def input_rational_number():
    try:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the demonator: "))
    except:
        return None
    return rational.Rational(n,d)

x = rational.Rational(1,3)
print(x)

y = rational.Rational(2,6)
print(y)

print(x + y)
print(x - y)
print(x == y)

z = None
while z == None:
    z = input_rational_number()
print(z)
#print(x + 2)
