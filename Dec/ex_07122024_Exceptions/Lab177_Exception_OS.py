class XYZ:

    def f1(self):
        try:
            a = int(input("Enter a number: "))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)
        finally:
            print("Finally part will always execute")

obj = XYZ()
obj.f1()