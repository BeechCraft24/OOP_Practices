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