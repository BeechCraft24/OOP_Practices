# class Readings:
#     def __init__(self):
#         self.voltage = 24
#         self.current = 5
#         self.temperature = 25
#         self.pressure = 1000
#         self.humidity = 21

# readings = Readings()
# print(readings.voltage)
# print(readings.current)
# print(readings.temperature)
# print(readings.pressure)
# print(readings.humidity)
# print(readings.__dict__)
# print(readings.__class__.__name__)



class OwnDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            self.__setitem__(key, value)

own_dict = OwnDict()
own_dict["Voltage"] = 5
own_dict["Pressure"] = 100
own_dict.update({"Temperature": 25, "Humidity": 21})
print(own_dict)