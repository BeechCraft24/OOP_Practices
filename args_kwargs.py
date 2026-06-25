# def my_decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Before")
#         func(*args, **kwargs)
#         print("After")
#     return wrapper

# print(my_decorator(print)("Hello"))



# class Sensor:

#     def __init__(self):
#         self._voltage = 0

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.setter
#     def voltage(self, value):
#         self._voltage = value

# sensor = Sensor()
# sensor.voltage = 4.2
# print(sensor.__dict__)
    


# class Sensor:

#     def __init__(self):
#         self.voltage = 0

# sensor = Sensor()
# sensor.voltage = float(input("Enter voltage: "))
# print(sensor.voltage)



# class Sensor:

#     def __init__(self):
#         self._voltage = 0

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.setter
#     def voltage(self, value):
#         if value < 0 or value > 5:
#             raise ValueError("Voltage must be between 0 and 5")

#         self._voltage = value

# sensor = Sensor()
# sensor.voltage = float(input("Enter voltage: "))
# print(sensor.voltage)