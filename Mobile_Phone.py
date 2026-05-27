class MobilePhone:

    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f"mobile phone {self.number} is turned on"

    def turn_off(self):
        return "mobile phone is turned off"

    def call(self, number):
        return f"calling {number}"

# creating two objects
phone1 = MobilePhone("01632-960004")
phone2 = MobilePhone("01632-960012")

# sequence of method calls
print(phone1.turn_on())
print(phone1.call("555-34343"))

print(phone2.turn_on())
print(phone2.call("555-34343"))

# turning off both phones
print(phone1.turn_off())
print(phone2.turn_off())