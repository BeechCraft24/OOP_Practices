import json

sensor_data = {
    "voltage": 45,
    "current": 100,
    "temperature": 25
}

with open(r"F:\OOP\json_files\sensor_data.json", "w") as file:
    json.dump(sensor_data, file, indent=4)

print("JSON file created")