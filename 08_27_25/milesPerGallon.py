'''
Program: Calculate Miles per gallon
Author: Angela Venable
'''

starting_mileage = int(input("Enter the starting mileage: "))
ending_mileage = int(input("Enter the ending mileage: "))
gallons_used = int(input("Enter the gallons used: "))
distance_driven = ending_mileage - starting_mileage
miles_per_gallon = distance_driven / gallons_used
print("Starting Mileage: ",end=" ")
print(starting_mileage)
print("Ending Mileage: ", ending_mileage)
print("Distance Driven: ", distance_driven)
print("Gallons Used: ", gallons_used)
print("Miles Per Gallon: ", miles_per_gallon)
