# def logger(func):
#     def wrapper():
#         print("Function called")
#         func()
#     return wrapper

# @logger
# def hello():
#     print("Hello")

# hello()




# class Car:
#     def engine(self):
#         print("Running")

# x = Car()
# x.engine()
       



# class Car:
#     def __init__(self, speed):
#         self.speed = speed

#     def engine(self):
#         print("running")

# x = Car()
# x.engine()




# class Car:
#     def __init__(self, speed):
#         self.speed = speed

#     def engine(self):
#         print("running at", self.speed, "mph")

# x = Car(100)
# x.engine()




# class Car:
#     def __init__(self, speed):
#         self.speed = speed

#     def engine(self):
#         print("running at", self.speed, "mph")

# x = Car(int(input("Enter speed: ")))
# x.engine()



# class Car:
#     def __init__(self, speed):
#         self.speed = speed
#         if self.speed < 0:
#             raise ValueError("Speed cannot be negative")

#     def engine(self):
#         print("running at", self.speed, "mph")

# x = Car(int(input("Enter speed: ")))
# x.engine()



# class Car:
#     def __init__(self, speed):
#         self.speed = speed
#         try:
#             if self.speed < 0:
#                 raise ValueError("Speed cannot be negative")
#         except ValueError as e:
#             print(e)

#     def engine(self):
#         print("running at", self.speed, "mph")

# x = Car(int(input("Enter speed: ")))
# x.engine()




# class Car:
#     def __init__(self, speed):
#         if speed < 0:
#             raise ValueError("Speed cannot be negative")

#         self.speed = speed

#     def engine(self):
#         print("running at", self.speed, "mph")

# try:
#     x = Car(int(input("Enter speed: ")))
#     x.engine()
# except ValueError as e:
#     print(e)



# class Car:
#     def __init__(self, speed):
#         if speed < 0:
#             raise ValueError("Speed cannot be negative")
#         elif speed > 300:
#             raise ValueError("Speed cannot exceed 300 mph")
#         elif speed == 0:
#             raise ValueError("Car stopped")

#         self.speed = speed

#     def engine(self):
#         print("running at", self.speed, "mph")

# try:
#     x = Car(int(input("Enter speed: ")))
#     x.engine()
# except ValueError as e:
#     print(e)




# class Oxygen_Transducer:
#     def __init__(self, voltage, pressure, temperature):
#         if voltage < 0:
#             raise ValueError("voltage cannot be negative")
#         elif voltage > 5:
#             raise ValueError("voltage cannot exceed 5V")
#         elif voltage == 0:
#             raise ValueError("no source of voltage")

#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature

#     def read_values(self):
#         print("voltage:", self.voltage, "V")
#         print("pressure:", self.pressure, "psi")
#         print("temperature:", self.temperature, "°F")

# try:
#     x = Oxygen_Transducer(
#         voltage=float(input("Enter voltage: ")),
#         pressure=float(input("Enter pressure: ")),
#         temperature=float(input("Enter temperature: "))
#     )
#     x.read_values()
# except ValueError as e:
#     print(e)




class Oxygen_Transducer:
    def __init__(self, voltage, pressure, temperature):
        if voltage < 0:
            raise ValueError("voltage cannot be negative")
        elif voltage > 5:
            raise ValueError("voltage cannot exceed 5V")
        elif voltage == 0:
            raise ValueError("no source of voltage")
        elif pressure > 2000:
            raise ValueError("pressure cannot exceed 2000 psi")
        elif pressure < 0:
            raise ValueError("pressure cannot be negative")
        elif pressure == 0:
            raise ValueError("no oxygen pressure")
        elif temperature <= 0:
            raise ValueError("temperature is out of valid range")
        elif temperature > 130:
            raise ValueError("temperature cannot exceed 130 °F")

        self.voltage = voltage
        self.pressure = pressure
        self.temperature = temperature

    def read_values(self):
        print("voltage:", self.voltage, "V")
        print("pressure:", self.pressure, "psi")
        print("temperature:", self.temperature, "°F")

try:
    x = Oxygen_Transducer(
        voltage=float(input("Enter voltage: ")),
        pressure=float(input("Enter pressure: ")),
        temperature=float(input("Enter temperature: "))
    )
    x.read_values()
except ValueError as e:
    print(e)