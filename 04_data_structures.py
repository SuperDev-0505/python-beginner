"""
Data Structures - Lists, Tuples, Dictionaries, and Sets
Learn about Python's built-in data structures.

Updated: Added more comprehensive examples.
"""

# ============================================
# 1. LISTS
# ============================================

print("=== LISTS ===\n")

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# Accessing elements
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# Slicing
print(f"\nFirst two fruits: {fruits[0:2]}")
print(f"All except first: {fruits[1:]}")
print(f"All except last: {fruits[:-1]}")

# Modifying lists
fruits.append("grape")
print(f"\nAfter appending 'grape': {fruits}")

fruits.insert(1, "mango")
print(f"After inserting 'mango' at index 1: {fruits}")

fruits.remove("banana")
print(f"After removing 'banana': {fruits}")

fruits.pop()
print(f"After pop(): {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print(f"\nSquares (list comprehension): {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# ============================================
# 2. TUPLES
# ============================================

print("\n=== TUPLES ===\n")

# Creating tuples
coordinates = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma!

print("Coordinates:", coordinates)
print("Colors:", colors)
print("Single item:", single_item)

# Accessing elements
print(f"\nX coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"First color: {colors[0]}")

# Tuples are immutable (cannot be changed)
# coordinates[0] = 5  # This would cause an error!

# Unpacking tuples
x, y = coordinates
print(f"\nUnpacked: x={x}, y={y}")

# Multiple return values (tuples)
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

# ============================================
# 3. DICTIONARIES
# ============================================

print("\n=== DICTIONARIES ===\n")

# Creating dictionaries
student = {
    "name": "Bob",
    "age": 20,
    "grade": "A"
}

print("Student:", student)

# Accessing values
print(f"\nName: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"Grade: {student.get('grade', 'N/A')}")

# Adding/updating values
student["city"] = "New York"
student["age"] = 21
print(f"\nAfter updates: {student}")

# Removing items
del student["grade"]
print(f"After deleting 'grade': {student}")

# Dictionary methods
print(f"\nKeys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# Looping through dictionaries
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"\nSquares dictionary: {squares_dict}")

# Nested dictionaries
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21}
}
print(f"\nNested dictionary: {students}")

# ============================================
# 4. SETS
# ============================================

print("\n=== SETS ===\n")

# Creating sets
fruits_set = {"apple", "banana", "orange", "apple"}  # Duplicates removed
numbers_set = set([1, 2, 3, 4, 5])

print("Fruits set:", fruits_set)  # Note: no duplicates
print("Numbers set:", numbers_set)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set methods
set1.add(6)
print(f"\nAfter adding 6: {set1}")

set1.remove(1)
print(f"After removing 1: {set1}")

# Checking membership
print(f"\nIs 3 in set1? {3 in set1}")
print(f"Is 10 in set1? {10 in set1}")

# ============================================
# 5. PRACTICAL EXAMPLES
# ============================================

print("\n=== Practical Examples ===\n")

# Shopping list (list)
shopping_list = ["milk", "bread", "eggs"]
print("Shopping list:", shopping_list)

# Phone book (dictionary)
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}
print(f"\nPhone book: {phone_book}")
print(f"Alice's number: {phone_book['Alice']}")

# Unique tags (set)
tags = {"python", "programming", "tutorial", "python"}  # Duplicate removed
print(f"\nUnique tags: {tags}")

# Student records (list of dictionaries)
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

print("\nStudent records:")
for student in students:
    print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")

# Finding common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"\nCommon elements in {list1} and {list2}: {common}")

# Word frequency counter
text = "hello world hello python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nWord frequency in '{text}':")
for word, count in word_count.items():
    print(f"  {word}: {count}")

