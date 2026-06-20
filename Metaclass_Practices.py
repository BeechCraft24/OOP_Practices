# class My_Meta(type):
#     classes_created = []
#     def __new__(mcs, name, bases, dictionary):
#         print(mcs)

# class PressureSensor(metaclass=My_Meta):
#     pass



# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         print(mcs)
#         print(name)
# class PressureSensor(metaclass=My_Meta):
#     pass




# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")

# class Truck(Vehicle):
#     def start_engine(self):
#         print("Truck engine started")

# car = Car()
# car.start_engine()
# truck = Truck()
# truck.start_engine()




# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def engine(self, speed, fuel_type):
#         pass

# class Car(Vehicle):
#     def engine(self, speed, fuel_type):
#         print(f"Car speed: {speed} mph with {fuel_type}")

# car = Car()
# car.engine(100, "gasoline")




# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def engine(self, speed, fuel_type):
#         pass

# class Car(Vehicle):
#     def engine(self, speed, fuel_type):
#         print(f"Car speed: {speed} mph with {fuel_type}")

# x = Car()
# x.engine(100, "gasoline")





# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def engine(self, speed, fuel_type):
#         pass

# class Car(Vehicle):
#     def engine(self, speed, fuel_type):
#         print(f"Car speed: {speed} mph with {fuel_type}")

# x = Car()
# x.engine(100, "gasoline")




from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def engine(self, speed, fuel_type):
        pass

    @abstractmethod 
    def upholstery(self, material, color):
        pass    

class Car(Vehicle):
    def engine(self, speed, fuel_type):
        print(f"Car speed: {speed} mph with {fuel_type}")

    def upholstery(self, material, color):
        print(f"Car upholstery: {material} in {color}")

x = Car()
x.engine(100, "gasoline")
x.upholstery("leather", "black")