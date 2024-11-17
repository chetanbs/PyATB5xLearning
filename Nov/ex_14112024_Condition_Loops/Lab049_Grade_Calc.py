# Write a program that calculates and displays the letter grade for a given numerical score
# ex: A,B,C,D,or F based on the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic building formula
# 1 -> User Inputs -> score or marks -> int
# 2 -> O/P -> str -> A or B

score = int(input("Enter your Score: "))

if score >= 90 and score <=100:
    print("Secured Grade is A")
elif score >=80 and score <=89:
    print("Secured Grade is B")
elif score >=70 and score <=79:
    print("Secured Grade is B")
elif score >=60 and score <=69:
    print("Secured Grade is B")
elif score >=100 and score <=-1:
    print("Invalid Grade")
else:
    print("Secured Grade is F")