class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

print(issubclass(Dog, Mammal))
print(issubclass(Dog, Animal))
print(isinstance(Dog(), Mammal))
print(isinstance(Dog(), Animal))
