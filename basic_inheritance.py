class Animal:
    def speak(self):
        print ("I make a sound")

class Dog(Animal):
    def speak(self):
        print('Woof! Woof! ')

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()