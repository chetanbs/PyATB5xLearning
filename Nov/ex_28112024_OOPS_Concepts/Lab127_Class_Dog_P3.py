class Dog:
    # Attributes
    name = None
    breed = None
    height = None
    weight = None


    def __init__(self, name, breed):
        print("Parameterized Constructor")
        self.name = name
        self.breed = breed


    # Behavior
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is Sleeping -> " + self.name)

    def talk(self):
        pass

# Object Ref

chow_ref = Dog("chow", "BB")
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))

mow_ref = Dog("mow", "husky")
#bow_ref = Dog("mow", "husky")
#rancho_ref = Dog()
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))

