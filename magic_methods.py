# class SensorData:
#     def __getitem__(self, index):
#         return f"Reading {index}"

# sensor = SensorData()
# print(sensor[2])



# class Alarm:
#     def __call__(self):
#         print("Alarm activated")

# alarm = Alarm()
# alarm()



class Alarm:
    def __call__(self):
        print("Alarm activated")

alarm = Alarm()
alarm.__call__()