# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         obj = super().__new__(mcs, name, bases, dictionary)
#         obj.custom_attribute = 'Added by My_Meta'
#         return obj

# class My_Object(metaclass=My_Meta):
#     pass

# print(My_Object.__dict__)



# class SensorMeta(type):

#     def __new__(mcs, name, bases, dct):

#         if "unit" not in dct:
#             raise TypeError(f"{name} must define a unit")

#         return super().__new__(mcs, name, bases, dct)
    
# class PressureSensor(metaclass=SensorMeta):
#     unit = "Pa"
#     pass




# def greetings(self):
#     print('Just a greeting function, but it could be something more serious like a check sum')

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if 'greetings' not in dictionary:
#             dictionary['greetings'] = greetings
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     def greetings(self):
#         print('We are ready to greet you!')

# myobj1 = My_Class1()
# myobj1.greetings()
# myobj2 = My_Class2()
# myobj2.greetings()




# def add(self, a, b):
#     print(f"{a} + {b} = {a + b}")

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if "add" not in dictionary:
#             dictionary["add"] = add
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     def add(self, a, b):
#         print(f"Custom addition: {a+b}")

# myobj1 = My_Class1()
# myobj1.add(10, 20)
# myobj2 = My_Class2()
# myobj2.add(10, 20)



# def add(self, a, b):
#     print(f"{a} + {b} = {a + b}")

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if "add" not in dictionary:
#             dictionary["add"] = add
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     pass

# myobj1 = My_Class1()
# myobj1.add(10, 20)
# myobj2 = My_Class2()
# myobj2.add(10, 20)




# def add(self, a, b):
#     return a + b

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if "add" not in dictionary:
#             dictionary["add"] = add
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     list = []
#     list.append(add)
    
# myobj1 = My_Class1()
# myobj1.add(10, 20)
# myobj2 = My_Class2()
# result = myobj2.add(10, 20)
# My_Class2.list.append(result)
# print(My_Class2.list)




def add(self, a, b):
    return a + b

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if "add" not in dictionary:
            dictionary["add"] = add
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):   #Created with My_Meta, so it gets the add method, but it doesn't have a list attribute
    pass                              #And we don't use this class in the rest of the code, so it doesn't affect anything

class My_Class2(metaclass=My_Meta):
    list = []
    
obj1 = My_Class2()
result = obj1.add(10, 20)
My_Class2.list.append(result)
print(My_Class2.list)