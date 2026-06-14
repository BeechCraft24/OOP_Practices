from copy import copy, deepcopy

class Delicacy:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name}, price={self.price}, weight={self.weight}"

candy1 = Delicacy("Chocolate", 1.0, 601)
candy2 = copy(candy1)       # shallow copy
candy3 = deepcopy(candy1)   # deep copy

print(candy1)
print(candy2)
print(candy3)