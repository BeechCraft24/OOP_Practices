# class Oxygen_Transducer:

#     def __init__(self, voltage, pressure, temperature):
#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature

#     def display(self):
#         print(self.voltage, self.pressure, self.temperature)

# inventory = []

# for i in range(3):

#     print(f"\nEntering sensor {i+1}")

#     voltage = float(input("Voltage: "))
#     pressure = float(input("Pressure: "))
#     temperature = float(input("Temperature: "))
#     sensor = Oxygen_Transducer(voltage, pressure, temperature)
#     inventory.append(sensor)

# print("\nALL SENSORS:\n")

# for sensor in inventory:
#     sensor.display()




from datetime import datetime

# class Oxygen_Transducer:

#     def __init__(self, voltage, pressure, temperature):

#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature
#         self.log = []
#         self.log_event("Sensor created")

#     def log_event(self, message):

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.log.append(f"{timestamp} -> {message}")

#     def display(self):

#         print(f"Voltage: {self.voltage}")
#         print(f"Pressure: {self.pressure}")
#         print(f"Temperature: {self.temperature}")

#     def show_log(self):

#         print("\nLOG HISTORY:")
#         for entry in self.log:
#             print(entry)

# inventory = []

# for i in range(3):

#     print(f"\nEntering sensor {i+1}")

#     voltage = float(input("Voltage: "))
#     pressure = float(input("Pressure: "))
#     temperature = float(input("Temperature: "))

#     sensor = Oxygen_Transducer(voltage, pressure, temperature)
#     inventory.append(sensor)

# print("total sensors added:", len(inventory))

# for sensor in inventory:
#     print(sensor.voltage, sensor.pressure, sensor.temperature)
#     print(sensor.log)





# class Oxygen_Transducer:

#     def __init__(self, voltage, pressure, temperature):

#         self.voltage = voltage
#         self.pressure = pressure
#         self.temperature = temperature
#         self.log = []
#         self.log_event()

#     def log_event(self):

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.log.append(f"{timestamp}")

#     def display(self):

#         print(f"Voltage: {self.voltage}")
#         print(f"Pressure: {self.pressure}")
#         print(f"Temperature: {self.temperature}")

#     def show_log(self):

#         print("\nLOG HISTORY:")
#         for entry in self.log:
#             print(entry)

# inventory = []

# for i in range(3):

#     print(f"\nEntering sensor {i+1}:")

#     voltage = float(input("Voltage: "))
#     pressure = float(input("Pressure: "))
#     temperature = float(input("Temperature: "))

#     sensor = Oxygen_Transducer(voltage, pressure, temperature)
#     inventory.append(sensor)

# print("total sensors added:", len(inventory))

# for sensor in inventory:
#     print(f"\nSensor Logs:")
#     print(sensor.voltage, sensor.pressure, sensor.temperature)
#     print(sensor.log)
#     print("\n")






class Oxygen_Transducer:

    def __init__(self, voltage, pressure, temperature):

        self.voltage = voltage
        self.pressure = pressure
        self.temperature = temperature
        self.log = []
        self.log_event()

    def log_event(self):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f"{timestamp}")

    def display(self):

        print(f"Voltage: {self.voltage}")
        print(f"Pressure: {self.pressure}")
        print(f"Temperature: {self.temperature}")

    def show_log(self):

        for entry in self.log:
            print(entry)

inventory = []

for i in range(3):

    print(f"\nEntering sensor {i+1}:")

    voltage = float(input("Voltage: "))
    pressure = float(input("Pressure: "))
    temperature = float(input("Temperature: "))

    sensor = Oxygen_Transducer(voltage, pressure, temperature)
    inventory.append(sensor)

print(f"\nTotal sensors added: {len(inventory)}")

for sensor in inventory:
    print(f"\nSensor Logs:")
    print(sensor.voltage, sensor.pressure, sensor.temperature)
    sensor.show_log()
    print("\n")




