"""
File Handling - Reading and Writing Files
Learn how to work with files in Python.
"""

import os

# ============================================
# 1. WRITING TO FILES
# ============================================

print("=== Writing to Files ===\n")

# Writing to a file (creates new file or overwrites existing)
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a Python file handling example.\n")
    file.write("Python is great for file operations!")

print("Created 'example.txt' with content")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nThis line was appended!")

print("Appended content to 'example.txt'")

# Writing multiple lines
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("example2.txt", "w") as file:
    file.writelines(lines)

print("Created 'example2.txt' with multiple lines")

# ============================================
# 2. READING FROM FILES
# ============================================

print("\n=== Reading from Files ===\n")

# Reading entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Full content of example.txt:")
    print(content)

# Reading line by line
print("\nReading line by line:")
with open("example.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print("Lines as list:", lines)

# Reading first N characters
with open("example.txt", "r") as file:
    first_20 = file.read(20)
    print(f"\nFirst 20 characters: {first_20}")

# ============================================
# 3. FILE MODES
# ============================================

print("\n=== File Modes ===\n")

# 'r' - Read mode (default for text files)
# 'w' - Write mode (overwrites existing file)
# 'a' - Append mode (adds to end of file)
# 'x' - Exclusive creation (fails if file exists)
# 'b' - Binary mode (e.g., 'rb', 'wb')
# 't' - Text mode (default)
# '+' - Read and write (e.g., 'r+', 'w+')

# Example with read and write mode
with open("example3.txt", "w+") as file:
    file.write("Initial content\n")
    file.seek(0)  # Move to beginning
    content = file.read()
    print("Content written and read:", content)

# ============================================
# 4. WORKING WITH CSV FILES
# ============================================

print("\n=== CSV Files ===\n")

# Writing CSV data
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"],
    ["Charlie", "35", "Tokyo"]
]

with open("data.csv", "w") as file:
    for row in csv_data:
        file.write(",".join(row) + "\n")

print("Created 'data.csv'")

# Reading CSV data
print("\nReading CSV file:")
with open("data.csv", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# ============================================
# 5. FILE OPERATIONS
# ============================================

print("\n=== File Operations ===\n")

# Check if file exists
if os.path.exists("example.txt"):
    print("'example.txt' exists")

# Get file size
file_size = os.path.getsize("example.txt")
print(f"Size of 'example.txt': {file_size} bytes")

# Rename file
if os.path.exists("example.txt"):
    os.rename("example.txt", "renamed_example.txt")
    print("Renamed 'example.txt' to 'renamed_example.txt'")

# ============================================
# 6. ERROR HANDLING WITH FILES
# ============================================

print("\n=== Error Handling ===\n")

# Safe file reading with try-except
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Creating it...")
    with open("nonexistent.txt", "w") as file:
        file.write("This file was created because it didn't exist!")

# ============================================
# 7. WORKING WITH JSON FILES
# ============================================

print("\n=== JSON Files ===\n")

import json

# Writing JSON data
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Created 'data.json'")

# Reading JSON data
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded JSON data:")
    print(json.dumps(loaded_data, indent=2))

# ============================================
# 8. PRACTICAL EXAMPLES
# ============================================

print("\n=== Practical Examples ===\n")

# Copy file content
def copy_file(source, destination):
    """Copy content from source file to destination file."""
    try:
        with open(source, "r") as src:
            content = src.read()
        with open(destination, "w") as dst:
            dst.write(content)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"Error: {source} not found")

copy_file("renamed_example.txt", "copy_example.txt")

# Count lines in a file
def count_lines(filename):
    """Count the number of lines in a file."""
    try:
        with open(filename, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

line_count = count_lines("renamed_example.txt")
print(f"Number of lines in 'renamed_example.txt': {line_count}")

# Search for text in file
def search_in_file(filename, search_term):
    """Search for a term in a file and return matching lines."""
    matches = []
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search_term.lower() in line.lower():
                    matches.append((line_num, line.strip()))
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    return matches

matches = search_in_file("renamed_example.txt", "Python")
print(f"\nLines containing 'Python':")
for line_num, line in matches:
    print(f"  Line {line_num}: {line}")

print("\n=== File Handling Complete ===")
print("Check the created files: example2.txt, example3.txt, data.csv, data.json, etc.")

