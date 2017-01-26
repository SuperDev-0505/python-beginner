"""
Classes and Objects - Object-Oriented Programming
Learn how to create classes and work with objects in Python.

Updated: Added inheritance and polymorphism examples.
"""

# ============================================
# 1. BASIC CLASS AND OBJECT
# ============================================

print("=== Basic Class and Object ===\n")

class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, age):
        """Initialize a Dog with name and age."""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Get information about the dog."""
        return f"{self.name} is {self.age} years old"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.get_info())

# ============================================
# 2. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================

print("\n=== Class vs Instance Attributes ===\n")

class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"Car 1: {car1.get_info()}, Wheels: {car1.wheels}")
print(f"Car 2: {car2.get_info()}, Wheels: {car2.wheels}")

# Changing class attribute affects all instances
Car.wheels = 6
print(f"\nAfter changing class attribute:")
print(f"Car 1 wheels: {car1.wheels}")
print(f"Car 2 wheels: {car2.wheels}")

# ============================================
# 3. METHODS
# ============================================

print("\n=== Methods ===\n")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get the current balance."""
        return f"Balance: ${self.balance}"

account = BankAccount("Alice", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

# ============================================
# 4. INHERITANCE
# ============================================

print("\n=== Inheritance ===\n")

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

# Child class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    def make_sound(self):
        return "Meow!"
    
    def get_info(self):
        return f"{self.name} is a {self.breed} {self.species}"

# Another child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"

cat = Cat("Whiskers", "Persian")
dog = Dog("Buddy", "Golden Retriever")

print(cat.get_info())
print(cat.make_sound())
print(dog.get_info())
print(dog.make_sound())

# ============================================
# 5. ENCAPSULATION (PRIVATE ATTRIBUTES)
# ============================================

print("\n=== Encapsulation ===\n")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self._protected_attr = "Protected"  # Convention: protected
        self.__private_attr = "Private"      # Name mangling: private
        self.__student_id = student_id
    
    def get_student_id(self):
        """Public method to access private attribute."""
        return self.__student_id
    
    def set_student_id(self, new_id):
        """Public method to modify private attribute."""
        if len(str(new_id)) > 0:
            self.__student_id = new_id
        else:
            print("Invalid student ID")

student = Student("Alice", "S12345")
print(f"Name: {student.name}")
print(f"Student ID (via method): {student.get_student_id()}")
student.set_student_id("S67890")
print(f"New Student ID: {student.get_student_id()}")

# ============================================
# 6. SPECIAL METHODS (MAGIC METHODS)
# ============================================

print("\n=== Special Methods ===\n")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users."""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return the number of pages."""
        return self.pages
    
    def __eq__(self, other):
        """Check if two books are equal."""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Python Basics", "John Doe", 250)

print(f"Book 1: {book1}")
print(f"Book 1 (repr): {repr(book1)}")
print(f"Pages: {len(book1)}")
print(f"Are books equal? {book1 == book2}")

# ============================================
# 7. STATIC METHODS AND CLASS METHODS
# ============================================

print("\n=== Static and Class Methods ===\n")

class MathUtils:
    # Class attribute
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance."""
        return a + b
    
    @classmethod
    def get_pi(cls):
        """Class method - works with class, not instance."""
        return cls.pi
    
    @classmethod
    def circle_area(cls, radius):
        """Calculate circle area using class method."""
        return cls.pi * radius ** 2

# Using static method (no instance needed)
print(f"5 + 3 = {MathUtils.add(5, 3)}")

# Using class method
print(f"Pi value: {MathUtils.get_pi()}")
print(f"Circle area (radius=5): {MathUtils.circle_area(5)}")

# ============================================
# 8. PROPERTIES (GETTERS AND SETTERS)
# ============================================

print("\n=== Properties ===\n")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 77
print(f"\nAfter setting to 77°F:")
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

# ============================================
# 9. PRACTICAL EXAMPLE
# ============================================

print("\n=== Practical Example: Library System ===\n")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def borrow_book(self, title):
        """Borrow a book from the library."""
        book = self.find_book(title)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return f"Borrowed: {book.title}"
        elif book and book.is_borrowed:
            return f"'{title}' is already borrowed"
        else:
            return f"'{title}' not found in library"
    
    def return_book(self, title):
        """Return a book to the library."""
        book = self.find_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return f"Returned: {book.title}"
        elif book and not book.is_borrowed:
            return f"'{title}' is not currently borrowed"
        else:
            return f"'{title}' not found in library"
    
    def list_books(self):
        """List all books in the library."""
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            print(f"  - {book}")

# Using the library system
library = Library("City Library")
library.add_book(Book("Python Basics", "John Doe", "123456"))
library.add_book(Book("Advanced Python", "Jane Smith", "789012"))

library.list_books()
print(f"\n{library.borrow_book('Python Basics')}")
library.list_books()
print(f"\n{library.return_book('Python Basics')}")
library.list_books()

