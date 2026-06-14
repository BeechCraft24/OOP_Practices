# try:
#     import abcdefghijk

# except ImportError as e:
#     print(e.args)
#     print(e.name)
#     print(e.path)


# class RocketNotReadyError(Exception):
#     pass

# def personnel_check():
#     try:
#         print("\tThe captain's name is", crew[0])
#         print("\tThe pilot's name is", crew[1])
#         print("\tThe mechanic's name is", crew[2])
#         print("\tThe navigator's name is", crew[3])
#     except IndexError as e:
#         raise RocketNotReadyError('Crew is incomplete') from e

# crew = ['John', 'Mary', 'Mike']
# print('Final check procedure')
# personnel_check()




# class RocketNotReadyError(Exception):
#     pass

# def personnel_check():
#     try:
#         print("\tThe captain's name is", crew[0])
#         print("\tThe pilot's name is", crew[1])
#         print("\tThe mechanic's name is", crew[2])
#         print("\tThe navigator's name is", crew[3])
#     except IndexError as e:
#         raise RocketNotReadyError('Crew is incomplete') from e

# def fuel_check():
#     try:
#         print('Fuel tank is full in {}%'.format(100 / 0))
#     except ZeroDivisionError as e:
#         raise RocketNotReadyError('Problem with fuel gauge') from e

# crew = ['John', 'Mary', 'Mike']
# fuel = 100
# check_list = [personnel_check, fuel_check]

# print('Final check procedure')

# for check in check_list:
#     try:
#         check()
#     except RocketNotReadyError as f:
#         print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))





# class SensorError(Exception):
#     pass

# def parameters_check():
#     try:
#         print("\tVoltage 1 is", readings[0])
#         print("\tVoltage 2 is", readings[1])
#         print("\tVoltage 3 is", readings[2])
#         print("\tVoltage 4 is", readings[3])
#     except IndexError as e:
#         raise SensorError('Readings are incomplete') from e

# def temperature_check():
#     try:
#         print('Temperature is {} degrees'.format(100 / 0))
#     except ZeroDivisionError as e:
#         raise SensorError('Problem with temperature vessel') from e

# readings = [12.5, 5, 4.5, 3]
# check_list = [parameters_check, temperature_check]

# print('Final check procedure')

# for check in check_list:
#     try:
#         check()
#     except SensorError as f:
#         print('SensorError exception: "{}", caused by "{}"'.format(f, f.__cause__))





# class SensorError(Exception):
#     pass

# def parameters_check():
#     if len(readings) < 4:
#         raise SensorError("Readings are incomplete")

#     for i, reading in enumerate(readings):
#         print(f"Voltage {i+1} is {reading}")

# def temperature_check():
#     try:
#         for i, reading in enumerate(readings):
#             print('Temperature {} is {} degrees'.format(i + 1, 100 / reading))
#     except ZeroDivisionError as e:
#         raise SensorError('Problem with temperature vessel') from e

# readings = []
# readings.append(float(input("Enter voltage 1: ")))
# readings.append(float(input("Enter voltage 2: ")))
# readings.append(float(input("Enter voltage 3: ")))
# readings.append(float(input("Enter voltage 4: ")))

# check_list = [parameters_check, temperature_check]

# print('Final check procedure')

# for check in check_list:
#     try:
#         check()
#     except SensorError as f:
#         print('SensorError exception: "{}", caused by "{}"'.format(f, f.__cause__))






class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        for i, reading in enumerate(readings):
            print('The result of the division is {}'.format(i + 1, 100 / reading))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with battery readings') from e

readings = []
readings.append(float(input("Enter voltage 1: ")))
readings.append(float(input("Enter voltage 2: ")))
readings.append(float(input("Enter voltage 3: ")))
readings.append(float(input("Enter voltage 4: ")))

def circuits_check():
    try:
        for i, reading in enumerate(readings): 
            if reading == 0:
                raise ZeroDivisionError('Voltage reading is zero')
            else:
                print('Continuity has been checked for voltage {}'.format(i + 1))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with circuit {}'.format(i + 1)) from e

readings = []
readings.append(float(input("Enter voltage 1: ")))
readings.append(float(input("Enter voltage 2: ")))
readings.append(float(input("Enter voltage 3: ")))
readings.append(float(input("Enter voltage 4: ")))

crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
