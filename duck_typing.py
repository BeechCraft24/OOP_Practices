class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


class Person:
    def speak(self):
        print("Hello")
        
def make_it_speak(obj):
    obj.speak()

dog = Dog()
cat = Cat()
person = Person()

make_it_speak(dog)
make_it_speak(cat)
make_it_speak(person)