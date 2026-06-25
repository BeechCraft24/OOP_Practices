# class Sensor:

#     def __init__(self):
#         self._voltage = 3.3

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.deleter
#     def voltage(self):
#         print("Deleting voltage")
#         del self._voltage

# sensor = Sensor()
# print(sensor.voltage)
# del sensor.voltage



# class Sensor:
#     def __init__(self):
#         self._voltage = 3.3

# sensor = Sensor()
# del sensor._voltage



# class Sensor:
#     def __init__(self):
#         self._voltage = 3.3

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.deleter
#     def voltage(self):
#         raise AttributeError("Voltage cannot be deleted")
    
# sensor = Sensor()
# del sensor.voltage




# class Sensor:
#     def __init__(self):
#         self._voltage = 3.3

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.deleter
#     def voltage(self):
#         print("Voltage cannot be deleted")
    
# sensor = Sensor()
# del sensor.voltage



# class Sensor:
#     def __init__(self, voltage):
#         self._voltage = voltage

#     @property
#     def voltage(self):
#         if self._voltage > 5 or self._voltage < 0:
#             raise AttributeError("Voltage is out of bounds")
#         return self._voltage

#     @voltage.deleter
#     def voltage(self):
#         print("Voltage cannot be deleted")
#         self._voltage = None
    
# sensor = Sensor(float(input("Enter voltage: ")))
# print(sensor.voltage)
# del sensor.voltage



# class Sensor:

#     def __init__(self):
#         self._voltage = 3.3

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.deleter
#     def voltage(self):
#         print("Deleting voltage...")
#         del self._voltage

# sensor = Sensor()
# print(sensor.voltage)
# del sensor.voltage



# class Account:

#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.deleter
#     def balance(self):
#         if self._balance != 0:
#             raise ValueError("Balance must be zero")
#         del self._balance

# acc = Account(0)
# del acc.balance



# class Account:

#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.deleter
#     def balance(self):
#         if self._balance != 0:
#             raise ValueError("Balance must be zero")
#         del self._balance

# acc = Account(balance=int(input("Enter balance: ")))
# del acc.balance



class Account:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        if self._balance != 0:
            raise ValueError("Balance must be zero")
        elif self._balance == 0:
            del self._balance
            print("Account deleted successfully")

acc = Account(balance=int(input("Enter balance: ")))
del acc.balance