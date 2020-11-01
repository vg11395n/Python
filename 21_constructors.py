class Point:
    # This method is used to create a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10, 20)
print(point.x)


class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


obj = Person("John Smith")
print(obj.name)
obj.talk()
