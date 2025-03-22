class Animals():
    age = 3
    classification = "none"
    cbd = "unknown"
class Cat(Animals):
    classification = "Mammalia"
    cbd = "Yes"
    def __init__(self):
        print(self.age)
        print(self.classification)
        print(self.cbd)
class FlyingSquirrel(Animals):
    age = "2"
    classification = "Mammalia"
    cbd = "Yes"
    def __init__(self):
        print(self.age)
        print(self.classification)
        print(self.cbd)
class AlbinoSnake(Animals):
    classification = "Reptilia"
    cbd = "No"
    def __init__(self):
        print(self.age)
        print(self.classification)
        print(self.cbd)
cat = Cat()
fs = FlyingSquirrel()
als = AlbinoSnake()

# Примітка: cbd означає чи можна тримати цю тварину вдома
