class Engine:
    def engine_type(self):
        print("I am an engine")

class Wheels:
    def wheel_count(self):
        print("I have 4 wheels")

class Car(Engine, Wheels):
    def car_type(self):
        print("I am a car")

car = Car()
car.engine_type()
car.wheel_count()
car.car_type()
