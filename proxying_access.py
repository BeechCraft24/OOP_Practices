# class Engine:
#     def get_temperature(self):
#         return 90

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     @property               #this property is proxying access to another object
#     def temperature(self):
#         return self.engine.get_temperature()
    
# car = Car()
# print(car.temperature)



class Sensor:
    def __init__(self):
        self._voltage = 3.3

    @property     
    def voltage(self):
        return self._voltage    #proxying to a private attribute (_voltage)
    



class Engine:
    def get_temperature(self):
        return 90

class Car:
    def __init__(self):
        self.engine = Engine()

    @property
    def temperature(self):
        return self.engine.get_temperature()    #here is proxying access to another object
