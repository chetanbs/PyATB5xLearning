class Calc:

    def sum(self, *args):
        for a in args:
            print(a)

# *args - Multiple values


calc_ref = Calc()
calc_ref.sum(2)
calc_ref.sum(2,4)
calc_ref.sum(2,4,6)
