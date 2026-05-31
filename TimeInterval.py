# class TimeInterval:

#     def __init__(self, *, hours=0, minutes=0, seconds=0):

#         # type validation
#         if not isinstance(hours, int):
#             raise TypeError("hours must be int")

#         if not isinstance(minutes, int):
#             raise TypeError("minutes must be int")

#         if not isinstance(seconds, int):
#             raise TypeError("seconds must be int")

#         # convert everything to total seconds
#         self.total_seconds = hours * 3600 + minutes * 60 + seconds

#     def __str__(self):

#         total = self.total_seconds

#         hours = total // 3600
#         total %= 3600

#         minutes = total // 60
#         seconds = total % 60

#         return f"{hours:02}:{minutes:02}:{seconds:02}"

#     def __add__(self, other):

#         if not isinstance(other, TimeInterval):
#             raise TypeError("Can only add TimeInterval")

#         return TimeInterval(
#             seconds=self.total_seconds + other.total_seconds
#         )

#     def __sub__(self, other):

#         if not isinstance(other, TimeInterval):
#             raise TypeError("Can only subtract TimeInterval")

#         return TimeInterval(
#             seconds=self.total_seconds - other.total_seconds
#         )

#     def __mul__(self, value):

#         if not isinstance(value, int):
#             raise TypeError("Multiplier must be int")

#         return TimeInterval(
#             seconds=self.total_seconds * value
#         )


# # TESTS

# t1 = TimeInterval(hours=1, minutes=20, seconds=30)
# t2 = TimeInterval(hours=0, minutes=40, seconds=15)

# print("t1 =", t1)
# print("t2 =", t2)

# print("Addition:", t1 + t2)
# print("Subtraction:", t1 - t2)
# print("Multiplication:", t1 * 2)






# class TimeInterval:

#     def __init__(self, *, hours=0, minutes=0, seconds=0):

#         if not isinstance(hours, int):
#             raise TypeError("hours must be int")

#         if not isinstance(minutes, int):
#             raise TypeError("minutes must be int")

#         if not isinstance(seconds, int):
#             raise TypeError("seconds must be int")

#         self.total_seconds = (
#             hours * 3600 +
#             minutes * 60 +
#             seconds
#         )

#     def __str__(self):

#         total = self.total_seconds

#         hours = total // 3600
#         total %= 3600

#         minutes = total // 60
#         seconds = total % 60

#         return f"{hours:02}:{minutes:02}:{seconds:02}"

#     def __add__(self, other):

#         # TimeInterval + TimeInterval
#         if isinstance(other, TimeInterval):

#             return TimeInterval(
#                 seconds=self.total_seconds + other.total_seconds
#             )

#         # TimeInterval + int
#         elif isinstance(other, int):

#             return TimeInterval(
#                 seconds=self.total_seconds + other
#             )

#         else:
#             raise TypeError("Unsupported type for addition")

#     def __sub__(self, other):

#         # TimeInterval - TimeInterval
#         if isinstance(other, TimeInterval):

#             return TimeInterval(
#                 seconds=self.total_seconds - other.total_seconds
#             )

#         # TimeInterval - int
#         elif isinstance(other, int):

#             return TimeInterval(
#                 seconds=self.total_seconds - other
#             )

#         else:
#             raise TypeError("Unsupported type for subtraction")

#     def __mul__(self, value):

#         if not isinstance(value, int):
#             raise TypeError("Multiplier must be int")

#         return TimeInterval(
#             seconds=self.total_seconds * value
#         )





