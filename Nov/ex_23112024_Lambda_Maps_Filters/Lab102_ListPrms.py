my_list = [1, 2, 3]

# Indexing
print("Element at the index 0 - ", my_list[0])
print("Element at the index 0 - ", my_list[1])
print("Element at the index 0 - ", my_list[2])

# append() -> Append object to the end of the list
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - append new list
my_list.extend([7, 8, 14, 16, 9, 10])
print(my_list)

# insert()
my_list.insert(1, "Python")
print(my_list)
print((len(my_list)))

my_list.insert(0, 0)
print(my_list)

my_list[1] = "Code"
print(my_list)

my_list.remove("Code")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.remove("Python")
print(my_list)

my_copy_list.remove("Python")
print(my_copy_list)

my_copy_list.sort()
print(my_list)
print(my_copy_list)

