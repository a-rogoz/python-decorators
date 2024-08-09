

def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == "milage":
            print("We noticed that the milage attribute was read")
        return class_.__getattr__orig(self, name)
    
    class_.__getattribute__ = new_getattr
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.milage = 0
        self.VIN = VIN


car = Car("ABC123")
print("The milage is", car.milage)
print("The VIN is", car.VIN)