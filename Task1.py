names = ["Emily", "Pete", "John", "Frank", "Boris", "Phil"]

print(names[0], "sup gang!")
print(names[1], "what u doin?")
print(names[3], "its lit.")

names.remove("John")
print(names)

names.insert(1, "Adria")
print(names)

del names[1] 
print(names)

names.sort(reverse=True)
print(names)

pizzas = ["Pepperoni", "Margarrita", "Seafood"]

for pizza in pizzas :
    print(pizza, "that s my favourite.")
    
