bob_salary = 25000

print(id(bob_salary))
tom_salary = 30000

print(id(tom_salary))
bob_salary = tom_salary

print(id(bob_salary))

print(id(tom_salary))
tom_salary = tom_salary * 1.2
print(id(tom_salary))
total_salaries = bob_salary + tom_salary
my_var = "abc"
my_var = "ABC"
