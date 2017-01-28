"""
Practical Projects - Real-World Examples
Complete projects that combine multiple Python concepts.

Updated: Added more project examples.
"""

import random
import json
from datetime import datetime

# ============================================
# PROJECT 1: TO-DO LIST MANAGER
# ============================================

print("=== PROJECT 1: To-Do List Manager ===\n")

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the list."""
        task_item = {
            "id": len(self.tasks) + 1,
            "task": task,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task_item)
        print(f"Added task: {task}")
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Completed task: {task['task']}")
                return
        print(f"Task {task_id} not found!")
    
    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("No tasks in the list!")
            return
        
        print("\nTo-Do List:")
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"  [{status}] {task['id']}. {task['task']}")
    
    def delete_task(self, task_id):
        """Delete a task from the list."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                print(f"Deleted task: {removed['task']}")
                # Reassign IDs
                for j, t in enumerate(self.tasks, 1):
                    t["id"] = j
                return
        print(f"Task {task_id} not found!")

# Using the TodoList
todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build a project")
todo.add_task("Write documentation")
todo.list_tasks()
todo.complete_task(1)
todo.list_tasks()

# ============================================
# PROJECT 2: NUMBER GUESSING GAME
# ============================================

print("\n=== PROJECT 2: Number Guessing Game ===\n")

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = 7
    
    def guess(self, number):
        """Make a guess and return feedback."""
        self.attempts += 1
        
        if number == self.secret_number:
            return "correct", self.attempts
        elif number < self.secret_number:
            return "too_low", None
        else:
            return "too_high", None
    
    def play(self):
        """Play the game."""
        print(f"Guess a number between {self.min_num} and {self.max_num}!")
        print(f"You have {self.max_attempts} attempts.\n")
        
        while self.attempts < self.max_attempts:
            # In real game: guess = int(input("Enter your guess: "))
            guess = random.randint(self.min_num, self.max_num)  # Simulating guesses
            result, attempts = self.guess(guess)
            
            if result == "correct":
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif result == "too_low":
                print(f"Too low! Attempts left: {self.max_attempts - self.attempts}")
            else:
                print(f"Too high! Attempts left: {self.max_attempts - self.attempts}")
        
        print(f"\nGame Over! The number was {self.secret_number}")
        return False

# Uncomment to play:
# game = NumberGuessingGame()
# game.play()

# ============================================
# PROJECT 3: CONTACT BOOK
# ============================================

print("\n=== PROJECT 3: Contact Book ===\n")

class ContactBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email=None):
        """Add a new contact."""
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Added contact: {name}")
    
    def find_contact(self, name):
        """Find a contact by name."""
        return self.contacts.get(name)
    
    def update_contact(self, name, phone=None, email=None):
        """Update an existing contact."""
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print(f"Updated contact: {name}")
        else:
            print(f"Contact '{name}' not found!")
    
    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"Contact '{name}' not found!")
    
    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts in the book!")
            return
        
        print("\nContacts:")
        for name, info in self.contacts.items():
            print(f"  {name}:")
            print(f"    Phone: {info['phone']}")
            if info['email']:
                print(f"    Email: {info['email']}")
    
    def save_to_file(self, filename):
        """Save contacts to a JSON file."""
        try:
            with open(filename, "w") as file:
                json.dump(self.contacts, file, indent=2)
            print(f"Contacts saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def load_from_file(self, filename):
        """Load contacts from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found!")
        except Exception as e:
            print(f"Error loading file: {e}")

# Using the ContactBook
contacts = ContactBook()
contacts.add_contact("Alice", "123-456-7890", "alice@email.com")
contacts.add_contact("Bob", "234-567-8901")
contacts.list_contacts()
contacts.save_to_file("contacts.json")

# ============================================
# PROJECT 4: SIMPLE CALCULATOR
# ============================================

print("\n=== PROJECT 4: Simple Calculator ===\n")

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def calculate(expression):
        """Evaluate a simple mathematical expression."""
        try:
            # Simple expression evaluator (for basic operations)
            # In production, use eval() carefully or a proper parser
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"

calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 * 5 = {calc.multiply(10, 5)}")
print(f"10 / 5 = {calc.divide(10, 5)}")
print(f"2 ** 3 = {calc.power(2, 3)}")

# ============================================
# PROJECT 5: PASSWORD GENERATOR
# ============================================

print("\n=== PROJECT 5: Password Generator ===\n")

class PasswordGenerator:
    def __init__(self):
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length=12, use_uppercase=True, use_digits=True, use_special=True):
        """Generate a random password."""
        characters = self.lowercase
        
        if use_uppercase:
            characters += self.uppercase
        if use_digits:
            characters += self.digits
        if use_special:
            characters += self.special
        
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def generate_multiple(self, count=5, length=12):
        """Generate multiple passwords."""
        passwords = []
        for _ in range(count):
            passwords.append(self.generate(length))
        return passwords

generator = PasswordGenerator()
print("Generated passwords:")
for i, pwd in enumerate(generator.generate_multiple(3, 16), 1):
    print(f"  {i}. {pwd}")

# ============================================
# PROJECT 6: TEXT ANALYZER
# ============================================

print("\n=== PROJECT 6: Text Analyzer ===\n")

class TextAnalyzer:
    @staticmethod
    def analyze(text):
        """Analyze text and return statistics."""
        words = text.split()
        characters = len(text)
        characters_no_spaces = len(text.replace(" ", ""))
        sentences = text.count(".") + text.count("!") + text.count("?")
        paragraphs = text.count("\n\n") + 1
        
        # Word frequency
        word_freq = {}
        for word in words:
            word = word.lower().strip(".,!?;:")
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Most common words
        most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "characters": characters,
            "characters_no_spaces": characters_no_spaces,
            "words": len(words),
            "sentences": sentences,
            "paragraphs": paragraphs,
            "most_common_words": most_common
        }
    
    @staticmethod
    def print_analysis(text):
        """Print formatted analysis."""
        stats = TextAnalyzer.analyze(text)
        print("Text Analysis:")
        print(f"  Characters: {stats['characters']}")
        print(f"  Characters (no spaces): {stats['characters_no_spaces']}")
        print(f"  Words: {stats['words']}")
        print(f"  Sentences: {stats['sentences']}")
        print(f"  Paragraphs: {stats['paragraphs']}")
        print("\n  Most common words:")
        for word, count in stats['most_common_words']:
            print(f"    '{word}': {count}")

sample_text = "Python is a great programming language. Python is easy to learn. Python is powerful!"
TextAnalyzer.print_analysis(sample_text)

print("\n=== Practical Projects Complete ===")

