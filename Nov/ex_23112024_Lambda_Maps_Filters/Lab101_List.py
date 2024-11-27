# Advanced Data Structures
# List -> Collection of Items
# grocery list - Butter, milk, banana
# 10th Marks - 70, 80, 90, 95, 88, 92
# Duplicates are allowed
# Multiple different data types are allowed
# Stored with the Index - 0 Zero -> 0 - n-1
# Syntax -> []
# List is mutable -> Value can be changed

my_list = [1,2,3]  # Same data type
my_list2 = [1, True, "Python", 12.34]

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
#print(my_list[3])  # List Index out of range

my_list[0] = "Learn"
my_list[1] = "Python"
my_list[2] = "Program"
print(my_list)

for item in my_list2:
    print(item)


# Range -> Also returns List only
