class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

def demonstrate_movement(movement):
    for mov in movement:
        mov.move()

car = Car()
plane = Plane()


movement = [car, plane]

demonstrate_movement(movement)
