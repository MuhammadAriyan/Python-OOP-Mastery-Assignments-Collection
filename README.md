# 🧠 Python OOP Mastery – 21 Core Assignments

> **Author**: Muhammad Aryan  
> **Date**: May 19, 2025  
> **Assignment Name**: Python Object-Oriented Programming (OOP) – Core Principles & Applications  
> **Objective**: Grasp the essence of OOP in Python through 21 practical, real-world examples and concepts.

---

## 📚 Assignment Index (21 Total)

### 1️⃣ Using `self`
Create a `Student` class with `name` and `marks`, initialized via `self` in the constructor. Includes `display()` method.

### 2️⃣ Using `cls`
Implement a `Counter` class with a class variable. Use `@classmethod` to track and display number of instances.

### 3️⃣ Public Variables and Methods
Build a `Car` class with a public variable `brand` and public method `start()`. Show how to access both from outside.

### 4️⃣ Class Variables & Class Methods
Create a `Bank` class with a class variable `bank_name`. Add `change_bank_name()` using `@classmethod` to update it.

### 5️⃣ Static Methods
Create `MathUtils` with a static method `add(a, b)` to return the sum of two numbers.

### 6️⃣ Constructors and Destructors
Design a `Logger` class that prints messages when an instance is created and destroyed.

### 7️⃣ Access Modifiers
In `Employee`, demonstrate:
- `name` (public)
- `_salary` (protected)
- `__ssn` (private, accessed via name mangling)

### 8️⃣ Using `super()`
Create a `Person` class with a constructor. Subclass `Teacher` uses `super()` to inherit and extend functionality with `subject`.

### 9️⃣ Abstract Classes
Use `abc.ABC` to create an abstract `Shape` class with `area()`. Implement it in `Rectangle`.

### 🔟 Class Method: Book Counter
Build a `Book` class with a class variable `total_books`. Use `@classmethod` to increment the count.

### 1️⃣1️⃣ Static Method: Temperature Conversion
Create `TemperatureConverter` with a static method to convert Celsius to Fahrenheit.

### 1️⃣2️⃣ Composition
Use `Car` and `Engine` classes to demonstrate composition—Engine object exists within Car.

### 1️⃣3️⃣ Aggregation
Use `Department` and `Employee` to model aggregation—a Department holds Employee references.

### 1️⃣4️⃣ Method Resolution Order (MRO)
Build a diamond inheritance structure: `A`, `B`, `C`, and `D(B, C)`. Show method resolution using `__mro__`.

### 1️⃣5️⃣ Function Decorators
Write a function decorator `log_function_call` that announces when a function is being called.

### 1️⃣6️⃣ Class Decorators
Create a class decorator `add_greeting` that dynamically injects a `greet()` method into the class.

### 1️⃣7️⃣ @property, @setter, @deleter
Define a `Product` class with private `_price` and use property decorators to manage access and deletion.

### 1️⃣8️⃣ Callable Classes
Create a `Multiplier` class with a `__call__()` method, enabling objects to be used like functions.

### 1️⃣9️⃣ Custom Exceptions
Implement `InvalidAgeError` and raise it in `check_age(age)` if age < 18. Use try-except to handle it.

### 2️⃣0️⃣ Iterable Object: Countdown
Build a `Countdown` class that implements `__iter__()` and `__next__()` to count down from a start value to 0.

### 2️⃣1️⃣ Final Integration & Mastery
A review-worthy final structure demonstrating every aspect of OOP in an integrated and interconnected way. This includes:
- Clean object instantiation
- Property decorators
- MRO logic
- Decorators (function/class)
- Custom exceptions
- Composition and Aggregation

---

## ⚙️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/python-oop-mastery.git
cd python-oop-mastery
