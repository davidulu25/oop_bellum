from collections.abc import Iterable
from abc import ABC, abstractmethod

#creating a class in python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says hello!"

# creating a subclass (Inheritance)
class Eagle(Animal):
    def speak(self):
        return "!!!"

# using the super() function
class Cow(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

# Encapsulation - private members
class TestClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

# Polymorphism - using inbuilt Abstract Base Classes (ABC)
# 1
def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"

# 2
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width  = width
    
    def area(self):
        return self.length * self.width

class Circular(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.142 * self.radius**2

def print_area(shape):
    print(f"Area of shape: {shape.area()}")

# defining an abstract base class
class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!"

# using class methods and static methods
class School:
    @classmethod
    def class_method(cls):
        return "Class method called"
    
    @staticmethod
    def static_method():
        return "Static method called"

class Knowledge:
    class_variable = "I'm a class variable"

    @classmethod
    def class_method(cls):
        return f"This is a class method, class variable = {cls.class_variable}"
    
    @staticmethod
    def static_method():
        return "This is a static method, I cannot access class variables."

# operator overloading in python
class Mango:
    def __init__(self, x):
        self.x = str(x)
    
    def __add__(self, other):
        return self.x + other.x

# using special methods for string representations
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person: {self.name}, {self.age}"

#using composition in OOP in python
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# using multiple inheritance
class Parent1:
    def method1(self):
        return "Parent1's method called"

class Parent2:
    def method2(self):
        return "Parent2's method called"

class Child(Parent1, Parent2):
    pass

# implementing `decorators within classes`
class CoffeeShop:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, item, price):
        self.menu[item] = price

    # This class decorator is used to check if an item is available on the menu
    def item_available(method):
        def order_processor(self, item, *args, **kwargs):
            if item not in self.menu:
                print(f"Sorry, {item} is not available.")
                return
            return method(self, item, *args, **kwargs)
        return order_processor

    # This method uses the above decorator to serve items
    @item_available
    def serve(self, item):
        print(f"Serving {item} for {self.menu[item]}!")

# creating a Singleton class in python
class Singleton:
    _instance = None

    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This is a singleton class!")
        else:
            Singleton._instance = self

# using Mixin classes in Python
class Mixin1(object):
    def test(self):
        print("Mixin1")

class Mixin2(object):
    def test(self):
        print("Mixin2")

class MyClass(Mixin1, Mixin2):
    pass