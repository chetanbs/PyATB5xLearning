def outer_function():
    var1 = 30  # Local or GLobal -> Local

    def inner_function():
        var2 = 50
        print(var1)

    def inner_function2():
        print(var1)


    inner_function()
    inner_function2()
    #print(var2) -> Not allowed

outer_function()

# Outer functions variabes can be used by the inner functions



