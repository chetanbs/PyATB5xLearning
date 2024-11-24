# Pizza
# Toppings -> Mushroom, Panner, Olives, Corn, PIneapple, Jalapeno

def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)

user1 = make_pizza("tomato", "olives")
user2 = make_pizza("tomato", "olives", "corn", "Panner")
user3 = make_pizza("tomato")

r1 = max(1,2,3,4,5)
r2 = max(1,2,3)
r3 = max(2,3)
