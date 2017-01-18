"""
Modules and Packages - Code Organization
Learn how to organize code using modules and packages.
"""

# ============================================
# 1. IMPORTING BUILT-IN MODULES
# ============================================

print("=== Importing Built-in Modules ===\n")

# Import entire module
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"Cosine of 0: {math.cos(0)}")

# Import specific functions
from datetime import datetime, timedelta
now = datetime.now()
print(f"\nCurrent date and time: {now}")
print(f"Date formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Import with alias
import random as rnd
random_number = rnd.randint(1, 10)
print(f"\nRandom number (1-10): {random_number}")

# Import all (not recommended, but shown for learning)
from math import *
print(f"Using imported sqrt directly: {sqrt(25)}")

# ============================================
# 2. COMMON BUILT-IN MODULES
# ============================================

print("\n=== Common Built-in Modules ===\n")

# os module - operating system interface
import os
print(f"Current directory: {os.getcwd()}")
print(f"OS name: {os.name}")

# sys module - system-specific parameters
import sys
print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")

# json module - JSON encoder and decoder
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(f"\nJSON string: {json_string}")
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# collections module - specialized container datatypes
from collections import Counter, defaultdict, deque

# Counter - count hashable objects
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"\nWord count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# defaultdict - dict with default values
dd = defaultdict(int)
dd["a"] += 1
dd["b"] += 2
print(f"Defaultdict: {dict(dd)}")

# deque - double-ended queue
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(f"Deque: {list(dq)}")

# ============================================
# 3. CREATING YOUR OWN MODULE
# ============================================

print("\n=== Creating Your Own Module ===\n")

# This would typically be in a separate file (e.g., my_utils.py)
# For demonstration, we'll define it here

def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# In another file, you would import like:
# from my_utils import greet, add
# or
# import my_utils

print(greet("Python"))
print(f"5 + 3 = {add(5, 3)}")
print(f"5 * 3 = {multiply(5, 3)}")

# ============================================
# 4. MODULE ATTRIBUTES
# ============================================

print("\n=== Module Attributes ===\n")

# __name__ attribute
print(f"Current module name: {__name__}")

# When a module is run directly, __name__ is "__main__"
# When imported, __name__ is the module name

def main():
    """Main function that runs when script is executed directly."""
    print("This is the main function!")

if __name__ == "__main__":
    main()
    print("Script is being run directly")

# ============================================
# 5. WORKING WITH DATETIME
# ============================================

print("\n=== Working with DateTime ===\n")

from datetime import datetime, timedelta, date, time

# Current date and time
now = datetime.now()
print(f"Now: {now}")

# Specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")

# Time difference
future = now + timedelta(days=30)
print(f"30 days from now: {future}")

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")

# Parsing dates
date_string = "2024-01-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# ============================================
# 6. WORKING WITH RANDOM
# ============================================

print("\n=== Working with Random ===\n")

import random

# Random integer
print(f"Random integer (1-10): {random.randint(1, 10)}")

# Random float
print(f"Random float (0-1): {random.random()}")

# Random choice from list
colors = ["red", "green", "blue", "yellow"]
print(f"Random color: {random.choice(colors)}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Random sample
sample = random.sample(range(1, 100), 5)
print(f"Random sample (5 numbers): {sample}")

# ============================================
# 7. WORKING WITH REGULAR EXPRESSIONS
# ============================================

print("\n=== Working with Regular Expressions ===\n")

import re

# Search for pattern
text = "Contact us at support@example.com or info@test.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"Found emails: {emails}")

# Replace pattern
new_text = re.sub(r'\d+', 'X', "I have 5 apples and 3 oranges")
print(f"Replaced numbers: {new_text}")

# Match pattern
pattern = r'^\d{3}-\d{2}-\d{4}$'  # SSN format
ssn = "123-45-6789"
if re.match(pattern, ssn):
    print(f"'{ssn}' matches SSN pattern")
else:
    print(f"'{ssn}' does not match SSN pattern")

# ============================================
# 8. WORKING WITH ITERTOOLS
# ============================================

print("\n=== Working with Itertools ===\n")

from itertools import combinations, permutations, cycle, count

# Combinations
items = ['A', 'B', 'C']
combs = list(combinations(items, 2))
print(f"Combinations of 2: {combs}")

# Permutations
perms = list(permutations(items, 2))
print(f"Permutations of 2: {perms}")

# Cycle
colors_cycle = cycle(['red', 'green', 'blue'])
print("Cycling colors:")
for i, color in enumerate(colors_cycle):
    if i >= 5:
        break
    print(f"  {color}")

# Count
print("\nCounting from 5:")
counter = count(5)
for i in range(5):
    print(f"  {next(counter)}")

# ============================================
# 9. WORKING WITH PATHLIB
# ============================================

print("\n=== Working with Pathlib ===\n")

from pathlib import Path

# Create Path object
current_dir = Path(".")
print(f"Current directory: {current_dir.absolute()}")

# Join paths
file_path = Path("data") / "file.txt"
print(f"File path: {file_path}")

# Check if path exists
if Path("09_modules_packages.py").exists():
    print("This file exists!")

# Get file info
file = Path("09_modules_packages.py")
if file.exists():
    print(f"File size: {file.stat().st_size} bytes")
    print(f"Is file: {file.is_file()}")
    print(f"Is directory: {file.is_dir()}")

# ============================================
# 10. PRACTICAL EXAMPLE: UTILITY MODULE
# ============================================

print("\n=== Practical Example ===\n")

# This demonstrates how you might organize utility functions

class StringUtils:
    """Utility class for string operations."""
    
    @staticmethod
    def reverse(text):
        """Reverse a string."""
        return text[::-1]
    
    @staticmethod
    def is_palindrome(text):
        """Check if string is a palindrome."""
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def count_words(text):
        """Count words in a string."""
        return len(text.split())

class MathUtils:
    """Utility class for math operations."""
    
    @staticmethod
    def factorial(n):
        """Calculate factorial."""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)
    
    @staticmethod
    def is_prime(n):
        """Check if number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Using the utility classes
print(f"Reverse of 'Python': {StringUtils.reverse('Python')}")
print(f"Is 'racecar' a palindrome? {StringUtils.is_palindrome('racecar')}")
print(f"Factorial of 5: {MathUtils.factorial(5)}")
print(f"Is 17 prime? {MathUtils.is_prime(17)}")

print("\n=== Modules and Packages Complete ===")

