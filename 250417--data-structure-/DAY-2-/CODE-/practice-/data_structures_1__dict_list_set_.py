print("===========================================")


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
print(numbers)

print("------------------")
numbers.reverse()
print(numbers)

print("------------------")

# todo: do the following using loop

print(f'{max(numbers)}')
print(f'{min(numbers)}')
print(f'{sum(numbers)}')

print("===========================================")


# Dict practice
# Create a dictionary of 3 employees and their salaries
# Update one salary and delete another

employee = { "pankaj": 50000, "luckey": 55000, "biraj": 45000}
print(employee)

employee["aayush"] = 60000
print(employee)

employee.pop("luckey", None)
print(employee, "luckey removed ---")

employee.pop("hello", None)
print(employee, "'hello' tried to remove ---")



print("===========================================")
# <!-- ASSINGMENT (3) -->

# Set practice
# Find common and unique items between two lists using sets
# Loop patterns
### todo : use loop to find answers


age1= [ 2, 4, 6]
age2 = [ 2, 7, 6]

print(age1, age2)

# [2, 4, 6] [2, 7, 6]
# common: {2, 6} ------------ intersection
# unique: {4, 7} //// # [4] [7]
# unique in both : {2, 4, 6, 7}         # (remove dublicates)

set_age1 = set(age1)
set_age2 = set(age2)

### todo : use loop to find answers

# copy_of_set_age1 = set_age1.copy
# copy_of_set_age2 = set_age2.copy

diff_in_two_sets = set_age1.difference(set_age2)
print(diff_in_two_sets, " unique element in one set") # {4} 
print(set_age1,)

print('----------')
sets_sym_diff = set_age1.symmetric_difference(set_age2)
print(sets_sym_diff, "symmetric_difference")

print('----------')
print(set_age1, set_age2)

set_intersection = set_age1.intersection(set_age2)
print(set_intersection, "intersection")

print(set_age1, set_age2)
print('----------')
print('----------')
set_age1.difference_update()
print(set_age1,)

print('----------')

# remove common elements from set_age1
set_diff_update = set_age1.difference_update(set_age2)
print(set_diff_update) # None
print(set_age1, "unique") # {4} # removed common elements from set_age1

print("unique in one set (dublicated not included):")

# print((set_age1 - ))


print('----------')



print('----------')


###### unique elements in both set or list (remove dublicates)
# age_set_common = set(age1 + age2)
age_set_unique = set(age1 + age2)
print("unique in both (remove dublicates):", age_set_unique) # {2, 4, 6, 7}


print('----------')




print('----------')

# age_set_common

print("===========================================")





print("===========================================")





























print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")
# print("===========================================")