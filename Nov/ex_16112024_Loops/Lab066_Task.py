# FizzBuzz Test
# Write a program that prints numbers from 1 to 100. However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print("None")


# Displays print message with numbers
#for i in range(1, 100):
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz", i)  # O/P -> FizzBuzz, number
#    elif i % 3 == 0:
#        print("Fizz", i)   # O/P -> Fizz, number
#    elif i % 5 == 0:
#        print("Buzz", i)   # O/P -> Buzz, number
#    else:
#        print("None", i)  # O/P -> None, number


