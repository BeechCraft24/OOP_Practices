class Tires:
    def __init__(self, size, pressure=32):
        self.size = size
        self.pressure = pressure

    def get_pressure(self):
        return self.pressure

    def pump(self, amount):
        self.pressure += amount
        print(f"Tires pumped to {self.pressure} PSI")

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        print(f"{self.fuel_type} engine started")

    def stop(self):
        self.running = False
        print(f"{self.fuel_type} engine stopped")

    def get_state(self):
        return "Running" if self.running else "Stopped"

class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

# Create tire sets
city_tires = Tires(size=15)
offroad_tires = Tires(size=18)

# Create engines
electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")

# Create vehicles
city_car = Vehicle(
    VIN="CITY-001",
    engine=electric_engine,
    tires=city_tires
)

offroad_car = Vehicle(
    VIN="OFFROAD-001",
    engine=petrol_engine,
    tires=offroad_tires
)

# Interact with city car
print("CITY CAR")
print("VIN:", city_car.VIN)
city_car.engine.start()

print("Engine state:", city_car.engine.get_state())
print("Tire size:", city_car.tires.size)
print("Pressure:", city_car.tires.get_pressure())

city_car.tires.pump(3)
city_car.engine.stop()
print("Engine state:", city_car.engine.get_state())
print("\n-------------------\n")

# Interact with off-road car
print("OFF-ROAD CAR")
print("VIN:", offroad_car.VIN)
offroad_car.engine.start()

print("Engine state:", offroad_car.engine.get_state())
print("Tire size:", offroad_car.tires.size)
print("Pressure:", offroad_car.tires.get_pressure())

offroad_car.tires.pump(5)
offroad_car.engine.stop()
print("Engine state:", offroad_car.engine.get_state())