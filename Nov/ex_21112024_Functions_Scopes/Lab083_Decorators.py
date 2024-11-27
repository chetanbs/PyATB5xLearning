# You can add a Annotation to the functions to perform the extra task
# Ex: before running the function i want to do something (decorators)

# Decorators in Python are a powerful and flexible tool that allows you to modify the behaviour of
# the functions or methods without changing their actual code

# They are essentially functions that take another function as an argument and entend
# or alter its behaviour

# Allure Report - HTML Report - @allure -> make sure that the allure report is generated
# API Automation - @file_details -> csv file or data

def add_extra_security(func):
    def wrapper():
        print("1.Before the function is called")
        print("2.Add Helmet, Dashcam, Gloves, KneeGuards, License")
        func()  # drive_scooty
        print("3.After the function is called")
        print("4.Secure Driving, Leave all the items")

    return wrapper()


@add_extra_security
def drive_ola_scooter():
    print("Ola")


@add_extra_security
def drive_scooty():
    print("Normal Function!")
    print("I am driving a Scooty")