class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    def drive_car(self):
        print("Driving on 4 wheels.")

class Bike(Vehicle):
    def ride_bike(self):
        print("Riding on 2 wheels.")

# Creating objects
my_car = Car()
my_bike = Bike()

my_car.start_engine()
my_car.drive_car()

my_bike.start_engine()
my_bike.ride_bike()
