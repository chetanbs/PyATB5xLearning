# Multi-Level Inheritance
# GrandParent -> Father -> Son

class GrandFather:
    Gold = "2Kg"

    def BHK1(self):
        print("1BHK")

class Father(GrandFather):
    Diamond = "22 Caret"

    def BHK2(self):
        print("2BHK")

class Son(Father):
    btc = "1BTC"

    def BHK3(self):
        print("3BHK")


s = Son()
print(s.Gold)
print(s.Diamond)
print(s.btc)

f = Father()
# print(f.btc)   # Son property
print(f.Gold)    # Able to access bcz its GrandParent property

