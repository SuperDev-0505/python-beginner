"""
Control Flow - If/Else Statements and Loops
Learn how to control the flow of your program.

Updated: Added more practical examples.
"""

# ============================================
# 1. IF/ELIF/ELSE STATEMENTS
# ============================================

print("=== IF/ELIF/ELSE Examples ===\n")

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult!")

# If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# If-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Multiple conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
elif age >= 18 and not has_license:
    print("You need a license to drive.")
else:
    print("You're too young to drive.")

# ============================================
# 2. FOR LOOPS
# ============================================

print("\n=== FOR LOOP Examples ===\n")

# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop with range and step
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# Loop through string
print("\nLooping through characters:")
word = "Python"
for char in word:
    print(char)

# Loop with index using enumerate
print("\nLooping with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Nested loops
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# ============================================
# 3. WHILE LOOPS
# ============================================

print("\n=== WHILE LOOP Examples ===\n")

# Simple while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
number = 10
while number > 0:
    print(f"Number: {number}")
    number -= 2

# While loop with break
print("\nLooping until we find 5:")
num = 0
while True:
    if num == 5:
        print("Found 5!")
        break
    print(f"Current number: {num}")
    num += 1

# While loop with continue
print("\nPrinting even numbers only:")
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(f"Even number: {num}")

# ============================================
# 4. BREAK AND CONTINUE
# ============================================

print("\n=== BREAK and CONTINUE Examples ===\n")

# Break example
print("Breaking at 5:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue example
print("\nSkipping odd numbers:")
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)

# ============================================
# 5. PRACTICAL EXAMPLES
# ============================================

print("\n=== Practical Examples ===\n")

# Finding maximum in a list
numbers = [3, 7, 2, 9, 1, 5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")

# Counting occurrences
text = "hello world"
count = 0
for char in text:
    if char == 'l':
        count += 1
print(f"Number of 'l' in '{text}': {count}")

# Sum of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Password checker (simple example)
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    # In real program: user_input = input("Enter password: ")
    user_input = "wrong"  # Simulating wrong input
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Wrong password! Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Access denied!")

