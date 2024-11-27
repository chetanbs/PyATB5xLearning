cities = ("London", "Bengaluru", "LA", "Tokyo")
print("Bengaluru" in cities)
print("New Delhi" in cities)

t = (12, 34, 56)
#t.append(12) # Attribute Error
my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)

ENV_API_URLs = tuple(["https://sdet.live/python", "https://qa.com"])
print(ENV_API_URLs)