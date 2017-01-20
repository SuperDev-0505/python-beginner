"""
Python Basics - Variables, Data Types, and Basic Operations
This file covers fundamental Python concepts for beginners.

Updated: Added more examples and improved documentation.
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Numbers
age = 25
height = 5.9
temperature = -10

print("Age:", age)
print("Height:", height)
print("Temperature:", temperature)

# Strings
name = "Alice"
greeting = 'Hello, World!'
message = """This is a
multi-line string"""

print("\nName:", name)
print("Greeting:", greeting)
print("Message:", message)

# Boolean
is_student = True
has_license = False

print("\nIs student:", is_student)
print("Has license:", has_license)

# None (represents absence of value)
data = None
print("\nData:", data)

# ============================================
# 2. TYPE CONVERSION
# ============================================

# Converting between types
number_str = "123"
number_int = int(number_str)
number_float = float(number_str)

print("\nString:", number_str, type(number_str))
print("Integer:", number_int, type(number_int))
print("Float:", number_float, type(number_float))

# ============================================
# 3. BASIC OPERATIONS
# ============================================

# Arithmetic operations
a = 10
b = 3

print("\n=== Arithmetic Operations ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # Floor division
print(f"{a} % {b} = {a % b}")    # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("\nFull name:", full_name)
print("Name repeated 3 times:", first_name * 3)

# ============================================
# 4. STRING FORMATTING
# ============================================

# f-strings (Python 3.6+)
name = "Bob"
age = 30
print(f"\n{name} is {age} years old")

# .format() method
print("{} is {} years old".format(name, age))

# % formatting (older style)
print("%s is %d years old" % (name, age))

# ============================================
# 5. USER INPUT
# ============================================

# Getting input from user (commented out to avoid blocking)
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# ============================================
# 6. COMMENTS
# ============================================

# This is a single-line comment

"""
This is a multi-line comment
or docstring
"""

# ============================================
# 7. VARIABLE NAMING RULES
# ============================================

# Valid variable names
my_variable = 10
myVariable = 20
_private_var = 30
var123 = 40

# Invalid variable names (commented out - would cause errors)
# 123var = 50  # Cannot start with number
# my-var = 60  # Cannot use hyphens
# my var = 70  # Cannot use spaces

print("\n=== Variable Naming Examples ===")
print("my_variable:", my_variable)
print("myVariable:", myVariable)
print("_private_var:", _private_var)
print("var123:", var123)

