class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def myFunction(self):
        print("Hello I am " + self.name + " and my email is" + self.email)


p1 = Person("Rokib", "rokib@gmail.com")
p1.myFunction()
