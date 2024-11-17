# Check for a Leap year - 2024 - Yes
# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

year = int(input("Enter the year: "))
if year % 100 == 0 and year % 400 != 0:
    print("Leap year")
else:
    print("Not a leap year")

