"""
Functions - Reusable Blocks of Code
Learn how to create and use functions in Python.

Updated: Enhanced examples with better explanations.
"""

# ============================================
# 1. BASIC FUNCTIONS
# ============================================

print("=== Basic Functions ===\n")

# Simple function without parameters
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Charlie", 25)

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# Function with multiple return values
def get_name_and_age():
    return "David", 30

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# ============================================
# 2. DEFAULT PARAMETERS
# ============================================

print("\n=== Default Parameters ===\n")

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()  # Uses default
greet_with_default("Emma")  # Uses provided value

def power(base, exponent=2):
    return base ** exponent

print(f"2^3 = {power(2, 3)}")
print(f"2^2 = {power(2)}")  # Uses default exponent

# ============================================
# 3. KEYWORD ARGUMENTS
# ============================================

print("\n=== Keyword Arguments ===\n")

def create_profile(name, age, city, country):
    print(f"{name}, {age} years old, from {city}, {country}")

# Positional arguments
create_profile("Frank", 28, "New York", "USA")

# Keyword arguments
create_profile(name="Grace", age=32, city="London", country="UK")

# Mix of positional and keyword
create_profile("Henry", age=35, city="Tokyo", country="Japan")

# ============================================
# 4. VARIABLE NUMBER OF ARGUMENTS
# ============================================

print("\n=== Variable Arguments ===\n")

# *args - variable positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ivy", age=27, city="Paris")
print_info(title="Engineer", experience=5)

# ============================================
# 5. LAMBDA FUNCTIONS
# ============================================

print("\n=== Lambda Functions ===\n")

# Regular function
def square(x):
    return x ** 2

# Lambda function (anonymous function)
square_lambda = lambda x: x ** 2

print(f"Square of 5: {square(5)}")
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Lambda with multiple parameters
multiply = lambda a, b: a * b
print(f"3 * 4 = {multiply(3, 4)}")

# Lambda in map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Lambda in filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# ============================================
# 6. RECURSION
# ============================================

print("\n=== Recursion ===\n")

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 10 numbers):")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

# ============================================
# 7. SCOPE AND GLOBAL VARIABLES
# ============================================

print("\n=== Variable Scope ===\n")

# Global variable
global_var = "I'm global"

def show_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

show_scope()
print(f"Outside function - Global: {global_var}")

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter after increments: {counter}")

# ============================================
# 8. DOCSTRINGS
# ============================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

print(f"\nArea of rectangle (5 x 3): {calculate_area(5, 3)}")
print(f"Function documentation:\n{calculate_area.__doc__}")

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================

print("\n=== Practical Examples ===\n")

# Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_to_celsius(77)}°C")

# Check if number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"\nIs 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")

# Find maximum in a list
def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [3, 7, 2, 9, 1, 5]
print(f"\nMaximum in {numbers}: {find_max(numbers)}")

