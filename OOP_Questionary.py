# import abc

# @abc.abstractclass   #there is no abstractclass decorator declared in this module 
# class BluePrint(abc.ABC):
#     @abc.abstractmethod
#     def hello(self):
#         pass
        
# class WhitePool(BluePrint):
#     def hello(self):
#         print("Hello from WhitePool")

# wp = WhitePool()
# wp.hello()         



# from abc import ABC, abstractmethod

# class BluePrint(ABC):
#     @abstractmethod
#     def hello(self):
#         pass

# class WhitePool(BluePrint):
#     def hello(self):
#         print("Hello from WhitePool")

# wp = WhitePool()
# wp.hello()



import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class WhitePool(BluePrint):
    def hello(self):
        print("Hello from WhitePool")

wp = WhitePool()
wp.hello()



# class OwnMath(Exception):
#     pass

# def calculate_value(numerator, denominator):
#     try:
#         value = numerator / denominator
#     except ZeroDivisionError as e:
#         raise OwnMath from e
#     return value
# calculate_value(4, 0)   #Why this is explicitly chained exception?