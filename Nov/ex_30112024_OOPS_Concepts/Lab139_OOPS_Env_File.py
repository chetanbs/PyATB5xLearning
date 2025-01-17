# Web Automation - Selenium
# Page - You are going to automate

from dotenv import load_dotenv
import os

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "Test @gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()

#user = VWOLoginPage("Test@gmil.com", "Pass1234")
#user.login_confirm()