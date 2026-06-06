# from datetime import datetime

# def timestamp_decorator(function):
#     def wrapper(*args):
#         current_time = datetime.now()
#         formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

#         print("Function executed at:", formatted_time)

#         result = function(*args)
#         return result

#     return wrapper

# @timestamp_decorator
# def add(a, b):
#     return a + b

# @timestamp_decorator
# def multiply(a, b):
#     return a * b

# @timestamp_decorator
# def subtract(a, b):
#     return a - b

# print(add(5, 3))
# print(multiply(4, 6))
# print(subtract(10, 7))





# def simple_decorator(own_function):

#     def internal_wrapper(*args, **kwargs):
#         print('"{}" was called with the following arguments'.format(own_function.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         own_function(*args, **kwargs)
#         print('Decorator is still operating')

#     return internal_wrapper





class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')

@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
