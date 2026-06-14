# class Person:

#     def __init__(self):
#         self._age = 0

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):

#         if value < 0:
#             print("Age cannot be negative")
#             return

#         self._age = value

# p = Person()

# p.age = 25
# print(p.age)
# p.age = -5
# print(p.age)




# class Person:
#     def __init__(self):
#         self.age = 0

# p = Person()
# p.age = 25
# print(p.age)



# class Oxygen_Transducer:
#     def __init__(self, voltage, pressure, temperature):
#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature
#         self.oxygen_level = 0

# p = Oxygen_Transducer(voltage=5.0, pressure=100, temperature=25)
# print("Voltage:", p.voltage)
# print("Pressure:", p.pressure)
# print("Temperature:", p.temperature)




# class Oxygen_Transducer:
#     def __init__(self, voltage, pressure, temperature):
#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature

# voltage = float(input("Enter voltage: "))
# pressure = float(input("Enter pressure: "))
# temperature = float(input("Enter temperature: "))

# p = Oxygen_Transducer(voltage=voltage, pressure=pressure, temperature=temperature)
# print("Voltage:", p.voltage)
# print("Pressure:", p.pressure)
# print("Temperature:", p.temperature)




# class Oxygen_Transducer:
#     def __init__(self, voltage, pressure, temperature):
#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature

# voltage = float(input("Enter voltage: "))
# pressure = float(input("Enter pressure: "))
# temperature = float(input("Enter temperature: "))

# print("Voltage:", voltage)
# print("Pressure:", pressure)
# print("Temperature:", temperature)




class Oxygen_Transducer:

    def __init__(self, voltage, pressure, temperature):
        self.voltage = voltage
        self.pressure = pressure
        self.temperature = temperature

    def display(self):
        print(self.voltage, self.pressure, self.temperature)

inventory = []

for i in range(3):

    print(f"\nEntering sensor {i+1}")

    voltage = float(input("Voltage: "))
    pressure = float(input("Pressure: "))
    temperature = float(input("Temperature: "))

    sensor = Oxygen_Transducer(voltage, pressure, temperature)
    inventory.append(sensor)

print("\nALL SENSORS:\n")

for sensor in inventory:
    sensor.display()