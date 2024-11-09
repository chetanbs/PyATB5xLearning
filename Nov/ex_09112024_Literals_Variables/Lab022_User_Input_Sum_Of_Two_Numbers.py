#Write a program to take the 2 user input
#then su the number
#mul -> *
#div -> /

#DAA -> Don't Assume Anything

#Logic Building
#Step1
#I/P -> num1, num2 -> int ot float
#O/P -> sum -> int, sub -> int, div -> float

num1 = int(input("Enter the num 1: "))
num2 = int(input("Enter the num 2: "))
print(type(num1))
print(type(num2))

#Step 2  | Rough Logic
#Sum +, Sub -, Mul *, Div /

#Step 3

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is -> ", sum)
print("Sub is -> ", sub)
print("Mul is -> ", mul)
print("Div is -> ", div)

