# class Duck:
#     def __init__(self, height, weight, sex):
#         self.height = height
#         self.weight = weight
#         self.sex = sex

#     def walk(self):
#         pass

#     def quack(self):
#         return print('Quack')

# duckling = Duck(height=10, weight=3.4, sex="male")
# drake = Duck(height=25, weight=3.7, sex="male")
# hen = Duck(height=20, weight=3.4, sex="female")

# drake.quack()
# print(duckling.height)



# class Duck:
#     def __init__(self, height, weight, sex):
#         self.height = height
#         self.weight = weight
#         self.sex = sex
#     def walk(self):
#         pass
#     def quack(self):
#         return print('Quack')
# duckling = Duck(height=10, weight=3.4, sex="male")
# drake = Duck(height=25, weight=3.7, sex="male")
# hen = Duck(height=20, weight=3.4, sex="female")
# print(Duck.__class__)
# print(duckling.__class__)
# print(duckling.sex.__class__)
# print(duckling.quack.__class__)


# class MobilePhone:

#     def __init__(self, number):
#         self.number = number

#     def turn_on(self):
#         return f"mobile phone {self.number} is turned on"

#     def turn_off(self):
#         return "mobile phone is turned off"

#     def call(self, number):
#         return f"calling {number}"

# # creating two objects
# phone1 = MobilePhone("305-555-1234")
# phone2 = MobilePhone("786-555-9876")

# # sequence of method calls
# print(phone1.turn_on())
# print(phone1.call("111-222-3333"))

# print(phone2.turn_on())
# print(phone2.call("999-888-7777"))

# # turning off both phones
# print(phone1.turn_off())
# print(phone2.turn_off())