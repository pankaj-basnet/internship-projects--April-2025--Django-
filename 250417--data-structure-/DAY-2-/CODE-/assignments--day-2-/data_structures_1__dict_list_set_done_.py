
print("===========================================")

print("assignment 1")


########################################
####### LIST
########################################
"""
Mini Exercises:
List practice
Reverse a list
Find max, min, and sum
"""

numbers = [ 2, 4, 6]
print(numbers, "original list")

print("------------------")
numbers.reverse()
print(numbers)
print("------------------")

print(f'{max(numbers)}, "max (highest num)"')
print(f'{min(numbers)},  "min (lowest num)"')
print(f'{sum(numbers)}, "sum of numbers"')

print("===========================================")

print("assignment 2")


# Dict practice
# Create a dictionary of 3 employees and their salaries
# Update one salary and delete another


print("original dictionary")
employee = { "pankaj": 50000, "luckey": 55000, "biraj": 45000}
print(employee)

print('----------')

employee["aayush"] = 60000
print(employee, " : added 'aayush'")

employee.pop("luckey", None)
print(employee, " : luckey removed")

employee.pop("hello", None)
print(employee, " :  tried to remove 'hello'")



print("===========================================")
# <!-- ASSINGMENT (3) -->

print("assignment 3")

# Set practice
# Find common and unique items between two lists using sets
# Loop patterns

age1= [ 2, 2, 4, 6]
age2 = [ 2, 7, 6]

print(age1, age2)

set_age1 = set(age1)
set_age2 = set(age2)

set_intersection = set_age1.intersection(set_age2)
print(set_intersection, "intersection")


print('----------')

###### unique elements in both set or list (remove dublicates)
age_set_unique = set(age1 + age2)
print("unique in both (remove duplicates):", age_set_unique) # {2, 4, 6, 7}



print("===========================================")





























print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")