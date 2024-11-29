student_info1 = {
    "name" : "Name",
    "age" : 30,
    "address" : {
        "home_address" : "AA",
        "office_address" : "KA"
    }
}


student_info2 = {
    "name" : "Man",
    "age" : 25,
    "address" : {
        "home_address" : "BB",
        "office_address" : "KA"
    }
}

student_list = [student_info1, student_info2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["office_address"])
print("==========")
print(student_list[1])
print(student_list[2])  # list index out of range