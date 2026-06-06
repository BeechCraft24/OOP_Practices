# def simple_hello():
#     print("Hello from simple function!")

# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function

# decorated = simple_decorator(simple_hello)
# decorated()




# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function

# @simple_decorator
# def simple_hello():
#     print("Hello from simple function!")

# simple_hello()




# def simple_decorator(own_function):

#     def internal_wrapper(*args, **kwargs):
#         print('"{}" was called with the following arguments'.format(own_function.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         own_function(*args, **kwargs)
#         print('Decorator is still operating')

#     return internal_wrapper

# @simple_decorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)

# combiner('a', 'b', exec='yes')





# def simple_decorator(own_function):

#     def internal_wrapper(*args, **kwargs):
#         print('"{}" was called with the following arguments'.format(own_function.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         own_function(*args, **kwargs)
#         print('Decorator is still operating')
#     return internal_wrapper

# @simple_decorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)
# combiner('a', 'b', exec='yes')




# def logger(original_function):

#     def wrapper():
#         print("Before calling the function")
#         original_function()
#         print("After calling the function")
#     return wrapper

# @logger
# def hello():
#     print("Hello from original function")
# hello()




# def require_admin(func):

#     def wrapper(user):
#         if user != "admin":
#             print("Access denied")
#             return
#         return func(user)
#     return wrapper

# @require_admin
# def delete_logs(user):
#     print("Logs deleted")
# delete_logs("admin")
# delete_logs("user")




# def audit(func):
#     def wrapper(*args, **kwargs):
#         print("AUDIT:", func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# @audit
# def open_port(port):
#     print("Opening port", port)
# open_port(8080)





# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper

# @warehouse_decorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)

# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)

# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')






# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper

# @warehouse_decorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)

# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)

# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')





# def warehouse_decorator(x):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('Wrapping items from {} with {}'.format(our_function.__name__, x))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper

# @warehouse_decorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)

# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)

# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')






def big_container(y):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('The whole order would be packed with', y)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(x):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('Wrapping items from {} with {}'.format(our_function.__name__, x))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
