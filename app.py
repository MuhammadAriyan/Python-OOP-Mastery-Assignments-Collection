# Author: MUHAMMAD ARYAN
# Date: 2023-10-05
# Description: This is a file containing Python code examples for tasks related to OOP.

''' 1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} got {self.marks} marks")
        
'''
2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the coun'''


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod # class method
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

'''
3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
'''        
class Car:
    def __init__(self, brand):
        self.brand = brand # public variable

    def start(self): # public method
        print(f"{self.brand} is starting.")
        
# Instantiate the classes and call car methods and attribute

bmwM5 = Car("BMW M5")
bmwM5.start() # Output : BMW M5 is starting.
print(bmwM5.brand) # Output: BMW M5

'''
4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.'''

class Bank:
    bank_name = "Chocolate Bank"

    @classmethod # class method
    def change_bank_name(cls, name):
        cls.bank_name = name
        
bank = Bank()
print(bank.bank_name) # Output: Chocolate Bank
bank.change_bank_name("ARY Bank")
print(bank.bank_name) # Output: ARY Bank

'''

5. Static Variables and Static Methods

Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.'''

class MathUtils:
    @staticmethod # static method
    def add(a, b):
        return a + b
    
'''
6. Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
'''

class Logger:
    def __init__(self):
        print("Generated an Instance ☁")

    def __del__(self):
        print("Terminated an Instance 🔪")
        
        
'''
7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
'''

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")
        
        
aryan = Employee("Muhammad Aryan", 100000, "123-45-6789")
print(aryan.name) # Output: Muhammad Aryan
print(aryan._salary) # Output: 100000
# print(aryan.__ssn) # Raises AttributeError: 'Employee' object has no attribute '__ssn'
# Accessing private variable using name mangling
print(aryan._Employee__ssn) # Output: 123-45-6789
aryan.display() # Output: Name: Muhammad Aryan, Salary: 100000, SSN: 123-45-6789

'''
8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

'''

class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):  
    def __init__(self, name, subject):
        super().__init__(name) # Call the base class constructor
        self.subject = subject
        
'''
9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
'''
11. Class Methods
Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
'''

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"there are {cls.total_books} books 📚")
        
'''
12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
'''

class TemperatureConverter:
    @staticmethod # static method
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
'''
13. Composition
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
'''
class Engine:
    def start(self):
        print("Engine started.")
        
class Car:
    def __init__(self, engine):
        self.engine = Engine() # Composition

    def start(self):
        self.engine.start() # Accessing Engine's method
        print("Car is ready to go.")
        
'''
14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

'''

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [] # List to hold Employee objects

    def add_employee(self, employee):
        self.employees.append(employee) # Aggregation
        
class Employee:
    def __init__(self, name):
        self.name = name
        
'''
15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
'''

class A:                   # ---
    def show(self):        #   |
        print("Class A")   #   |
                           #   |
class B(A):                # <-|          <--
    def show(self):        #   |            |
        print("Class B")   #   |            |
                           #   |            |
class C(A):                #  <-          <-- 
    def show(self):        #                |
        print("Class C")   #                |
                           #                |
class D(B, C): # diamond inheritance    <---- 
    def show(self):        
        print("Class D")   
        
# Create an object of D and call show()
d = D()
print(d.show()) # Output: Class D
mro = D.__mro__
print(mro) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


'''
16. Function Decorators
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
'''
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper
        

@log_function_call
def say_hello():
    print('hello')

'''
17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
'''

class add_greeting:
    def __init__(self,cls):
        self._cls = cls
    
    @classmethod
    def greet(cls):
        return "Hello from Decorator!"
    
    def __call__(self, *args, **kwargs):
        self._cls.greet = self.greet
        return self._cls(*args, **kwargs)


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        
pers = Person("Aryan")
print(pers.greet()) # Output: Hello from Decorator!

'''
18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
'''

class Product:
    def __init__(self, price):
        self.__price = price # private attribute

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self.__price
        
        
# Example usage
product = Product(100)
print(product.price) # Output: 100
product.price = 150
print(product.price) # Output: 150
del product.price


'''
19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

'''

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
    
nine = Multiplier(9)

for i in range(10):
    print(nine(i+1)) # Output: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90
    
'''
    20. Creating a Custom Exception
    Assignment:
    Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

'''

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be at least 18.")
        else:
            print("Age is valid.")
    except InvalidAgeError as e:
        print(e)
        
a= check_age(16) # Output: Age must be at least 18.
        
'''
21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
'''

class Countdown:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

countdown = Countdown(5)
for number in countdown:
    print(number) # Output: 5, 4, 3, 2, 1, 0