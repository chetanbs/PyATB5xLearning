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


student_info3 = {
    "name" : "Carl",
    "age" : 25,
    "address" : {
        "home_address" : "COT",
        "office_address" : "Delhi"
    }
}

student_list = [student_info1, student_info2, student_info3]
print(student_list)
print(student_list[2]["address"])
print(student_list[2]["address"]["office_address"])


# Alternate way
print(student_info3["address"])
print(student_info3["address"]["office_address"])

