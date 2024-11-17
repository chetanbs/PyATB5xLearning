# Match Statement -> Switch statement in Java
# Match the O/P and execute
# Python > 3.10 - match works with this version and above

# match variable:
#   case pattern1:
#       code block
#   case pattern2:
#       code block

# Write a program to ask the user which browser he wants to run automation

browser_name = input("Enter the browser name: ")
match browser_name:
    case "Firefox":
        print("Starting the Firefox Browser....")
    case "Chrome":
        print("Starting the Chrome Browser....")
    case "Edge":
        print("Starting the Edge Browser....")
    case "Safari":
        print("Starting the Safari Browser....")
    case _:  # default
        print("Browser not found")
