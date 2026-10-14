PYTHON_LESSONS = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "duration": "10 minutes",
        "description": "Python is a beginner-friendly programming language. You can use it to build websites, applications, and automation tools.",
        "code": 'print("Hello, World!")',
        "exercise": "Write a Python program that prints your name."
    },
    {
        "id": 2,
        "title": "Variables and Data Types",
        "duration": "15 minutes",
        "description": "Variables store information. Common data types include integers, floats, strings, and booleans.",
        "code": 'name = "Ravi"\nage = 20\nheight = 5.8\nis_student = True\n\nprint(name)\nprint(age)',
        "exercise": "Create variables for your name, age, and college. Print them."
    },
    {
        "id": 3,
        "title": "Input and Output",
        "duration": "15 minutes",
        "description": "Use input() to receive information from the user and print() to display information.",
        "code": 'name = input("Enter your name: ")\nprint("Welcome", name)',
        "exercise": "Ask the user for their name and print a welcome message."
    },
    {
        "id": 4,
        "title": "Operators",
        "duration": "15 minutes",
        "description": "Operators perform arithmetic, comparison, and logical operations.",
        "code": 'a = 10\nb = 3\n\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)\nprint(a % b)',
        "exercise": "Take two numbers and display their sum, difference, and product."
    },
    {
        "id": 5,
        "title": "Conditional Statements",
        "duration": "20 minutes",
        "description": "Use if, elif, and else to make decisions in your program.",
        "code": 'age = int(input("Enter your age: "))\n\nif age >= 18:\n    print("You are an adult")\nelse:\n    print("You are a minor")',
        "exercise": "Write a program to check whether a number is positive, negative, or zero."
    },
    {
        "id": 6,
        "title": "Loops",
        "duration": "20 minutes",
        "description": "Loops repeat instructions. Python provides for loops and while loops.",
        "code": 'for number in range(1, 6):\n    print(number)',
        "exercise": "Print the multiplication table of a number entered by the user."
    },
    {
        "id": 7,
        "title": "Strings",
        "duration": "15 minutes",
        "description": "Strings represent text. You can join strings, change their case, and access individual characters.",
        "code": 'message = "Learn Python"\n\nprint(message.upper())\nprint(message.lower())\nprint(len(message))',
        "exercise": "Ask for a word and display it in uppercase and lowercase."
    },
    {
        "id": 8,
        "title": "Python Collections",
        "duration": "25 minutes",
        "description": "Lists, tuples, sets, and dictionaries help you organize multiple values.",
        "code": 'fruits = ["apple", "banana", "mango"]\nprint(fruits)\n\nstudent = {"name": "Ravi", "age": 20}\nprint(student["name"])',
        "exercise": "Create a list of five favorite subjects and print each subject."
    },
    {
        "id": 9,
        "title": "Functions",
        "duration": "20 minutes",
        "description": "Functions group reusable instructions. Define them using the def keyword.",
        "code": 'def greet(name):\n    print("Hello", name)\n\ngreet("Ravi")',
        "exercise": "Create a function that accepts two numbers and returns their sum."
    },
    {
        "id": 10,
        "title": "Exception Handling",
        "duration": "20 minutes",
        "description": "Exceptions help you handle errors without abruptly stopping your program.",
        "code": 'try:\n    number = int(input("Enter a number: "))\n    print(10 / number)\nexcept ValueError:\n    print("Please enter a valid integer")\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',
        "exercise": "Write a program that safely converts user input into an integer."
    },
    {
        "id": 11,
        "title": "File Handling",
        "duration": "20 minutes",
        "description": "Python can create, read, and write files. The with statement helps manage files safely.",
        "code": 'with open("notes.txt", "w") as file:\n    file.write("I am learning Python!")\n\nwith open("notes.txt", "r") as file:\n    print(file.read())',
        "exercise": "Write your favorite programming language into a text file and read it back."
    },
    {
        "id": 12,
        "title": "Object-Oriented Programming",
        "duration": "25 minutes",
        "description": "Classes define objects. Objects can contain data through attributes and behavior through methods.",
        "code": 'class Student:\n    def __init__(self, name):\n        self.name = name\n\n    def introduce(self):\n        print("My name is", self.name)\n\nstudent = Student("Ravi")\nstudent.introduce()',
        "exercise": "Create a Book class with a title attribute and a method that displays the title."
    },
    {
        "id": 13,
        "title": "Modules and Libraries",
        "duration": "15 minutes",
        "description": "Modules let you reuse code. Python includes useful built-in modules such as random and math.",
        "code": 'import random\n\nnumber = random.randint(1, 10)\nprint("Random number:", number)',
        "exercise": "Use the random module to generate a random number between 1 and 100."
    },
    {
        "id": 14,
        "title": "Mini Project: Calculator",
        "duration": "30 minutes",
        "description": "Combine variables, input, conditions, and arithmetic operators to create a simple calculator.",
        "code": 'a = float(input("Enter first number: "))\noperator = input("Enter operator (+, -, *, /): ")\nb = float(input("Enter second number: "))\n\nif operator == "+":\n    print(a + b)\nelif operator == "-":\n    print(a - b)\nelif operator == "*":\n    print(a * b)\nelif operator == "/" and b != 0:\n    print(a / b)\nelse:\n    print("Invalid operator or division by zero")',
        "exercise": "Improve the calculator by adding the modulo (%) operator."
    }
]