---
triggers:
  - python
---

# Python Knowledge

This microagent provides comprehensive information about Python when triggered.

## What is Python?

Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected, supporting multiple programming paradigms including structured, object-oriented, and functional programming.

## Key Features

- **Simple and Readable Syntax**: Python's syntax is designed to be intuitive and close to natural language
- **Interpreted Language**: No compilation step needed, code runs directly
- **Dynamic Typing**: Variables don't need explicit type declarations
- **Cross-Platform**: Runs on Windows, macOS, Linux, and many other platforms
- **Extensive Standard Library**: "Batteries included" philosophy with rich built-in modules
- **Object-Oriented**: Supports classes, inheritance, and encapsulation
- **Functional Programming**: Supports lambda functions, map, filter, and reduce

## Common Use Cases

1. **Web Development**: Django, Flask, FastAPI frameworks
2. **Data Science & Analytics**: NumPy, Pandas, Matplotlib, Seaborn
3. **Machine Learning & AI**: TensorFlow, PyTorch, Scikit-learn
4. **Automation & Scripting**: System administration, task automation
5. **Desktop Applications**: Tkinter, PyQt, Kivy
6. **Game Development**: Pygame, Panda3D
7. **Scientific Computing**: SciPy, SymPy
8. **Web Scraping**: BeautifulSoup, Scrapy, Selenium

## Basic Syntax Examples

### Variables and Data Types
```python
# Numbers
age = 25
price = 19.99
is_active = True

# Strings
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# Lists and Dictionaries
fruits = ["apple", "banana", "orange"]
person = {"name": "John", "age": 30, "city": "New York"}
```

### Functions
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Lambda functions
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
```

### Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

person = Person("Alice", 25)
print(person.introduce())
```

### Control Flow
```python
# If statements
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Loops
for i in range(5):
    print(i)

while condition:
    # do something
    pass
```

## Popular Libraries and Frameworks

### Web Development
- **Django**: Full-featured web framework
- **Flask**: Lightweight and flexible web framework
- **FastAPI**: Modern, fast web framework for building APIs

### Data Science
- **NumPy**: Numerical computing with arrays
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting and visualization
- **Jupyter**: Interactive notebooks

### Machine Learning
- **Scikit-learn**: Machine learning library
- **TensorFlow**: Deep learning framework
- **PyTorch**: Deep learning framework
- **Keras**: High-level neural networks API

### Other Popular Libraries
- **Requests**: HTTP library for API calls
- **BeautifulSoup**: Web scraping
- **Pillow**: Image processing
- **SQLAlchemy**: Database toolkit

## Python Philosophy (The Zen of Python)

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts
- There should be one obvious way to do it

## Getting Started

1. **Installation**: Download from python.org or use package managers
2. **Interactive Shell**: Use `python` command to start REPL
3. **Package Management**: Use `pip` to install packages
4. **Virtual Environments**: Use `venv` or `conda` for project isolation

Python's versatility and ease of use make it an excellent choice for beginners and experienced developers alike, powering everything from simple scripts to complex enterprise applications.