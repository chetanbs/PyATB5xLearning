#for i in range(10):    # 0 to 9
#    print(i)

for i in range(0, 10):
    print(i)
    if i == 5:
        break      # Exit the loop

# | i | condition | O/P |
# | 0 | 0 == 5 -> False | O/P = 0
# | 1 | 1 == 5 -> False | O/P = 1
# | 2 | 2 == 5 -> False | O/P = 2
# | 3 | 3 == 5 -> False | O/P = 3
# | 4 | 4 == 5 -> False | O/P = 4
# | 5 | 5 == 5 -> True | O/P = FIVE  -> Break out of for loop


