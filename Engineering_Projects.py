# class Router:
#     def __init__(self, ip, hostname):
#         self.ip = ip
#         self.hostname = hostname

#     @classmethod
#     def from_config_file(cls, line):
#         ip, hostname = line.split(",")
#         return cls(ip, hostname)

# router = Router.from_config_file("192.168.1.1,CoreRouter")

# print(router.ip)
# print(router.hostname)





# class PressureSensor:
#     def __init__(self, voltage, pressure):
#         self.voltage = voltage
#         self.pressure = pressure

#     @classmethod
#     def from_adc_reading(cls, adc_value):
#         voltage = adc_value * 5 / 1023
#         pressure = voltage * 100
#         return cls(voltage, pressure)

# sensor = PressureSensor.from_adc_reading(512)

# print(sensor.voltage)
# print(sensor.pressure)




# class Employee:
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department

#     @classmethod
#     def from_database_row(cls, row):
#         return cls(row["name"], row["department"])

# db_row = {
#     "name": "Alex",
#     "department": "Engineering"
# }

# employee = Employee.from_database_row(db_row)

# print(employee.name)
# print(employee.department)




# class MaintenanceTask:
#     def __init__(self, pn, qty):
#         self.part_number = pn
#         self.quantity = qty

#     @classmethod
#     def from_barcode(cls, barcode):
#         pn, qty = barcode.split("-")
#         return cls(pn, int(qty))

# task = MaintenanceTask.from_barcode("MS24566-4")

# print(task.part_number)
# print(task.quantity)




# class Image:
#     def __init__(self, pixels):
#         self.pixels = pixels

#     @classmethod
#     def from_file(cls, filename):
#         print("Loading image from disk")
#         pixels = [1, 2, 3]
#         return cls(pixels)

# img = Image.from_file("photo.png")




# class LuxuryWatch:
#     watches_created = 0

#     def __init__(self):
#         LuxuryWatch.watches_created += 1
#         self.engraving = None

#     @classmethod
#     def get_number_of_watches_created(cls):
#         return cls.watches_created

#     @classmethod
#     def with_engraving(cls, text):
#         cls.validate_engraving(text)

#         watch = cls()
#         watch.engraving = text
#         return watch

#     @staticmethod
#     def validate_engraving(text):
#         if len(text) > 40:
#             raise ValueError("Engraving text cannot be longer than 40 characters.")

#         if not text.isalnum():
#             raise ValueError("Engraving text must contain only alphanumeric characters.")

# watch1 = LuxuryWatch()
# print(LuxuryWatch.get_number_of_watches_created())

# watch2 = LuxuryWatch.with_engraving("BestWatch2026")
# print(LuxuryWatch.get_number_of_watches_created())

# try:
#     watch3 = LuxuryWatch.with_engraving("foo@baz.com")
#     print(LuxuryWatch.get_number_of_watches_created())
# except ValueError as error:
#     print("Error:", error)

# print(LuxuryWatch.get_number_of_watches_created())





import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.scanner_resolution = "300 DPI"
        self.printer_resolution = "300 DPI"

    def scan_document(self):
        return "MFD1: Document has been scanned."

    def get_scanner_status(self):
        return f"MFD1 scanner resolution: {self.scanner_resolution}, serial number: {self.serial_number}"

    def print_document(self):
        return "MFD1: Document has been printed."

    def get_printer_status(self):
        return f"MFD1 printer resolution: {self.printer_resolution}, serial number: {self.serial_number}"

class MFD2(Scanner, Printer):
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.scanner_resolution = "600 DPI"
        self.printer_resolution = "600 DPI"
        self.history = []

    def scan_document(self):
        self.history.append("scan")
        return "MFD2: Document has been scanned."

    def get_scanner_status(self):
        return f"MFD2 scanner resolution: {self.scanner_resolution}, serial number: {self.serial_number}"

    def print_document(self):
        self.history.append("print")
        return "MFD2: Document has been printed."

    def get_printer_status(self):
        return f"MFD2 printer resolution: {self.printer_resolution}, serial number: {self.serial_number}"

    def print_history(self):
        return f"MFD2 operation history: {self.history}"

class MFD3(Scanner, Printer):
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.scanner_resolution = "1200 DPI"
        self.printer_resolution = "2400 DPI"
        self.history = []

    def scan_document(self):
        self.history.append("scan")
        return "MFD3: Document has been scanned."

    def get_scanner_status(self):
        return f"MFD3 scanner resolution: {self.scanner_resolution}, serial number: {self.serial_number}"

    def print_document(self):
        self.history.append("print")
        return "MFD3: Document has been printed."

    def get_printer_status(self):
        return f"MFD3 printer resolution: {self.printer_resolution}, serial number: {self.serial_number}"

    def print_history(self):
        return f"MFD3 operation history: {self.history}"

    def fax_document(self):
        self.history.append("fax")
        return "MFD3: Document has been faxed."

mfd1 = MFD1("MFD1-001")
mfd2 = MFD2("MFD2-001")
mfd3 = MFD3("MFD3-001")

devices = [mfd1, mfd2, mfd3]

for device in devices:
    print(device.scan_document())
    print(device.print_document())
    print(device.get_scanner_status())
    print(device.get_printer_status())
    print()

print(mfd2.print_history())
print(mfd3.fax_document())
print(mfd3.print_history())





class RouterConfig:
    def __init__(self):
        self.__ip_address = "192.168.1.1"

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):

        if value.count(".") != 3:
            raise ValueError("Invalid IP address")

        self.__ip_address = value

router = RouterConfig()

router.ip_address = "101.0.0.1"
print(router.ip_address)