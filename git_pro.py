def hello():
    return "Hello World!"

class Person():

    def __init__(self, name="Jose", age=20):
        self.name = name
        self.age = age

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def __str__(self):
        return f"My name is {self.name} and age is {self.age}"