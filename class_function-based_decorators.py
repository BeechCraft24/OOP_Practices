# class SimpleDecorator:
#     def __init__(self, own_function):
#         self.func = own_function
#     def __call__(self, *args, **kwargs):
#         print("Before")
#         self.func(*args, **kwargs)
#         print("After")

# @SimpleDecorator
# def combiner():
#     pass
# combiner()




# def SimpleDecorator(own_function):
#     def internal_wrapper(*args, **kwargs):
#         print("Before")
#         own_function(*args, **kwargs)
#         print("After")
#     return internal_wrapper

# @SimpleDecorator
# def combiner():
#     pass
# combiner()




# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.count = 0

#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print("Call number:", self.count)
#         return self.func(*args, **kwargs)
    
# @CountCalls
# def hello():
#     print("Hello")
# hello()
# hello()
# hello()





# import time

# class Timer:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start:.4f} seconds")
#         return result

# @Timer
# def slow_function():
#     time.sleep(2)
#     print("Finished task")
# slow_function()



# class Car:
#     def __init__(self, VIN):
#         self.mileage = 0
#         self.VIN = VIN

# car = Car('ABC123')
# print('The mileage is', car.mileage)
# print('The VIN is', car.VIN)




# def object_counter(class_):
#     class_.__getattr__orig = class_.__getattribute__

#     def new_getattr(self, name):
#         if name == 'mileage':
#             print('We noticed that the mileage attribute was read')
#         return class_.__getattr__orig(self, name)

#     class_.__getattribute__ = new_getattr
#     return class_

# @object_counter
# class Car:
#     def __init__(self, VIN):
#         self.mileage = 0
#         self.VIN = VIN
# car = Car('ABC123')
# print('The mileage is', car.mileage)
# print('The VIN is', car.VIN)




# class Car:
#     def __init__(self, vin):
#         print('Ordinary __init__ was called for', vin)
#         self.vin = vin
#         self.brand = ''

#     @classmethod
#     def including_brand(cls, vin, brand):
#         print('Class method was called')
#         _car = cls(vin)
#         _car.brand = brand
#         return _car

# car1 = Car('ABCD1234')
# car2 = Car.including_brand('DEF567', 'NewBrand')

# print(car1.vin, car1.brand)
# print(car2.vin, car2.brand)




class Router:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    @classmethod
    def from_config_file(cls, line):
        ip, hostname = line.split(",")
        return cls(ip, hostname)

router = Router.from_config_file("192.168.1.1,CoreRouter")

print(router.ip)
print(router.hostname)