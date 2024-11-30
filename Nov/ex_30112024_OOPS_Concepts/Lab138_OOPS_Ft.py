# Web Automation - Selenium
# Page - You are going to automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "Abc@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

# email = Read from test data - Excel or Env File
# password = Read from test data - Excel or Env File

# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

user = VWOLoginPage("Test@gmil.com", "Pass1234")
user.login_confirm()