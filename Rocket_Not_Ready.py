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