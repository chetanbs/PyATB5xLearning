# Tuple - Collection of items
# Syntax - ()
# Its immutable in nature -> Cannot be changed the values

my_tuple = (1, 4, 9, 16, 25)
#my_tuple[3] = 64 # TypeError: tuple object does not support item assignment

shopping_list = ["Bread", " Butter", "Milk"]
print(shopping_list)
shopping_list[2] = "Curd"
print(shopping_list)

# Real Ex Tuple
my_tuple = ("abc.com", "QA.com")
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0] = "mnc.com" # 'tuple' object does not support item assignment

# Real case
API_URLs = ("https://sdet.live/python", "https://qa.com")
print(API_URLs[0])
print(API_URLs[1])