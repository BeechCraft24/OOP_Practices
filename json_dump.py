# import os
# import json

# print("Current folder:", os.getcwd())

# with open(r"F:\OOP\json_files\test.json", "w") as file:
#     json.dump({"voltage": 2.5}, file)




# import os
# import json

# print("Current folder:", os.getcwd())

# with open(r"F:\OOP\json_files\test.json", "w") as file:
#     json.dump({"voltage": 45}, file)



import os
import json

print("Current folder:", os.getcwd())

with open(r"F:\OOP\json_files\sensor_data.json", "w") as file:
    json.dump({"voltage": 45, "current": 100, "temperature": 25}, file)