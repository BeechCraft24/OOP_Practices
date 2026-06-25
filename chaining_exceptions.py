# class SensorError(Exception):
#     pass

# try:
#     int("abc")
# except ValueError as e:
#     try:
#         raise SensorError("Invalid sensor reading") from e
#     except SensorError as s:
#         print(s.__cause__)



# class SensorError(Exception):
#     pass

# try:
#     int(input("Enter value: "))
# except ValueError as e:
#     try:
#         raise SensorError("Invalid sensor reading") from e
#     except SensorError as s:
#         print(s)
#         print(s.__cause__)




# class SensorError(Exception):
#     pass

# try:
#     int(input("Enter value: "))
# except ValueError as e:
#     raise SensorError("Invalid sensor reading") from e





# class SensorError(Exception):
#     pass

# try:
#     int(input("Enter value: "))
# except ValueError as e:
#     try:
#         raise SensorError("Invalid sensor reading") from e
#     except SensorError as s:
#         print(s)
#         print(s.__context__)




# class SensorError(Exception):
#     pass

# try:
#     int(input("Enter value: "))
# except ValueError as e:
#     try:
#         raise SensorError("Invalid sensor reading") from e
#     except SensorError as s:
#         print(s)
#         print(s.__traceback__)





# class SensorError(Exception):
#     pass

# try:
#     int(input("Enter value: "))
# except ValueError as e:
#     try:
#         raise SensorError("Invalid sensor reading") from e
#     except SensorError as s:
#         print(s)
#         print(s.args)