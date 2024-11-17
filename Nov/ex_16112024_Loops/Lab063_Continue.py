# Continue Statement -> Continue Statement skips the current iteration of loop and moves to the next iteration

for number in range(10):
    if number % 2 == 0:
        continue     # for even numbers we are skipping to display in output
    else:
        print(number)  # Odd numbers get display in output


# | i | condition | O/P |
# | 0 | 0%2 == 0 -> True | Continue -> Skips, No O/P
# | 1 | 1%2 == 0 -> False | O/P = 1
# | 2 | 2%2 == 0 -> True | O/P = 2


# pass -> can be used in the statement, functions, classes and objects

