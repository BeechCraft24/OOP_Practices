# class LogDict(dict):
#     def __setitem__(self, key, value):
#         print(f"Adding {key} = {value}")
#         super().__setitem__(key, value)

# d = LogDict()
# d["Voltage"] = 5
# d["Pressure"] = 100
# print(d)



# class SensorDict(dict):
#     def __setitem__(self, key, value):
#         if value < 0 or value > 5:
#             raise ValueError("Voltage out of range")
#         super().__setitem__(key, value)

# sensors = SensorDict()
# sensors["Voltage"] = 3
# print(sensors)




# class SensorStorage:
#     def __init__(self):
#         self.storage = []

#     def __setitem__(self, index, value):
#         while len(self.storage) <= index:
#             self.storage.append(None)   #None is used to create a placeholder for the index, like empty positions in the list.
#         self.storage[index] = value
        
# s = SensorStorage()
# s[0] = int(input("Enter voltage: "))
# s[1] = int(input("Enter pressure: "))
# s[2] = int(input("Enter temperature: "))
# s[3] = int(input("Enter humidity: "))
# print(s.storage)
        



# import shelve

# class SensorStorage:
#     def __init__(self):
#         self.storage = []
#     def __setitem__(self, index, value):
#         while len(self.storage) <= index:
#             self.storage.append(None)
#         self.storage[index] = value

# s = SensorStorage()
# s[0] = int(input("Enter voltage: "))
# s[1] = int(input("Enter pressure: "))
# s[2] = int(input("Enter temperature: "))
# s[3] = int(input("Enter humidity: "))
# print("Current list:", s.storage)

# # Save the list permanently
# db = shelve.open("sensor_database", flag="c")
# db["sensor_readings"] = s.storage
# db.close()
# print("Sensor readings saved.")




import shelve

class SensorStorage:
    def __init__(self):
        self.storage = {}
    def __setitem__(self, key, value):
        self.storage[key] = value

s = SensorStorage()
s["Voltage"] = float(input("Enter voltage: "))
s["Pressure"] = float(input("Enter pressure: "))
s["Temperature"] = float(input("Enter temperature: "))
s["Humidity"] = float(input("Enter humidity: "))
print("\nCurrent Sensor Readings")
print(s.storage)

db = shelve.open("sensor_database", flag="c")
db["Sensors"] = s.storage
db.close()
print("\nSensor data saved successfully.")