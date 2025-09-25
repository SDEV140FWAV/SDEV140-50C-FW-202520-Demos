import rational
def input_rational_number():
    n = int(input("Enter the numerator: "))
    d = int(input("Enter the demonator: "))
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
    try:
        z = input_rational_number()
    except ValueError as err:
        print(err)
        print("Non-integer input detected.")
        print("Please try again")
    except ZeroDivisionError as err:
        print(err)
        print("Please try again")
print(z)
#print(x + 2)
try:
    special = rational.Rational("hello", "world")
    print(special + z)
except TypeError as err:
    print(err)