"""
Error Handling - Try/Except and Exception Handling
Learn how to handle errors gracefully in Python.
"""

# ============================================
# 1. BASIC TRY-EXCEPT
# ============================================

print("=== Basic Try-Except ===\n")

# Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling multiple exceptions
try:
    number = int("not a number")
except ValueError:
    print("Error: Invalid number format!")

# ============================================
# 2. TRY-EXCEPT-ELSE
# ============================================

print("\n=== Try-Except-Else ===\n")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    else:
        print("Division successful!")
        return result

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# ============================================
# 3. TRY-EXCEPT-FINALLY
# ============================================

print("\n=== Try-Except-Finally ===\n")

def read_file_safe(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print("File read successfully!")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    finally:
        print("This always executes, even if there's an error")
        # Cleanup code goes here

read_file_safe("nonexistent.txt")

# ============================================
# 4. MULTIPLE EXCEPTIONS
# ============================================

print("\n=== Multiple Exceptions ===\n")

def process_number(num_str):
    try:
        number = int(num_str)
        result = 100 / number
        return result
    except ValueError:
        print("Error: Invalid number format!")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

process_number("10")
process_number("abc")
process_number("0")

# ============================================
# 5. CATCHING SPECIFIC EXCEPTIONS
# ============================================

print("\n=== Catching Specific Exceptions ===\n")

def get_list_item(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None
    except TypeError:
        print("Error: Invalid index type!")
        return None

numbers = [1, 2, 3, 4, 5]
get_list_item(numbers, 2)
get_list_item(numbers, 10)
get_list_item(numbers, "invalid")

# ============================================
# 6. RAISING EXCEPTIONS
# ============================================

print("\n=== Raising Exceptions ===\n")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 150:
        raise ValueError("Age seems unrealistic!")
    else:
        print(f"Age {age} is valid!")

try:
    check_age(25)
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# ============================================
# 7. CUSTOM EXCEPTIONS
# ============================================

print("\n=== Custom Exceptions ===\n")

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds! Balance: ${self.balance}, Requested: ${amount}"
            )
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

account = BankAccount(100)
try:
    print(account.withdraw(50))
    print(account.withdraw(100))  # This will raise an error
except InsufficientFundsError as e:
    print(f"Error: {e}")

# ============================================
# 8. ASSERT STATEMENTS
# ============================================

print("\n=== Assert Statements ===\n")

def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    assert len(numbers) > 0, "List cannot be empty!"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers!"
    
    return sum(numbers) / len(numbers)

try:
    print(f"Average: {calculate_average([1, 2, 3, 4, 5])}")
    calculate_average([])  # This will raise AssertionError
except AssertionError as e:
    print(f"Assertion Error: {e}")

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================

print("\n=== Practical Examples ===\n")

# Safe division function
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Division by zero!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# Safe file reader
def safe_read_file(filename):
    """Safely read a file."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Safe dictionary access
def safe_get_value(dictionary, key, default=None):
    """Safely get a value from a dictionary."""
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found in dictionary")
        return default
    except TypeError:
        print("Error: First argument must be a dictionary!")
        return default

data = {"name": "Alice", "age": 25}
print(f"\nName: {safe_get_value(data, 'name')}")
print(f"City: {safe_get_value(data, 'city', 'Unknown')}")

# Input validation
def get_positive_number():
    """Get a positive number from user."""
    while True:
        try:
            # In real program: user_input = input("Enter a positive number: ")
            user_input = "5"  # Simulating input
            number = float(user_input)
            if number <= 0:
                raise ValueError("Number must be positive!")
            return number
        except ValueError as e:
            print(f"Invalid input: {e}")
            break  # In real program, would continue loop

print(f"\nPositive number: {get_positive_number()}")

# ============================================
# 10. EXCEPTION HIERARCHY
# ============================================

print("\n=== Exception Hierarchy ===\n")

# Common built-in exceptions
exceptions = [
    Exception,           # Base class for all exceptions
    ArithmeticError,     # Base for arithmetic errors
    ZeroDivisionError,   # Division by zero
    ValueError,          # Invalid value
    TypeError,           # Invalid type
    IndexError,          # Index out of range
    KeyError,            # Key not found
    FileNotFoundError,   # File not found
    AttributeError,      # Attribute not found
]

print("Common Python exceptions:")
for exc in exceptions:
    print(f"  - {exc.__name__}")

# Catching base exception
try:
    result = 10 / 0
except ArithmeticError as e:
    print(f"\nCaught ArithmeticError: {e}")

print("\n=== Error Handling Complete ===")

