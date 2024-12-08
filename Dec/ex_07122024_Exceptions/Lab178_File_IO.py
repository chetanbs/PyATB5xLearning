file_name = "Test.txt"
content = "This is a Test file"

with open(file_name, "w") as file:
    file.write(content)

with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)