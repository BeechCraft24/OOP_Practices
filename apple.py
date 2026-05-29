import random


class Apple:

    # class variables
    counter = 0
    total_weight = 0

    def __init__(self):

        # random weight between 0.2 and 0.5
        self.weight = random.uniform(0.2, 0.5)

        # update class variables
        Apple.counter += 1
        Apple.total_weight += self.weight


# packaging process
apples = []

while Apple.counter < 1000 and Apple.total_weight <= 300:

    apple = Apple()

    # stop immediately if weight exceeded
    if Apple.total_weight > 300:
        break

    apples.append(apple)


print("Packaging process stopped")
print("Number of apples:", Apple.counter)
print("Total weight:", round(Apple.total_weight, 2))