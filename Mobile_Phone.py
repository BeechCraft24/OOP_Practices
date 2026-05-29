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
# phone1 = MobilePhone("01632-960004")
# phone2 = MobilePhone("01632-960012")
# # sequence of method calls
# print(phone1.turn_on())
# print(phone1.call("555-34343"))
# print(phone2.turn_on())
# print(phone2.call("555-34343"))
# # turning off both phones
# print(phone1.turn_off())
# print(phone2.turn_off())


# class Demo:
#     def __init__(self, value):
#         self.instance_var = value
# d1 = Demo(100)
# d2 = Demo(200)
# print("d1's instance variable is equal to:", d1.instance_var)
# print("d2's instance variable is equal to:", d2.instance_var)


# class Demo:
#     def __init__(self, value):
#         self.instance_var = value
# d1 = Demo("100")
# d2 = Demo("200")
# print("d1's instance variable is equal to:", d1.instance_var)
# print("d2's instance variable is equal to:", d2.instance_var)


# class Demo:
#     class_var = 'shared variable'
# print(Demo.class_var)
# print(Demo.__dict__)



# class Demo:
#     class_var = 'shared variable'
# d1 = Demo()
# d2 = Demo()
# print(Demo.class_var)
# print(d1.class_var)
# print(d2.class_var)
# print('contents of d1:', d1.__dict__)



# class Demo:
#     class_var = 'shared variable'

# d1 = Demo()
# d2 = Demo()

# # both instances allow access to the class variable
# print(d1.class_var)
# print(d2.class_var)
# print('.' * 20)

# # d1 object has no instance variable
# print('contents of d1:', d1.__dict__)
# print('.' * 20)

# # d1 object receives an instance variable named 'class_var'
# d1.class_var = "I'm messing with the class variable"

# # d1 object owns the variable named 'class_var' which holds a different value than the class variable named in the same way
# print('contents of d1:', d1.__dict__)
# print(d1.class_var)
# print('.' * 20)

# # d2 object variables were not influenced
# print('contents of d2:', d2.__dict__)

# # d2 object variables were not influenced
# print('contents of class variable accessed via d2:', d2.class_var)



# class Phone:
#     counter = 0
#     def __init__(self, number):
#         self.number = number
#         Phone.counter += 1
#     def call(self, number):
#         message = 'Calling {} using own number {}'.format(number, self.number)
#         return message
# class FixedPhone(Phone):
#     last_SN = 0
#     def __init__(self, number):
#         super().__init__(number)
#         FixedPhone.last_SN += 1
#         self.SN = 'FP-{}'.format(FixedPhone.last_SN)
# class MobilePhone(Phone):
#     last_SN = 0
#     def __init__(self, number):
#         super().__init__(number)
#         MobilePhone.last_SN += 1
#         self.SN = 'MP-{}'.format(MobilePhone.last_SN)
# print('Total number of phone devices created:', Phone.counter)
# print('Creating 2 devices')
# fphone = FixedPhone('555-2368')
# mphone = MobilePhone('01632-960004')
# print('Total number of phone devices created:', Phone.counter)
# print('Total number of mobile phones created:', MobilePhone.last_SN)
# print(fphone.call('01632-960004'))
# print('Fixed phone received "{}" serial number'.format(fphone.SN))
# print('Mobile phone received "{}" serial number'.format(mphone.SN))



# class Phone:
#     counter = 0
#     def __init__(self, number):
#         self.number = number
#         Phone.counter += 1
#     def call(self, number):
#         message = 'Calling {} using own number {}'.format(number, self.number)
#         return message
# class FixedPhone(Phone):
#     last_SN = 0
#     def __init__(self, number):
#         super().__init__(number)
#         FixedPhone.last_SN += 1
#         self.SN = 'FP-{}'.format(FixedPhone.last_SN)
# class MobilePhone(Phone):
#     last_SN = 0
#     def __init__(self, number):
#         super().__init__(number)
#         MobilePhone.last_SN += 1
#         self.SN = 'MP-{}'.format(MobilePhone.last_SN)
# print('Total number of phone devices created:', Phone.counter)
# print('Creating 2 devices')
# fphone = FixedPhone('555-2368')
# mphone = MobilePhone('01632-960004')
# print('Total number of phone devices created:', Phone.counter)
# print('Total number of mobile phones created:', MobilePhone.last_SN)
# print(fphone.call('01632-960004'))
# print('Fixed phone received "{}" serial number'.format(fphone.SN))
# print('Mobile phone received "{}" serial number'.format(mphone.SN))