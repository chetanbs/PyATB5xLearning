student_info = {
    "name" : "Name",
    "age" : 30,
    "address" : "KA"
}

print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 28
print(student_info)

# Another way to create a dictionary
student_info = dict(name =  "ABC", age = 50, address = "KA")


student_info1 = {
    "name" : "Name",
    "age" : 30,
    "address" : {
        "home_address" : "AA",
        "office_address" : "KA"
    }
}