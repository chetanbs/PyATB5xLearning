# Dictionary - Dict -> Key and Value Pair
# A Dictionary is a unordered, mutable and indexed collection of Key-Value pairs in Python
# Syntax -> {} - Curly braces
# Common Operations with Dictionaries
# Accessing Values : Key-Value Pair: my_dict[Key] = value
# Removing a Key: del my_dict[key]
# Iterating: for key, value in my_dict.items():
# dict() - Empty Dictionary
# Dictionary Methods:
# * get(), keys(), values(), items(), update(), pop(), clear()

my_dict = {
    "name" : "ABC",
    "age" : 30,
    "role" : "SDET",
    "experience" : 5
}

print(my_dict)

my_dict["role"] = "Manual Tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(key, " -> ", value)

print("age" in my_dict)
print("role" in my_dict)