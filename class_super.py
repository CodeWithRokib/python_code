class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


car = Car("Toyota", "Corolla", 4)
car.display_info()
