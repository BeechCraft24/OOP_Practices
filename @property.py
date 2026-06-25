# class Person:
#     def get_age(self):
#         return 42
# p = Person()
# print(p.get_age())



# class Person:
#     @property
#     def get_age(self):
#         return 42
# p = Person()
# print(p.get_age)



# class Account:
#     def __init__(self):
#         self._balance = 0

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self._balance = value

# acc = Account()
# acc.balance = int(input("Enter balance: "))
# print(acc.balance)





# class OxygenSensor:

#     def __init__(self):
#         self._voltage = 4.75

#     @property
#     def voltage(self):
#         return self._voltage

# sensor = OxygenSensor()
# print(sensor.voltage)




# class OxygenSensor:

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

# sensor = OxygenSensor()
# sensor.voltage = float(input("Enter voltage: "))
# print(sensor.voltage)




# class OxygenSensor:

#     def __init__(self, voltage):
#         self._voltage = voltage

#     @property
#     def voltage(self):
#         return self._voltage
    
#     @voltage.setter
#     def voltage(self, value):
#         if value < 0 or value > 5:
#             raise ValueError("Voltage must be between 0 and 5")
#         self._voltage = value

# sensor = OxygenSensor(3.3)
# sensor.voltage = float(input("Enter voltage: "))
# print(sensor.voltage)


# class OxygenSensor:

#     def __init__(self, voltage):
#         self.voltage = voltage

#     @property
#     def voltage(self):
#         return self._voltage
    
#     @voltage.setter
#     def voltage(self, value):
#         if value < 0 or value > 5:
#             raise ValueError("Voltage must be between 0 and 5")
#         self._voltage = value

# sensor = OxygenSensor(9)
# sensor.voltage = float(input("Enter voltage: "))
# print(sensor.voltage)


class OxygenSensor:

    def __init__(self, voltage):
        self.voltage = 0

    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self, value):
        if value < 0 or value > 5:
            raise ValueError("Voltage must be between 0 and 5")
        self._voltage = value

sensor = OxygenSensor(0)
sensor.voltage = float(input("Enter voltage: "))
print(sensor.voltage)