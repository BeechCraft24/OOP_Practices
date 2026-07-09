# class MyMeta(type):
#     def __new__(mcs, name, bases, namespace):
#         namespace['manufacturer'] = 'Honeywell'
#         return super().__new__(mcs, name, bases, namespace)
    
# class PressureSensor(metaclass=MyMeta):
#     pass

# sensor = PressureSensor()
# print(sensor.manufacturer)




# class MyMeta(type):
#     def __new__(mcs, name, bases, namespace):

#         def calibrate(self):
#             print("Calibration completed")
#         namespace["calibrate"] = calibrate
#         return super().__new__(mcs, name, bases, namespace)

# class TemperatureSensor(metaclass=MyMeta):
#     pass

# sensor = TemperatureSensor()
# sensor.calibrate()




# from datetime import datetime

# class MyMeta(type):
#     def __new__(mcs, name, bases, namespace):
#         namespace["creation_time"] = datetime.now()
#         return super().__new__(mcs, name, bases, namespace)

# class PressureSensor(metaclass=MyMeta):
#     pass

# print(PressureSensor.creation_time)




# class MyMeta(type):

#     def __new__(mcs, name, bases, namespace):
#         if "manufacturer" not in namespace:
#             raise TypeError("Every sensor class must define manufacturer.")
#         return super().__new__(mcs, name, bases, namespace)

# class PressureSensor(metaclass=MyMeta):
#     manufacturer = "Honeywell"




# class SensorMeta(type):
#     registry = []
#     def __new__(mcs, name, bases, namespace):
#         cls = super().__new__(mcs, name, bases, namespace)
#         mcs.registry.append(name)
#         return cls

# class PressureSensor(metaclass=SensorMeta):
#     pass

# class TemperatureSensor(metaclass=SensorMeta):
#     pass

# print(SensorMeta.registry)




# class AviationMeta(type):
#     def __new__(mcs, name, bases, namespace):
#         if "manufacturer" not in namespace:
#             raise TypeError("manufacturer missing")
#         if "calibrate" not in namespace:
#             raise TypeError("calibrate() missing")
#         return super().__new__(mcs, name, bases, namespace)

# class PressureSensor(metaclass=AviationMeta):
#     manufacturer = "Honeywell"
#     def calibrate(self):
#         print("Calibration completed")





# from datetime import datetime

# class MyMeta(type):

#     def __new__(mcs, name, bases, namespace):
#         namespace["instantiation_time"] = datetime.now()

#         def get_instantiation_time(self):
#             return self.instantiation_time

#         namespace["get_instantiation_time"] = get_instantiation_time
#         return super().__new__(mcs, name, bases, namespace)
# class PressureSensor(metaclass=MyMeta):
#     pass

# sensor = PressureSensor()
# print(sensor.get_instantiation_time())



class Sensor:
    def read_value(self):
        print("Generic sensor reading")

class PressureSensor(Sensor):
    def read_value(self):
        print("Pressure sensor reading")

sensor = PressureSensor()
sensor.read_value()