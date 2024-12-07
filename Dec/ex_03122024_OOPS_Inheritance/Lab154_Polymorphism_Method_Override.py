class Father:

    def home(self):
        print("1BHK")

class Son(Father):

    def home(self):
        print("2BHK")

s = Son()
s.home()

f = Father()
f.home()