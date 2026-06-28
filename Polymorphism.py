class Sensor:
    def read(self):
        pass

class OxygenSensor(Sensor):
    def read(self):
        print("Reading oxygen level...")

class TemperatureSensor(Sensor):
    def read(self):
        print("Reading temperature...")

class PressureSensor(Sensor):
    def read(self):
        print("Reading pressure...")

sensor = [OxygenSensor(), TemperatureSensor(), PressureSensor()]
for s in sensor:
    s.read()