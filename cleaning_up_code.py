from datetime import datetime

class LegacyMeta(type):
    classes_created = []

    def __new__(mcs, name, bases, dictionary):
        dictionary["instantiation_time"] = datetime.now()

        def get_instantiation_time(self):
            return self.instantiation_time
        
        dictionary["get_instantiation_time"] = get_instantiation_time
        mcs.classes_created.append(name)
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class LegacyUser(metaclass=LegacyMeta):
    pass

class LegacyOrder(metaclass=LegacyMeta):
    pass

class LegacyPayment(metaclass=LegacyMeta):
    pass

user = LegacyUser()
order = LegacyOrder()
payment = LegacyPayment()

print(user.get_instantiation_time())
print(order.get_instantiation_time())
print(payment.get_instantiation_time())
print("Classes created by LegacyMeta:")
print(LegacyMeta.classes_created)