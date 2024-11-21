class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I cannot fly, but I can swim")

bird = Bird()
bird.fly()

penguin = Penguin()
penguin.fly()
