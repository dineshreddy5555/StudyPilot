COURSES = [
    {
    "id": "python",
    "name": "Python Programming",
    "icon": "🐍",
    "description": "Learn Python from the basics to practical programming.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to Python",
            "content": """
LEARNING OBJECTIVES
- Understand what Python is.
- Learn how to run a Python statement.
- Display information using print().
    
WHAT IS PYTHON?
Python is a popular programming language used in web development,
automation, data science, artificial intelligence, and education.

Python code is designed to be readable and relatively easy to learn.

YOUR FIRST PROGRAM
print("Hello, World!")

The print() function displays information on the screen.
Text is placed inside quotation marks.

You can display multiple messages:
print("Welcome to Study Pilot")
print("I am learning Python")

COMMENTS
Comments explain code to human readers. Python ignores them.

Example:
# This is a comment
print("Start learning")

PRACTICE
Write a program that displays your name and your favourite subject.
""",
            "code": 'print("Hello, World!")\nprint("Welcome to Study Pilot")\n# My first Python program',
            "quiz": [
                {"question": "Which function displays information in Python?", "options": ["show()", "print()", "display()", "writeText()"], "answer": 1},
                {"question": "Which character starts a single-line comment?", "options": ["//", "#", "<!--", "**"], "answer": 1},
                {"question": "Which is a valid Python statement?", "options": ["print('Hello')", "echo 'Hello'", "display: Hello", "say('Hello'"], "answer": 0},
                {"question": "What is Python commonly used for?", "options": ["Only drawing", "Only typing", "Web development and data analysis", "Only making documents"], "answer": 2},
                {"question": "What does print('Hi') do?", "options": ["Deletes text", "Displays Hi", "Creates a database", "Stops Python"], "answer": 1}
            ]
        },
        {
            "id": 2,
            "title": "Variables and Data Types",
            "content": """
LEARNING OBJECTIVES
- Store information in variables.
- Recognise common Python data types.
- Convert between basic data types.

WHAT IS A VARIABLE?
A variable is a name that refers to a value.

Examples:
name = "Alex"
age = 18
height = 1.7
is_student = True

COMMON DATA TYPES
str: text, such as "Python"
int: whole numbers, such as 10
float: decimal numbers, such as 3.14
bool: True or False

DISPLAYING VALUES
name = "Alex"
age = 18
print(name)
print(age)

CHECKING TYPES
Use type() to inspect a value's type.

print(type(10))
print(type("Hello"))

TYPE CONVERSION
Use int(), float(), and str() when an appropriate conversion is needed.

number = int("25")
print(number + 5)

Remember that not every string can be converted into a number.

PRACTICE
Create variables for your name, age, and favourite number.
Print each variable.
""",
            "code": 'name = "Alex"\nage = 18\nheight = 1.7\nis_student = True\nprint(name)\nprint(type(age))',
            "quiz": [
                {"question": "Which type stores whole numbers?", "options": ["str", "int", "bool", "list"], "answer": 1},
                {"question": "Which value is a string?", "options": ["25", "3.5", '"Python"', "True"], "answer": 2},
                {"question": "Which type represents True or False?", "options": ["float", "str", "bool", "tuple"], "answer": 2},
                {"question": "What does type(3.14) return?", "options": ["str", "float", "bool", "list"], "answer": 1},
                {"question": "What does int('25') produce?", "options": ["The integer 25", "The string '25'", "The number 2.5", "An error every time"], "answer": 0}
            ]
        },
        {
            "id": 3,
            "title": "Operators and Expressions",
            "content": """
LEARNING OBJECTIVES
- Use arithmetic operators.
- Compare values.
- Understand logical operators.

ARITHMETIC OPERATORS
+ adds values.
- subtracts values.
* multiplies values.
/ performs division.
// performs floor division.
% returns the remainder.
** raises a number to a power.

Example:
a = 10
b = 3
print(a + b)
print(a % b)

COMPARISON OPERATORS
== means equal to.
!= means not equal to.
> means greater than.
< means less than.
>= means greater than or equal to.
<= means less than or equal to.

A comparison produces True or False.

LOGICAL OPERATORS
and: both conditions must be true.
or: at least one condition must be true.
not: reverses a Boolean value.

Example:
age = 20
print(age >= 18 and age < 30)

PRACTICE
Calculate the total cost of three items and print the result.
""",
            "code": 'a = 10\nb = 3\nprint(a + b)\nprint(a // b)\nprint(a % b)\nprint(a > b)',
            "quiz": [
                {"question": "Which operator performs multiplication?", "options": ["+", "*", "%", "//"], "answer": 1},
                {"question": "What is 10 % 3?", "options": ["3", "1", "0", "10"], "answer": 1},
                {"question": "Which operator checks equality?", "options": ["=", "==", "!=", ">"], "answer": 1},
                {"question": "What does the and operator require?", "options": ["Both conditions true", "Both conditions false", "Only the first true", "No conditions"], "answer": 0},
                {"question": "What is 2 ** 3?", "options": ["5", "6", "8", "9"], "answer": 2}
            ]
        },
        {
            "id": 4,
            "title": "Conditions and Decision Making",
            "content": """
LEARNING OBJECTIVES
- Use if, elif, and else.
- Make decisions based on conditions.
- Understand indentation.

WHY CONDITIONS?
Programs often need to choose what to do based on information.

IF AND ELSE
score = 75

if score >= 50:
    print("Pass")
else:
    print("Try again")

The indented lines belong to their corresponding blocks.

ELIF
Use elif when checking another condition.

score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Keep practising")

ORDER MATTERS
Python checks conditions from top to bottom.
The first true branch is executed.

COMMON MISTAKE
Use == to compare values and = to assign values.

PRACTICE
Write a program that checks whether a number is positive,
negative, or zero.
""",
            "code": 'number = 7\nif number > 0:\n    print("Positive")\nelif number < 0:\n    print("Negative")\nelse:\n    print("Zero")',
            "quiz": [
                {"question": "Which keyword begins a conditional statement?", "options": ["repeat", "if", "when", "check"], "answer": 1},
                {"question": "What is elif used for?", "options": ["Checking another condition", "Ending the program", "Creating a list", "Importing a module"], "answer": 0},
                {"question": "Which keyword handles the final alternative branch?", "options": ["otherwise", "default", "else", "last"], "answer": 2},
                {"question": "What is important about Python code inside an if block?", "options": ["It must be indented", "It must be uppercase", "It must contain a loop", "It must be in quotation marks"], "answer": 0},
                {"question": "Which operator compares two values for equality?", "options": ["=", "==", "+=", "**"], "answer": 1}
            ]
        },
        {
            "id": 5,
            "title": "Loops",
            "content": """
LEARNING OBJECTIVES
- Repeat instructions using loops.
- Use for and while.
- Control a loop with break and continue.

FOR LOOPS
A for loop visits items in a sequence.

for number in range(3):
    print(number)

This displays 0, 1, and 2.
The ending value of range() is excluded.

RANGE WITH START AND STOP
for number in range(1, 5):
    print(number)

This displays 1, 2, 3, and 4.

WHILE LOOPS
A while loop repeats while its condition is true.

count = 1
while count <= 3:
    print(count)
    count += 1

Make sure the condition can eventually become false.

BREAK AND CONTINUE
break ends the loop.
continue skips to the next iteration.

PRACTICE
Display the numbers from 1 to 10 using a for loop.
""",
            "code": 'for number in range(1, 6):\n    print(number)\n\ncount = 1\nwhile count <= 3:\n    print("Count:", count)\n    count += 1',
            "quiz": [
                {"question": "Which loop is commonly used to iterate over a sequence?", "options": ["for", "define", "class", "import"], "answer": 0},
                {"question": "What does range(3) produce when iterated?", "options": ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3 only"], "answer": 1},
                {"question": "What does break do?", "options": ["Ends the loop", "Repeats forever", "Defines a function", "Creates a variable"], "answer": 0},
                {"question": "When does a while loop continue?", "options": ["While its condition is true", "Only once", "Only when the condition is false", "Never"], "answer": 0},
                {"question": "What does continue do?", "options": ["Stops Python", "Skips to the next iteration", "Deletes the loop", "Returns a value"], "answer": 1}
            ]
        },
        {
            "id": 6,
            "title": "Lists and Tuples",
            "content": """
LEARNING OBJECTIVES
- Store multiple values.
- Access elements using indexes.
- Understand lists and tuples.

LISTS
A list stores multiple items in order.
Lists are mutable, meaning their contents can change.

subjects = ["Math", "Science", "Python"]
print(subjects[0])
subjects.append("English")
print(subjects)

Python indexing starts at zero.
The first item is at index 0.

USEFUL LIST OPERATIONS
append(item): adds an item.
remove(item): removes a matching item.
len(items): returns the number of items.
items[1]: accesses the second item.

TUPLES
A tuple also stores ordered items, but cannot be reassigned
item by item after creation.

point = (10, 20)
print(point[0])

Use a list when you need to modify a collection.
Use a tuple for a collection intended to remain fixed.

PRACTICE
Create a list of five subjects and display each subject.
""",
            "code": 'subjects = ["Math", "Science", "Python"]\nsubjects.append("English")\nprint(subjects[0])\nprint(len(subjects))\npoint = (10, 20)\nprint(point[1])',
            "quiz": [
                {"question": "Which brackets are normally used to create a list?", "options": ["()", "[]", "{}", "<>"], "answer": 1},
                {"question": "What is the index of the first list item?", "options": ["1", "-1", "0", "2"], "answer": 2},
                {"question": "Which list method adds an item to the end?", "options": ["append()", "insertEndOnly()", "pushBackText()", "join()"], "answer": 0},
                {"question": "Which collection is immutable?", "options": ["List", "Tuple", "Set", "Dictionary"], "answer": 1},
                {"question": "What does len([2, 4, 6]) return?", "options": ["2", "3", "6", "12"], "answer": 1}
            ]
        },
        {
            "id": 7,
            "title": "Dictionaries and Sets",
            "content": """
LEARNING OBJECTIVES
- Store key-value pairs in dictionaries.
- Access and update dictionary values.
- Understand sets and unique values.

DICTIONARIES
A dictionary stores key-value pairs.

student = {
    "name": "Alex",
    "age": 18
}

print(student["name"])
student["age"] = 19
student["course"] = "Python"

Keys are used to look up values.
Accessing a missing key with square brackets raises KeyError.

The get() method can provide a default:
print(student.get("grade", "Not available"))

SETS
A set stores unique elements.

numbers = {1, 2, 2, 3}
print(numbers)

The repeated value 2 appears only once in the set.

PRACTICE
Create a dictionary describing a book with title and author.
Then create a set containing repeated numbers.
""",
            "code": 'student = {"name": "Alex", "age": 18}\nprint(student["name"])\nstudent["age"] = 19\nstudent["course"] = "Python"\nprint(student)\nnumbers = {1, 2, 2, 3}\nprint(numbers)',
            "quiz": [
                {"question": "What does a dictionary store?", "options": ["Only indexes", "Key-value pairs", "Only unique numbers", "Only functions"], "answer": 1},
                {"question": "How do you access the name in student['name']?", "options": ["By its key", "By a CSS selector", "By a loop only", "By its file name"], "answer": 0},
                {"question": "What is a key feature of a set?", "options": ["It preserves every duplicate", "It stores only text", "It contains unique elements", "It cannot store numbers"], "answer": 2},
                {"question": "What does dictionary get() help with?", "options": ["Providing a default for a missing key", "Sorting every list", "Creating a class", "Opening a file"], "answer": 0},
                {"question": "Which brackets create a dictionary literal?", "options": ["[]", "()", "{}", "<>"], "answer": 2}
            ]
        },
        {
            "id": 8,
            "title": "Functions",
            "content": """
LEARNING OBJECTIVES
- Define reusable functions.
- Use parameters and arguments.
- Return results from functions.

WHAT IS A FUNCTION?
A function groups instructions that can be called when needed.

def greet():
    print("Welcome to Python")

greet()

PARAMETERS
Parameters receive information supplied when a function is called.

def greet(name):
    print("Hello", name)

greet("Alex")

RETURN VALUES
return sends a result back to the caller.

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

A function that reaches its end without returning a value
normally returns None.

WHY USE FUNCTIONS?
Functions reduce repeated code and make programs easier to test,
understand, and maintain.

PRACTICE
Write a function that accepts two numbers and returns their product.
""",
            "code": 'def add(a, b):\n    return a + b\n\nresult = add(3, 4)\nprint(result)\n\ndef greet(name):\n    print("Hello", name)\n\ngreet("Alex")',
            "quiz": [
                {"question": "Which keyword defines a function?", "options": ["function", "def", "make", "fun"], "answer": 1},
                {"question": "What does return do?", "options": ["Sends a result back to the caller", "Always prints text", "Creates a loop", "Imports a package"], "answer": 0},
                {"question": "What is a parameter?", "options": ["A variable in a function definition", "A type of loop", "A database table", "A comment"], "answer": 0},
                {"question": "What does add(3, 4) return for the given add function?", "options": ["1", "7", "12", "34"], "answer": 1},
                {"question": "Why are functions useful?", "options": ["They encourage code reuse", "They remove all variables", "They prevent all errors", "They replace Python"], "answer": 0}
            ]
        },
        {
            "id": 9,
            "title": "Strings and String Methods",
            "content": """
LEARNING OBJECTIVES
- Work with text.
- Access characters and slices.
- Use common string methods.

STRINGS
A string is a sequence of characters.

message = "Study Pilot"
print(message[0])
print(len(message))

INDEXING AND SLICING
message[0] accesses the first character.
message[0:5] selects characters from index 0 up to,
but not including, index 5.

USEFUL METHODS
upper(): converts letters to uppercase.
lower(): converts letters to lowercase.
strip(): removes surrounding whitespace.
replace(old, new): replaces matching text.
split(): separates text into a list.

Example:
text = "  Learn Python  "
print(text.strip())
print(text.upper())

Strings are immutable: methods return new strings instead of
changing the original string in place.

PRACTICE
Ask a user for their name and display it in uppercase.
""",
            "code": 'message = "  Learn Python  "\nprint(message.strip())\nprint(message.upper())\nprint("Study Pilot".replace("Pilot", "Python"))',
            "quiz": [
                {"question": "Which method converts text to uppercase?", "options": ["upper()", "capital()", "big()", "uppercaseText()"], "answer": 0},
                {"question": "What does strip() remove?", "options": ["All letters", "Surrounding whitespace", "Every number", "All punctuation everywhere"], "answer": 1},
                {"question": "What does len('Python') return?", "options": ["5", "6", "7", "0"], "answer": 1},
                {"question": "Which slice selects characters from index 0 to 2, excluding 2?", "options": ["[0:2]", "[0:3]", "[2:0]", "[1:2]"], "answer": 0},
                {"question": "Are Python strings mutable?", "options": ["Yes, always", "No, they are immutable", "Only if numeric", "Only inside functions"], "answer": 1}
            ]
        },
        {
            "id": 10,
            "title": "File Handling and Exceptions",
            "content": """
LEARNING OBJECTIVES
- Open and read files.
- Write text to a file.
- Handle common errors.

OPENING FILES
Python can read and write files.

The with statement is recommended because it closes
the file automatically when the block finishes.

Example:
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("I am learning Python")

READING A FILE
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

COMMON MODES
r: read an existing file.
w: write, replacing existing content.
a: append to the end of a file.

Be careful with w mode because it replaces existing content.

EXCEPTION HANDLING
Errors such as missing files can be handled using try and except.

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

PRACTICE
Write a short message to a file and then read it back.
Try handling a file that does not exist.
""",
            "code": 'try:\n    with open("notes.txt", "w", encoding="utf-8") as file:\n        file.write("Learning Python")\n\n    with open("notes.txt", "r", encoding="utf-8") as file:\n        print(file.read())\nexcept OSError as error:\n    print("File operation failed:", error)',
            "quiz": [
                {"question": "Which mode opens a file for reading?", "options": ["w", "r", "a", "x only"], "answer": 1},
                {"question": "What does write mode w normally do to an existing file?", "options": ["Replaces its contents", "Only reads it", "Prints it", "Never opens it"], "answer": 0},
                {"question": "Why is with open(...) useful?", "options": ["It manages closing the file", "It always deletes files", "It prevents all errors", "It creates a website"], "answer": 0},
                {"question": "Which block handles an exception?", "options": ["except", "repeat", "switch", "select"], "answer": 0},
                {"question": "Which exception can occur when opening a missing file for reading?", "options": ["FileNotFoundError", "ColorError", "CSSException", "LoopError"], "answer": 0}
            ]
        }
    ]
},
    {
        "id": "java",
        "name": "Java Programming",
        "icon": "☕",
        "description": "Learn Java from the basics to object-oriented programming.",
        "level": "Beginner",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Java",
                "content": """
LESSON 1: INTRODUCTION TO JAVA
================================

1. WHAT IS JAVA?

Java is a high-level, general-purpose programming language.
It is used to develop desktop applications, web applications,
backend systems, enterprise software, and Android applications.

Java is popular because it supports object-oriented programming
and can run on different operating systems using a compatible
Java Virtual Machine.

2. FEATURES OF JAVA

Platform independent:
Java source code is compiled into bytecode. A compatible JVM
can execute that bytecode on different operating systems.

Object-oriented:
Java programs can be organized using classes and objects.

Strongly typed:
Variables have declared types such as int, double, and String.

Automatic memory management:
Java uses garbage collection to help reclaim memory used by
objects that are no longer needed.

3. JDK, JRE, AND JVM

JDK:
The Java Development Kit contains development tools, including
the Java compiler.

JRE:
Traditionally, the Java Runtime Environment describes the
components needed to run Java applications.

JVM:
The Java Virtual Machine executes Java bytecode.

Java source code (.java)
        |
        v
Java compiler (javac)
        |
        v
Bytecode (.class)
        |
        v
JVM executes bytecode

4. YOUR FIRST JAVA PROGRAM

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

Explanation:

public class Main:
Declares a class named Main.

public static void main(String[] args):
Defines the main method, where a typical standalone Java
application begins execution.

System.out.println():
Displays information and moves to a new line.

Braces {} group a block of code.
A semicolon ends a Java statement.

5. PRINTING OUTPUT

Example:

System.out.println("Welcome to Java");
System.out.println(100);
System.out.println(10 + 20);

Output:
Welcome to Java
100
30

Java calculates 10 + 20 before printing the result.

6. PRINT AND PRINTLN

System.out.print() displays output without automatically
moving to the next line.

System.out.println() displays output and moves to the next line.

Example:

System.out.print("Hello ");
System.out.print("Student");
System.out.println("!");

Output:
Hello Student!

7. COMMON MISTAKES

Forgetting semicolons:
System.out.println("Hello");

Incorrect capitalization:
System is different from system.
String is different from string.

Missing braces:
Opening and closing braces must match.

Filename:
A public class named Main normally belongs in Main.java.

PRACTICE EXERCISES

1. Write a program that displays your name.
2. Print three lines describing your favorite subject.
3. Display the result of 25 + 15.

LESSON SUMMARY

You learned what Java is, its features, the JDK, JRE, JVM,
the structure of a Java program, and how to print output.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Welcome to Java!");\n        System.out.println("I am learning programming.");\n        System.out.println(25 + 15);\n    }\n}',
                "quiz": [
                    {
                        "question": "What is Java?",
                        "options": ["A programming language", "An operating system", "A database only", "A web browser"],
                        "answer": 0
                    },
                    {
                        "question": "What does the JVM execute?",
                        "options": ["HTML", "Java bytecode", "CSS", "SQL tables"],
                        "answer": 1
                    },
                    {
                        "question": "Which statement prints text in Java?",
                        "options": ["echo()", "printText()", "System.out.println()", "displayText()"],
                        "answer": 2
                    },
                    {
                        "question": "Which symbol normally ends a Java statement?",
                        "options": [":", ";", ",", "#"],
                        "answer": 1
                    },
                    {
                        "question": "Which tool includes the Java compiler?",
                        "options": ["JDK", "JVM only", "HTML", "CSS"],
                        "answer": 0
                    }
                ]
            },
            {
                "id": 2,
                "title": "Variables and Data Types",
                "content": """
LESSON 2: VARIABLES AND DATA TYPES
===================================

1. WHAT IS A VARIABLE?

A variable is a named storage location used to hold a value.

Example:
int age = 18;

int is the data type.
age is the variable name.
18 is the value.

The equals sign assigns the value to the variable.

2. DECLARING VARIABLES

General syntax:
dataType variableName = value;

Examples:
int age = 18;
double price = 49.99;
char grade = 'A';
boolean isActive = true;
String studentName = "Alex";

Java requires a declared type for each variable.

3. PRIMITIVE DATA TYPES

byte:
Stores small whole numbers.

short:
Stores short-range whole numbers.

int:
Commonly used for whole numbers.

long:
Used for larger whole numbers.

float:
Stores decimal values with single precision.
A float literal commonly uses the suffix f.

double:
Stores decimal values with double precision.

char:
Stores one UTF-16 code unit, commonly used for a character.

boolean:
Stores true or false.

Example:
int count = 10;
long population = 8000000L;
float temperature = 25.5f;
double price = 99.99;
char grade = 'A';
boolean passed = true;

4. THE STRING TYPE

String stores text. String is a class, not a primitive type.

Example:
String name = "Sam";
System.out.println(name);

Text is enclosed in double quotation marks.
A char value uses single quotation marks.

5. CONSTANTS

Use final to declare a variable that cannot be reassigned.

Example:
final double PI = 3.14159;

After initialization, PI cannot be assigned a different value.

6. CHANGING VARIABLE VALUES

Example:
int score = 50;
score = 75;

The variable now contains 75.

A variable declared with final cannot be reassigned.

7. TYPE CONVERSION

Widening conversions can happen automatically when a value
fits the destination type.

Example:
int number = 10;
double result = number;

Explicit casting can convert a double to an int.

Example:
double price = 19.95;
int wholePrice = (int) price;

The result is 19 because the fractional part is discarded.

8. NAMING RULES

Variable names can contain letters, digits, underscores,
and dollar signs, but cannot begin with a digit.

Names are case-sensitive.

Use meaningful names:
studentAge
totalMarks
courseName

PRACTICE EXERCISES

1. Create variables for your name, age, and grade.
2. Create two integer variables and print their sum.
3. Declare a final variable for a number such as 100.

LESSON SUMMARY

You learned variable declarations, primitive types, String,
constants, assignment, and type conversion.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        String name = "Alex";\n        int age = 18;\n        double marks = 87.5;\n        char grade = \'A\';\n        boolean passed = true;\n\n        System.out.println(name);\n        System.out.println(age);\n        System.out.println(marks);\n        System.out.println(grade);\n        System.out.println(passed);\n    }\n}',
                "quiz": [
                    {
                        "question": "Which type stores whole numbers?",
                        "options": ["int", "String", "boolean", "char"],
                        "answer": 0
                    },
                    {
                        "question": "Which type stores text?",
                        "options": ["int", "String", "double", "boolean"],
                        "answer": 1
                    },
                    {
                        "question": "Which type stores true or false?",
                        "options": ["char", "int", "boolean", "String"],
                        "answer": 2
                    },
                    {
                        "question": "Which keyword prevents reassignment of a variable?",
                        "options": ["static", "final", "fixed", "constant"],
                        "answer": 1
                    },
                    {
                        "question": "What is the result of (int) 19.95?",
                        "options": ["19", "20", "19.95", "An error in every case"],
                        "answer": 0
                    }
                ]
            },
            {
                "id": 3,
                "title": "Operators and Expressions",
                "content": """
LESSON 3: OPERATORS AND EXPRESSIONS
====================================

1. WHAT IS AN OPERATOR?

An operator performs an operation on one or more values.

Example:
int total = 10 + 5;

The + operator adds the values 10 and 5.

2. ARITHMETIC OPERATORS

+ Addition
- Subtraction
* Multiplication
/ Division
% Remainder

Example:
int a = 10;
int b = 3;

System.out.println(a + b);  // 13
System.out.println(a - b);  // 7
System.out.println(a * b);  // 30
System.out.println(a / b);  // 3
System.out.println(a % b);  // 1

Integer division discards the fractional part.

For decimal division, use a decimal value:
System.out.println(10.0 / 3);

3. ASSIGNMENT OPERATORS

= assigns a value.
+= adds and assigns.
-= subtracts and assigns.
*= multiplies and assigns.
/= divides and assigns.

Example:
int score = 10;
score += 5;

The score is now 15.

4. COMPARISON OPERATORS

== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

Comparison expressions produce a boolean result.

Example:
int age = 18;
System.out.println(age >= 18);

Output:
true

5. LOGICAL OPERATORS

&& means logical AND.
|| means logical OR.
! means logical NOT.

Example:
int age = 20;
boolean hasTicket = true;

System.out.println(age >= 18 && hasTicket);

Both conditions must be true for && to produce true.

6. INCREMENT AND DECREMENT

++ increases a value by one.
-- decreases a value by one.

Example:
int count = 5;
count++;
System.out.println(count);

Output:
6

7. OPERATOR PRECEDENCE

Multiplication and division generally occur before addition
and subtraction.

Example:
int result = 2 + 3 * 4;

The result is 14.

Use parentheses to make the intended order clear:
int result = (2 + 3) * 4;

The result is 20.

PRACTICE EXERCISES

1. Calculate the sum, difference, and product of two numbers.
2. Check whether a number is greater than 50.
3. Use && to check two conditions.

LESSON SUMMARY

You learned arithmetic, assignment, comparison, logical,
increment, decrement, and precedence rules.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        int a = 10;\n        int b = 3;\n\n        System.out.println(a + b);\n        System.out.println(a % b);\n        System.out.println(a > b);\n\n        int score = 10;\n        score += 5;\n        System.out.println(score);\n    }\n}',
                "quiz": [
                    {
                        "question": "Which operator performs addition?",
                        "options": ["-", "+", "*", "/"],
                        "answer": 1
                    },
                    {
                        "question": "What is 10 % 3?",
                        "options": ["0", "1", "3", "10"],
                        "answer": 1
                    },
                    {
                        "question": "Which operator checks equality?",
                        "options": ["=", "==", "!=", ">"],
                        "answer": 1
                    },
                    {
                        "question": "Which operator means logical AND?",
                        "options": ["||", "!", "&&", "=="],
                        "answer": 2
                    },
                    {
                        "question": "What is 2 + 3 * 4?",
                        "options": ["20", "14", "24", "11"],
                        "answer": 1
                    }
                ]
            },
            {
                "id": 4,
                "title": "Conditions and Decision Making",
                "content": """
LESSON 4: CONDITIONS AND DECISION MAKING
=========================================

1. WHY DO WE NEED CONDITIONS?

Conditions let a program make decisions based on information.

Examples:
- Checking whether a student passed.
- Checking whether a user is old enough for an activity.
- Choosing a message based on a score.

2. THE IF STATEMENT

Syntax:
if (condition) {
    // Code runs when condition is true
}

Example:
int marks = 75;

if (marks >= 50) {
    System.out.println("Pass");
}

3. IF AND ELSE

Use else to provide an alternative when the condition is false.

Example:
int marks = 40;

if (marks >= 50) {
    System.out.println("Pass");
} else {
    System.out.println("Try again");
}

4. ELSE IF

Use else if to test several conditions.

Example:
int marks = 85;

if (marks >= 90) {
    System.out.println("Grade A");
} else if (marks >= 75) {
    System.out.println("Grade B");
} else if (marks >= 50) {
    System.out.println("Grade C");
} else {
    System.out.println("Needs improvement");
}

Conditions are checked in order. The first matching branch
is executed.

5. NESTED CONDITIONS

An if statement can appear inside another if statement.

Example:
int age = 20;
boolean hasID = true;

if (age >= 18) {
    if (hasID) {
        System.out.println("Condition satisfied");
    }
}

Avoid unnecessary nesting because it can make code harder
to understand.

6. THE SWITCH STATEMENT

A switch can select a branch based on a value.

Example:
int day = 2;

switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    default:
        System.out.println("Other day");
}

In this traditional switch statement, break prevents
execution from falling through to the next case.
default handles unmatched cases.

7. BOOLEAN CONDITIONS

Conditions commonly use comparison operators:
==, !=, >, <, >=, <=

Combine conditions with && and || when appropriate.

PRACTICE EXERCISES

1. Check whether a number is positive or negative.
2. Print a grade based on a student's marks.
3. Use switch to display a weekday based on a number.

LESSON SUMMARY

You learned if, else, else if, nested conditions, switch,
and how programs choose between alternatives.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        int marks = 75;\n\n        if (marks >= 90) {\n            System.out.println("Grade A");\n        } else if (marks >= 75) {\n            System.out.println("Grade B");\n        } else if (marks >= 50) {\n            System.out.println("Grade C");\n        } else {\n            System.out.println("Try again");\n        }\n    }\n}',
                "quiz": [
                    {
                        "question": "Which keyword checks a condition?",
                        "options": ["if", "repeat", "class", "import"],
                        "answer": 0
                    },
                    {
                        "question": "Which block runs when an if condition is false and no else-if matches?",
                        "options": ["main", "else", "for", "new"],
                        "answer": 1
                    },
                    {
                        "question": "What does >= mean?",
                        "options": ["Less than", "Equal only", "Greater than or equal to", "Not equal"],
                        "answer": 2
                    },
                    {
                        "question": "Which statement can select a branch based on a value?",
                        "options": ["switch", "import", "package", "extends"],
                        "answer": 0
                    },
                    {
                        "question": "If age is 20, is age >= 18 true?",
                        "options": ["Yes", "No", "Only in Python", "It is an error"],
                        "answer": 0
                    }
                ]
            },
            {
                "id": 5,
                "title": "Loops in Java",
                "content": """
LESSON 5: LOOPS IN JAVA
========================

1. WHAT IS A LOOP?

A loop repeats a block of code while a condition or
iteration rule allows it to continue.

Loops are useful for processing lists of values, repeating
calculations, and displaying sequences.

2. THE FOR LOOP

A traditional for loop contains:
- Initialization
- Condition
- Update

Example:
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}

The output is:
1
2
3
4
5

The variable i begins at 1. The loop continues while i <= 5.
After each iteration, i increases by one.

3. THE WHILE LOOP

A while loop checks its condition before each iteration.

Example:
int i = 1;

while (i <= 3) {
    System.out.println(i);
    i++;
}

If the condition is initially false, the loop body does
not run.

Remember to update variables when needed to avoid
accidentally creating an infinite loop.

4. THE DO-WHILE LOOP

A do-while loop runs its body at least once because the
condition is checked after the body.

Example:
int i = 1;

do {
    System.out.println(i);
    i++;
} while (i <= 3);

Notice the semicolon after the while condition.

5. NESTED LOOPS

A nested loop is a loop inside another loop.

Example:
for (int row = 1; row <= 2; row++) {
    for (int col = 1; col <= 3; col++) {
        System.out.print("* ");
    }
    System.out.println();
}

This displays two rows of three stars.

6. BREAK AND CONTINUE

break:
Stops the nearest enclosing loop.

continue:
Skips the rest of the current iteration and proceeds
to the next iteration.

Example:
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    System.out.println(i);
}

This skips printing 3.

7. COMMON LOOP MISTAKES

- Forgetting to update the loop variable.
- Using the wrong comparison operator.
- Accidentally creating an infinite loop.
- Using an incorrect starting value.

PRACTICE EXERCISES

1. Print numbers from 1 to 10 using a for loop.
2. Print even numbers from 2 to 20.
3. Display a rectangle of stars using nested loops.

LESSON SUMMARY

You learned for, while, do-while, nested loops, break,
continue, and common loop mistakes.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            System.out.println(i);\n        }\n    }\n}',
                "quiz": [
                    {
                        "question": "What is the purpose of a loop?",
                        "options": ["Repeat code", "Create a database", "Rename a class", "Delete Java"],
                        "answer": 0
                    },
                    {
                        "question": "How many times does for (int i = 0; i < 3; i++) run?",
                        "options": ["2", "3", "4", "0"],
                        "answer": 1
                    },
                    {
                        "question": "Which loop runs its body at least once?",
                        "options": ["for", "while", "do-while", "None of these"],
                        "answer": 2
                    },
                    {
                        "question": "Which statement exits a loop immediately?",
                        "options": ["continue", "break", "skip", "next"],
                        "answer": 1
                    },
                    {
                        "question": "What does continue do?",
                        "options": ["Ends the whole program", "Skips to the next iteration", "Creates a new loop", "Declares a variable"],
                        "answer": 1
                    }
                ]
            },
            {
                "id": 6,
                "title": "Arrays in Java",
                "content": """
LESSON 6: ARRAYS IN JAVA
=========================

1. WHAT IS AN ARRAY?

An array stores a fixed number of values of one declared
element type. Its length is set when the array is created.

Arrays are useful when several related values need to be
stored under one variable name.

2. DECLARING AN ARRAY

Example:
int[] numbers;

This declares a variable that can refer to an integer array.

You can create an array with a chosen length:
numbers = new int[5];

The array contains five integer elements. Their initial
values are zero.

3. INITIALIZING AN ARRAY

Example:
int[] numbers = {10, 20, 30, 40};

This creates an array with four elements.

4. ARRAY INDEXES

Array indexes start at zero.

numbers[0] is 10.
numbers[1] is 20.
numbers[2] is 30.
numbers[3] is 40.

The last valid index is array.length - 1.

Using an index outside the valid range causes an
ArrayIndexOutOfBoundsException at runtime.

5. CHANGING ARRAY VALUES

Example:
int[] numbers = {10, 20, 30};
numbers[1] = 99;

The array now contains:
10, 99, 30

6. LOOPING THROUGH AN ARRAY

Example:
int[] numbers = {10, 20, 30};

for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

The length property gives the number of elements.

7. ENHANCED FOR LOOP

You can use an enhanced for loop when you need to visit
each element.

Example:
int[] numbers = {10, 20, 30};

for (int number : numbers) {
    System.out.println(number);
}

This is convenient when you do not need the index.

8. FINDING A TOTAL

Example:
int[] marks = {70, 80, 90};
int total = 0;

for (int mark : marks) {
    total += mark;
}

System.out.println(total);

The total is 240.

PRACTICE EXERCISES

1. Create an array containing five integers.
2. Print every element using an enhanced for loop.
3. Calculate the sum of an array's values.

LESSON SUMMARY

You learned array declaration, initialization, indexing,
changing elements, looping, and calculating a total.
""",
                "code": 'public class Main {\n    public static void main(String[] args) {\n        int[] numbers = {10, 20, 30, 40};\n\n        for (int number : numbers) {\n            System.out.println(number);\n        }\n\n        System.out.println("Length: " + numbers.length);\n    }\n}',
                "quiz": [
                    {
                        "question": "What does an array store?",
                        "options": ["Only one value forever", "Multiple values of one declared element type", "Only methods", "Only files"],
                        "answer": 1
                    },
                    {
                        "question": "What is the first index of a Java array?",
                        "options": ["1", "-1", "0", "2"],
                        "answer": 2
                    },
                    {
                        "question": "What is numbers[1] in {10, 20, 30}?",
                        "options": ["10", "20", "30", "1"],
                        "answer": 1
                    },
                    {
                        "question": "Which property gives an array's length?",
                        "options": ["size()", "count()", "length", "total()"],
                        "answer": 2
                    },
                    {
                        "question": "What happens when an array index is outside its valid range?",
                        "options": ["It always returns zero", "A runtime exception can occur", "The array grows automatically", "Java changes the index"],
                        "answer": 1
                    }
                ]
            },
            {
                "id": 7,
                "title": "Methods in Java",
                "content": """
LESSON 7: METHODS IN JAVA
==========================

1. WHAT IS A METHOD?

A method is a named block of code that performs a task.
Methods help organize programs and avoid unnecessary
repetition.

2. DECLARING A METHOD

Example:
static void greet() {
    System.out.println("Welcome!");
}

static is a modifier.
void means the method does not return a value.
greet is the method name.
The parentheses hold any parameters.

3. CALLING A METHOD

A method must be called for its code to run.

Example:
static void greet() {
    System.out.println("Welcome!");
}

public static void main(String[] args) {
    greet();
}

Calling greet() executes the method body.

4. PARAMETERS AND ARGUMENTS

Parameters are variables declared in a method definition.
Arguments are the actual values supplied when calling it.

Example:
static void greet(String name) {
    System.out.println("Hello, " + name);
}

Call:
greet("Alex");

Output:
Hello, Alex

5. RETURN VALUES

A method can return a result instead of printing it.

Example:
static int add(int a, int b) {
    return a + b;
}

Calling add(2, 3) returns 5.

The declared return type must match the returned value.
A void method does not return a value to its caller.

6. METHOD OVERLOADING

Java allows multiple methods with the same name when
their parameter lists differ.

Example:
static int add(int a, int b) {
    return a + b;
}

static double add(double a, double b) {
    return a + b;
}

The compiler selects a suitable overload based on the
arguments and method signatures.

Changing only the return type is not enough to overload
a method.

7. LOCAL VARIABLES

Variables declared inside a method are local to that
method's scope. They generally cannot be accessed directly
from outside that scope.

8. WHY METHODS ARE USEFUL

Methods help you:
- Reuse code.
- Divide a large task into smaller tasks.
- Test individual pieces of logic.
- Make programs easier to maintain.

PRACTICE EXERCISES

1. Create a method that prints a welcome message.
2. Create a method that returns the sum of two integers.
3. Create overloaded methods that calculate a sum.

LESSON SUMMARY

You learned method declarations, method calls, parameters,
return values, overloading, and local variables.
""",
                "code": 'public class Main {\n    static int add(int a, int b) {\n        return a + b;\n    }\n\n    public static void main(String[] args) {\n        int result = add(10, 20);\n        System.out.println(result);\n    }\n}',
                "quiz": [
                    {
                        "question": "What is a method?",
                        "options": ["A reusable block of code", "A loop only", "A database table", "A comment"],
                        "answer": 0
                    },
                    {
                        "question": "Which keyword indicates that a method returns no value?",
                        "options": ["int", "return", "void", "new"],
                        "answer": 2
                    },
                    {
                        "question": "What are parameters used for?",
                        "options": ["Passing information into a method", "Closing the program", "Creating HTML", "Deleting a class"],
                        "answer": 0
                    },
                    {
                        "question": "What does return do?",
                        "options": ["Repeats a loop", "Provides a result from a method", "Declares an array", "Imports a package"],
                        "answer": 1
                    },
                    {
                        "question": "What does add(2, 3) return in the example?",
                        "options": ["2", "3", "5", "23"],
                        "answer": 2
                    }
                ]
            },
            {
                "id": 8,
                "title": "Classes and Objects",
                "content": """
LESSON 8: CLASSES AND OBJECTS
==============================

1. OBJECT-ORIENTED PROGRAMMING

Object-oriented programming organizes software around
objects that contain data and provide behavior.

Java supports classes, objects, inheritance, polymorphism,
encapsulation, and abstraction.

2. WHAT IS A CLASS?

A class is a blueprint that describes the data and behavior
its objects can have.

Example:
class Car {
    String color;

    void drive() {
        System.out.println("Car is moving");
    }
}

The class describes a color field and a drive method.

3. WHAT IS AN OBJECT?

An object is an instance of a class.

Example:
Car myCar = new Car();

Car is the type.
myCar is the reference variable.
new Car() creates a Car object.

You can access a public field or method through a reference:
myCar.color = "Red";
myCar.drive();

4. FIELDS AND METHODS

Fields store information associated with an object or class.
Methods describe actions or operations.

Instance fields belong to individual objects.

Example:
class Student {
    String name;
    int age;
}

Each Student object can hold its own name and age.

5. CONSTRUCTORS

A constructor initializes a new object.

Example:
class Student {
    String name;

    Student(String studentName) {
        name = studentName;
    }
}

Create an object:
Student student = new Student("Alex");

A constructor has the same name as its class and has no
declared return type.

6. ENCAPSULATION

Encapsulation protects an object's internal data by
controlling how it is accessed.

A common approach is to make fields private and provide
methods to read or update them.

Example:
class Account {
    private int balance;

    public int getBalance() {
        return balance;
    }

    public void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
}

The private field cannot be accessed directly from
unrelated external code.

7. THE THIS KEYWORD

this refers to the current object.

Example:
class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

Here, this.name refers to the field, while name refers
to the constructor parameter.

8. WHY CLASSES AND OBJECTS MATTER

Classes help organize related data and behavior.
Objects represent individual instances.
Constructors initialize objects.
Encapsulation helps protect data and maintain rules.

PRACTICE EXERCISES

1. Create a Book class with title and author fields.
2. Add a constructor that initializes a Student's name.
3. Create an Account class with a private balance field
   and a method that adds a positive deposit.

LESSON SUMMARY

You learned classes, objects, fields, methods, constructors,
encapsulation, and the this keyword.
""",
                "code": 'class Student {\n    private String name;\n\n    Student(String name) {\n        this.name = name;\n    }\n\n    public String getName() {\n        return name;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Student student = new Student("Alex");\n        System.out.println(student.getName());\n    }\n}',
                "quiz": [
                    {
                        "question": "What is a class?",
                        "options": ["A blueprint for objects", "A loop", "A conversion", "A comment"],
                        "answer": 0
                    },
                    {
                        "question": "What is an object?",
                        "options": ["An instance of a class", "A package name only", "A loop keyword", "A text file"],
                        "answer": 0
                    },
                    {
                        "question": "Which keyword commonly creates an object?",
                        "options": ["make", "new", "class", "object"],
                        "answer": 1
                    },
                    {
                        "question": "Which access modifier restricts direct access to a field from unrelated classes?",
                        "options": ["public", "private", "open", "global"],
                        "answer": 1
                    },
                    {
                        "question": "What is a constructor used for?",
                        "options": ["Initializing new objects", "Repeating a loop", "Importing a package", "Printing every variable"],
                        "answer": 0
                    }
                ]
            }
        ]
    },
    {
    "id": "javascript",
    "name": "JavaScript",
    "icon": "🟨",
    "description": "Master JavaScript fundamentals, DOM manipulation, events, and modern web development.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to JavaScript",
            "content": """
JavaScript is a programming language that makes web pages interactive.

It can:
- Respond to button clicks.
- Validate form input.
- Update page content.
- Perform calculations.
- Communicate with web servers.

JavaScript can run in web browsers and in environments such as Node.js.

The console is useful for testing JavaScript and viewing output.

Practice:
Write a program that displays your name in the console.
""",
            "code": """console.log("Welcome to Study Pilot!");

console.log("I am learning JavaScript.");

console.log(10 + 20);""",
            "quiz": [
                {
                    "question": "What is a common use of JavaScript?",
                    "options": [
                        "Adding interactivity to web pages",
                        "Creating HTML tags only",
                        "Replacing every database",
                        "Styling text exclusively"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which command displays output in the browser console?",
                    "options": [
                        "print()",
                        "console.log()",
                        "echo()",
                        "display.text()"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which file extension is commonly used for JavaScript files?",
                    "options": [".html", ".css", ".js", ".sql"],
                    "answer": 2
                },
                {
                    "question": "Where can JavaScript run?",
                    "options": [
                        "Only inside a database",
                        "In browsers and environments such as Node.js",
                        "Only inside CSS",
                        "Only in image files"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does console.log(10 + 20) display?",
                    "options": ["1020", "10 + 20", "30", "Error"],
                    "answer": 2
                }
            ]
        },
        {
            "id": 2,
            "title": "Variables and Data Types",
            "content": """
Variables store information that a program can use.

JavaScript provides three common ways to declare variables:
- let: Used for values that may be reassigned.
- const: Used for bindings that should not be reassigned.
- var: An older declaration style.

Common data types include:
- String: Text.
- Number: Numeric values.
- Boolean: true or false.
- Undefined: A variable without an assigned value.
- Null: An intentional absence of a value.
- Object: A collection of properties and values.

Use const by default when reassignment is unnecessary.
Use let when a value needs to change.

Practice:
Create variables for your name, age, and whether you enjoy coding.
""",
            "code": """const studentName = "Alex";
let age = 18;
const enjoysCoding = true;

console.log(studentName);
console.log(age);
console.log(enjoysCoding);

age = 19;
console.log(age);""",
            "quiz": [
                {
                    "question": "Which keyword declares a variable that can be reassigned?",
                    "options": ["let", "const", "fixed", "static"],
                    "answer": 0
                },
                {
                    "question": "Which value represents a Boolean?",
                    "options": ['"Hello"', "25", "true", "null"],
                    "answer": 2
                },
                {
                    "question": "What is the data type of 'Study'?",
                    "options": ["Number", "String", "Boolean", "Undefined"],
                    "answer": 1
                },
                {
                    "question": "Which keyword prevents reassignment of a variable binding?",
                    "options": ["let", "var", "const", "change"],
                    "answer": 2
                },
                {
                    "question": "What does an unassigned variable declared with let contain?",
                    "options": ["0", "false", "undefined", "An empty object"],
                    "answer": 2
                }
            ]
        },
        {
            "id": 3,
            "title": "Operators and Expressions",
            "content": """
Operators perform calculations and comparisons.

Arithmetic operators:
- + addition
- - subtraction
- * multiplication
- / division
- % remainder
- ** exponentiation

Comparison operators:
- === checks strict equality.
- !== checks strict inequality.
- > checks greater than.
- < checks less than.
- >= checks greater than or equal to.
- <= checks less than or equal to.

Logical operators:
- && means AND.
- || means OR.
- ! means NOT.

Prefer === over == when you want equality without automatic type conversion.

Practice:
Calculate the total price of two products.
""",
            "code": """const price1 = 100;
const price2 = 50;

const total = price1 + price2;
const difference = price1 - price2;
const remainder = 10 % 3;

console.log(total);
console.log(difference);
console.log(remainder);

console.log(5 === 5);
console.log(10 > 5);""",
            "quiz": [
                {
                    "question": "Which operator performs multiplication?",
                    "options": ["+", "*", "/", "%"],
                    "answer": 1
                },
                {
                    "question": "What is the result of 10 % 3?",
                    "options": ["3", "1", "0", "10"],
                    "answer": 1
                },
                {
                    "question": "Which operator checks strict equality?",
                    "options": ["=", "==", "===", "!="],
                    "answer": 2
                },
                {
                    "question": "Which operator means logical AND?",
                    "options": ["||", "!", "&&", "==="],
                    "answer": 2
                },
                {
                    "question": "What is the result of 2 ** 3?",
                    "options": ["5", "6", "8", "9"],
                    "answer": 2
                }
            ]
        },
        {
            "id": 4,
            "title": "Conditional Statements",
            "content": """
Conditional statements allow a program to make decisions.

The if statement runs code when a condition is true.

The else statement handles an alternative case.

The else if statement checks additional conditions.

The switch statement is useful when comparing one expression
against several possible cases.

Conditions often use comparison and logical operators.

Practice:
Write a program that checks whether a number is positive,
negative, or zero.
""",
            "code": """const marks = 75;

if (marks >= 90) {
    console.log("Grade A");
} else if (marks >= 70) {
    console.log("Grade B");
} else if (marks >= 50) {
    console.log("Grade C");
} else {
    console.log("Needs improvement");
}""",
            "quiz": [
                {
                    "question": "Which statement checks a condition?",
                    "options": ["if", "repeat", "define", "import"],
                    "answer": 0
                },
                {
                    "question": "Which block handles an alternative when previous conditions fail?",
                    "options": ["const", "else", "return", "break"],
                    "answer": 1
                },
                {
                    "question": "Which statement is useful for matching one expression against multiple cases?",
                    "options": ["switch", "console", "typeof", "class"],
                    "answer": 0
                },
                {
                    "question": "What is displayed when marks is 75 in the example?",
                    "options": ["Grade A", "Grade B", "Grade C", "Needs improvement"],
                    "answer": 1
                },
                {
                    "question": "Which operator means greater than or equal to?",
                    "options": ["<=", ">", ">=", "==="],
                    "answer": 2
                }
            ]
        },
        {
            "id": 5,
            "title": "Loops",
            "content": """
Loops repeat a block of code.

Common JavaScript loops include:

for:
Useful when you know how many times to repeat.

while:
Repeats while a condition remains true.

do...while:
Executes the body at least once before checking the condition.

for...of:
Iterates over values in an iterable such as an array.

Make sure loop conditions eventually become false when necessary.
Otherwise, the loop may continue indefinitely.

Practice:
Print numbers from 1 to 10.
""",
            "code": """for (let i = 1; i <= 5; i++) {
    console.log(i);
}

const subjects = ["Python", "Java", "HTML"];

for (const subject of subjects) {
    console.log(subject);
}

let count = 1;

while (count <= 3) {
    console.log("Count:", count);
    count++;
}""",
            "quiz": [
                {
                    "question": "Which loop is useful when the number of repetitions is known?",
                    "options": ["for", "if", "switch", "class"],
                    "answer": 0
                },
                {
                    "question": "Which loop checks its condition before each iteration?",
                    "options": ["while", "do...while only after execution", "switch", "try"],
                    "answer": 0
                },
                {
                    "question": "Which loop iterates over values in an array?",
                    "options": ["for...of", "if...else", "try...catch", "switch"],
                    "answer": 0
                },
                {
                    "question": "How many times does for (let i = 0; i < 3; i++) run?",
                    "options": ["2", "3", "4", "0"],
                    "answer": 1
                },
                {
                    "question": "What can happen if a loop's condition never becomes false?",
                    "options": [
                        "It may run indefinitely",
                        "It always runs once",
                        "It becomes a function",
                        "It automatically creates a variable"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "Functions",
            "content": """
Functions group reusable instructions.

A function can:
- Accept input through parameters.
- Perform operations.
- Return a result.

A function declaration uses the function keyword.

An arrow function provides a shorter syntax.

Parameters are names in a function definition.
Arguments are the actual values passed when calling it.

A return statement sends a result back to the caller.

Practice:
Create a function that multiplies two numbers.
""",
            "code": """function multiply(a, b) {
    return a * b;
}

console.log(multiply(4, 5));

const square = number => number * number;

console.log(square(6));""",
            "quiz": [
                {
                    "question": "Which keyword declares a traditional function?",
                    "options": ["function", "method", "define", "func"],
                    "answer": 0
                },
                {
                    "question": "Which keyword sends a value back from a function?",
                    "options": ["break", "return", "continue", "switch"],
                    "answer": 1
                },
                {
                    "question": "What does multiply(4, 5) return in the example?",
                    "options": ["9", "20", "45", "1"],
                    "answer": 1
                },
                {
                    "question": "Which symbol is used in an arrow function?",
                    "options": ["->", "=>", "::", "**"],
                    "answer": 1
                },
                {
                    "question": "What are parameters?",
                    "options": [
                        "Named inputs in a function definition",
                        "CSS selectors",
                        "HTML headings",
                        "Database tables"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 7,
            "title": "Arrays and Array Methods",
            "content": """
An array stores an ordered collection of values.

Array indexes start at zero.

Useful array methods include:
- push(): Adds an item to the end.
- pop(): Removes the last item.
- includes(): Checks whether an item exists.
- map(): Creates a new array by transforming each item.
- filter(): Creates a new array containing matching items.
- find(): Returns the first matching item, or undefined.

The length property gives the number of items.

map() and filter() do not modify the original array
when used normally with a callback.

Practice:
Create an array of numbers and find the even numbers.
""",
            "code": """const numbers = [1, 2, 3, 4, 5];

numbers.push(6);

const doubled = numbers.map(number => number * 2);
const evenNumbers = numbers.filter(number => number % 2 === 0);

console.log(numbers);
console.log(doubled);
console.log(evenNumbers);
console.log(numbers.length);""",
            "quiz": [
                {
                    "question": "What is the index of the first array element?",
                    "options": ["0", "1", "-1", "2"],
                    "answer": 0
                },
                {
                    "question": "Which method adds an element to the end of an array?",
                    "options": ["pop()", "push()", "filter()", "find()"],
                    "answer": 1
                },
                {
                    "question": "Which method transforms each item into a new array?",
                    "options": ["map()", "pop()", "includes()", "shift()"],
                    "answer": 0
                },
                {
                    "question": "Which method selects items that satisfy a condition?",
                    "options": ["filter()", "push()", "join()", "pop()"],
                    "answer": 0
                },
                {
                    "question": "What does numbers.length return for [10, 20, 30]?",
                    "options": ["2", "3", "30", "0"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 8,
            "title": "Objects and JSON",
            "content": """
Objects store related information as key-value pairs.

Properties describe an object.
Methods are functions stored as object properties.

You can access properties using dot notation
or bracket notation.

JSON stands for JavaScript Object Notation.
It is a text format commonly used to exchange data.

JSON.stringify() converts a JavaScript value into JSON text.
JSON.parse() converts valid JSON text into a JavaScript value.

JSON does not support every JavaScript value or syntax.
For example, JSON strings require double quotes around property names.

Practice:
Create a student object with a name and course.
""",
            "code": """const student = {
    name: "Alex",
    course: "JavaScript",
    completedLessons: 5
};

console.log(student.name);
console.log(student["course"]);

const jsonText = JSON.stringify(student);
console.log(jsonText);

const restoredStudent = JSON.parse(jsonText);
console.log(restoredStudent.completedLessons);""",
            "quiz": [
                {
                    "question": "How are object properties commonly represented?",
                    "options": [
                        "As key-value pairs",
                        "Only as array indexes",
                        "Only as HTML tags",
                        "As CSS rules"
                    ],
                    "answer": 0
                },
                {
                    "question": "How can you access the name property of student?",
                    "options": [
                        "student->name",
                        "student.name",
                        "student::name",
                        "student/name"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does JSON.stringify() do?",
                    "options": [
                        "Converts a value into JSON text",
                        "Creates a CSS stylesheet",
                        "Deletes an object",
                        "Starts a loop"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does JSON.parse() do?",
                    "options": [
                        "Converts valid JSON text into a JavaScript value",
                        "Converts HTML into CSS",
                        "Creates a function automatically",
                        "Removes all object properties"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which is a valid JSON object?",
                    "options": [
                        "{name: 'Alex'}",
                        '{"name": "Alex"}',
                        "{'name': 'Alex'}",
                        "{name = Alex}"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 9,
            "title": "DOM Manipulation and Events",
            "content": """
The Document Object Model (DOM) represents a web page
as objects that JavaScript can access and modify.

document.querySelector() selects the first matching element.
document.querySelectorAll() selects all matching elements.

textContent changes an element's text.
classList.add() adds a CSS class.
addEventListener() registers an event handler.

Common events include:
- click
- input
- change
- submit

DOM code normally runs after the relevant elements exist
in the document.

Practice:
Create a button that changes a heading when clicked.
""",
            "code": """<!-- HTML -->
<h1 id="heading">Welcome</h1>
<button id="changeButton" type="button">Change Text</button>

<script>
const heading = document.querySelector("#heading");
const button = document.querySelector("#changeButton");

button.addEventListener("click", function () {
    heading.textContent = "Keep Learning!";
});
</script>""",
            "quiz": [
                {
                    "question": "What does DOM stand for?",
                    "options": [
                        "Document Object Model",
                        "Data Output Method",
                        "Digital Order Machine",
                        "Document Orientation Mode"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which method selects the first matching element?",
                    "options": [
                        "document.querySelector()",
                        "document.selectAllFirst()",
                        "document.findHTML()",
                        "document.getCSS()"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which method registers an event handler?",
                    "options": [
                        "addEventListener()",
                        "addCSS()",
                        "writeStyle()",
                        "createLoop()"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which property changes an element's text content?",
                    "options": ["textContent", "font-family", "src", "href"],
                    "answer": 0
                },
                {
                    "question": "Which event commonly occurs when a user clicks a button?",
                    "options": ["click", "resize-only", "install", "database"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "Modern JavaScript and Error Handling",
            "content": """
Modern JavaScript includes useful features for writing
clearer and more maintainable programs.

Template literals use backticks and allow expressions
inside ${...}.

Destructuring extracts values from arrays or objects.

The spread syntax (...) can expand iterable values
or copy properties into a new object.

Promises represent the eventual result of an asynchronous operation.
async functions allow you to use await to wait for a promise.

try...catch handles exceptions so a program can respond
to errors rather than stopping unexpectedly.

When using fetch() for network requests, check response.ok
because HTTP error responses do not automatically reject the promise.

Practice:
Create a template literal and use try...catch to handle an error.
""",
            "code": """const name = "Alex";
const course = "JavaScript";

console.log(`Hello ${name}, welcome to ${course}!`);

const original = [1, 2, 3];
const copy = [...original, 4];

console.log(copy);

async function loadData() {
    try {
        const response = await fetch("/api/data");

        if (!response.ok) {
            throw new Error("Request failed");
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log("Could not load data:", error.message);
    }
}

// Call loadData() when the endpoint is available.""",
            "quiz": [
                {
                    "question": "Which characters are used for template literals?",
                    "options": [
                        "Backticks (`)",
                        "Square brackets only",
                        "Angle brackets",
                        "Forward slashes"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does await do inside an async function?",
                    "options": [
                        "Waits for a promise to settle before continuing that function",
                        "Creates a CSS class",
                        "Deletes a variable",
                        "Automatically repeats a loop"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which block handles an exception?",
                    "options": ["catch", "repeat", "style", "select"],
                    "answer": 0
                },
                {
                    "question": "What does the spread syntax look like?",
                    "options": ["...", "===", "&&", "=>"],
                    "answer": 0
                },
                {
                    "question": "Why should fetch() code check response.ok?",
                    "options": [
                        "HTTP error responses do not automatically reject the promise",
                        "It changes the website's colors",
                        "It creates an HTML heading",
                        "It converts JavaScript into CSS"
                    ],
                    "answer": 0
                }
            ]
        }
    ]
},
    {
    "id": "html-css",
    "name": "HTML and CSS",
    "icon": "🎨",
    "description": "Learn HTML, CSS, responsive design, and web development.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "HTML Basics",
            "content": """
HTML stands for HyperText Markup Language.
It defines the structure and content of web pages.

Important HTML tags:
- <html>: Root element.
- <head>: Contains page information.
- <title>: Sets the browser tab title.
- <body>: Contains visible page content.
- <h1> to <h6>: Headings.
- <p>: Paragraphs.
- <br>: Line break.

HTML elements usually have opening and closing tags.
""",
            "code": """<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Welcome to Study Pilot</h1>
    <p>My first web page.</p>
</body>
</html>""",
            "quiz": [
                {
                    "question": "What does HTML stand for?",
                    "options": [
                        "HyperText Markup Language",
                        "HighText Machine Language",
                        "Hyper Transfer Main Language",
                        "Home Tool Markup Language"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which tag creates a paragraph?",
                    "options": ["<h1>", "<p>", "<img>", "<table>"],
                    "answer": 1
                },
                {
                    "question": "Which tag contains visible page content?",
                    "options": ["<head>", "<title>", "<body>", "<meta>"],
                    "answer": 2
                },
                {
                    "question": "Which tag defines the largest standard heading?",
                    "options": ["<h6>", "<head>", "<h1>", "<p>"],
                    "answer": 2
                },
                {
                    "question": "Which declaration identifies an HTML5 document?",
                    "options": [
                        "<html5>",
                        "<!DOCTYPE html>",
                        "<document>",
                        "<head>"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 2,
            "title": "Links and Images",
            "content": """
Links connect one web page to another.

The <a> tag creates a hyperlink.
The href attribute specifies the destination.

Images use the <img> tag.
The src attribute specifies the image location.
The alt attribute describes the image for accessibility.

The <img> element does not require a closing tag.
""",
            "code": """<a href="https://example.com">Visit Example</a>

<img src="flower.jpg"
     alt="A beautiful flower"
     width="300">""",
            "quiz": [
                {
                    "question": "Which tag creates a hyperlink?",
                    "options": ["<link>", "<a>", "<href>", "<url>"],
                    "answer": 1
                },
                {
                    "question": "Which attribute specifies a link destination?",
                    "options": ["src", "alt", "href", "class"],
                    "answer": 2
                },
                {
                    "question": "Which tag displays an image?",
                    "options": ["<picture-text>", "<image>", "<img>", "<photo>"],
                    "answer": 2
                },
                {
                    "question": "What is the purpose of the alt attribute?",
                    "options": [
                        "To describe an image",
                        "To change the font",
                        "To create a database",
                        "To execute JavaScript"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which attribute specifies an image file?",
                    "options": ["href", "src", "target", "value"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 3,
            "title": "HTML Lists and Tables",
            "content": """
HTML lists organize related information.

An unordered list uses <ul> and <li>.
An ordered list uses <ol> and <li>.

Tables organize information into rows and columns.

Important table elements:
- <table>: Creates a table.
- <tr>: Creates a row.
- <th>: Creates a header cell.
- <td>: Creates a data cell.
- <caption>: Adds a table caption.

Use tables for tabular information rather than page layout.
""",
            "code": """<h2>My Subjects</h2>

<ul>
    <li>Python</li>
    <li>Java</li>
    <li>HTML</li>
</ul>

<table border="1">
    <tr>
        <th>Subject</th>
        <th>Hours</th>
    </tr>
    <tr>
        <td>Python</td>
        <td>2</td>
    </tr>
</table>""",
            "quiz": [
                {
                    "question": "Which tag creates an unordered list?",
                    "options": ["<ol>", "<ul>", "<li>", "<list>"],
                    "answer": 1
                },
                {
                    "question": "Which tag creates a list item?",
                    "options": ["<item>", "<li>", "<ul>", "<row>"],
                    "answer": 1
                },
                {
                    "question": "Which tag creates a table row?",
                    "options": ["<td>", "<th>", "<tr>", "<table-row>"],
                    "answer": 2
                },
                {
                    "question": "Which tag creates a table header cell?",
                    "options": ["<th>", "<head>", "<header>", "<td>"],
                    "answer": 0
                },
                {
                    "question": "Which tag creates an ordered list?",
                    "options": ["<ul>", "<ol>", "<li>", "<order>"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 4,
            "title": "HTML Forms",
            "content": """
Forms collect information from users.

Common form elements:
- <form>: Contains form controls.
- <label>: Describes an input.
- <input>: Accepts user input.
- <textarea>: Accepts longer text.
- <select>: Provides a dropdown.
- <option>: Defines a dropdown choice.
- <button>: Creates a button.

The name attribute identifies submitted form fields.
The method attribute specifies how form data is sent.

Use labels to make forms easier to understand and access.
""",
            "code": """<form action="/register" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <button type="submit">Register</button>
</form>""",
            "quiz": [
                {
                    "question": "Which tag creates a form?",
                    "options": ["<input>", "<form>", "<fieldset-only>", "<data>"],
                    "answer": 1
                },
                {
                    "question": "Which input type is suitable for an email address?",
                    "options": ["text", "email", "image", "button"],
                    "answer": 1
                },
                {
                    "question": "What does the required attribute do?",
                    "options": [
                        "Makes a field mandatory",
                        "Changes the page color",
                        "Creates a link",
                        "Deletes a field"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which element creates a dropdown?",
                    "options": ["<textarea>", "<select>", "<heading>", "<article>"],
                    "answer": 1
                },
                {
                    "question": "Which method commonly sends form data in the request body?",
                    "options": ["POST", "COLOR", "STYLE", "FONT"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 5,
            "title": "Introduction to CSS",
            "content": """
CSS stands for Cascading Style Sheets.

CSS controls how HTML elements look.

A CSS rule contains:
- A selector.
- One or more declarations.
- Property names and values.

Three ways to apply CSS:
1. Inline CSS: Uses the style attribute.
2. Internal CSS: Uses a style element.
3. External CSS: Uses a separate .css file.

External stylesheets are useful for maintaining consistent styling.
""",
            "code": """/* External CSS example */
h1 {
    color: blue;
    text-align: center;
}

p {
    font-size: 18px;
    color: #333333;
}""",
            "quiz": [
                {
                    "question": "What does CSS stand for?",
                    "options": [
                        "Cascading Style Sheets",
                        "Computer Style System",
                        "Creative Sheet Syntax",
                        "Colorful Styling Software"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which character begins a CSS ID selector?",
                    "options": [".", "#", "@", "&"],
                    "answer": 1
                },
                {
                    "question": "Which character begins a CSS class selector?",
                    "options": ["#", ".", "@", "$"],
                    "answer": 1
                },
                {
                    "question": "Which property changes text color?",
                    "options": ["font-size", "background", "color", "padding"],
                    "answer": 2
                },
                {
                    "question": "Which HTML element can link an external stylesheet?",
                    "options": ["<css>", "<style-link>", "<link>", "<script>"],
                    "answer": 2
                }
            ]
        },
        {
            "id": 6,
            "title": "CSS Colors, Fonts and Backgrounds",
            "content": """
CSS can control text, colors and backgrounds.

Useful properties:
- color: Changes text color.
- background-color: Sets an element's background.
- font-family: Chooses a typeface.
- font-size: Sets text size.
- font-weight: Controls text thickness.
- text-align: Aligns text.
- line-height: Controls line spacing.

Colors can be specified using names, hexadecimal values,
RGB values and other supported color formats.
""",
            "code": """body {
    background-color: #f0f4ff;
    font-family: Arial, sans-serif;
}

h1 {
    color: #174ea6;
    text-align: center;
    font-size: 32px;
}

p {
    line-height: 1.6;
    font-weight: normal;
}""",
            "quiz": [
                {
                    "question": "Which property changes the background color?",
                    "options": ["color", "background-color", "font-weight", "display"],
                    "answer": 1
                },
                {
                    "question": "Which property chooses the typeface?",
                    "options": ["font-family", "font-color", "text-style", "line-height"],
                    "answer": 0
                },
                {
                    "question": "Which property aligns text?",
                    "options": ["text-align", "padding", "margin", "border"],
                    "answer": 0
                },
                {
                    "question": "Which property controls text size?",
                    "options": ["font-size", "font-style", "background", "position"],
                    "answer": 0
                },
                {
                    "question": "Which CSS property controls line spacing?",
                    "options": ["letter-spacing", "line-height", "text-align", "display"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 7,
            "title": "CSS Box Model",
            "content": """
Every ordinary CSS box consists of content, padding,
border and margin.

Content holds the element's text or other content.
Padding adds space between the content and border.
Border surrounds the padding and content.
Margin creates space outside the border.

The box-sizing property changes how dimensions are calculated.

With border-box, the declared width includes padding and border.
""",
            "code": """.card {
    width: 300px;
    padding: 20px;
    border: 2px solid #333;
    margin: 15px;
    box-sizing: border-box;
}""",
            "quiz": [
                {
                    "question": "Which box-model area surrounds the content?",
                    "options": ["Margin", "Padding", "Border only", "Viewport"],
                    "answer": 1
                },
                {
                    "question": "Which property adds space outside the border?",
                    "options": ["padding", "margin", "color", "font-size"],
                    "answer": 1
                },
                {
                    "question": "What does the border property control?",
                    "options": [
                        "The element's outline around its box",
                        "The text content",
                        "The browser title",
                        "The database connection"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does box-sizing: border-box do?",
                    "options": [
                        "Includes padding and border in the specified width",
                        "Removes every border",
                        "Adds a background image",
                        "Changes the font"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which property sets the width of an element?",
                    "options": ["height", "width", "margin", "font-weight"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 8,
            "title": "CSS Flexbox",
            "content": """
Flexbox is a CSS layout system for arranging items
in a row or column.

Important properties:
- display: flex enables a flex container.
- flex-direction chooses row or column.
- justify-content distributes items along the main axis.
- align-items aligns items along the cross axis.
- gap adds space between items.
- flex-wrap allows items to wrap when needed.

Flexbox is useful for navigation bars, cards and toolbars.
""",
            "code": """.container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}

.card {
    padding: 20px;
    border: 1px solid #ccc;
}""",
            "quiz": [
                {
                    "question": "Which declaration enables Flexbox?",
                    "options": [
                        "display: flex",
                        "position: flex",
                        "layout: flex",
                        "style: flex"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which property changes the main layout direction?",
                    "options": ["flex-direction", "font-family", "border-style", "text-decoration"],
                    "answer": 0
                },
                {
                    "question": "Which property distributes items along the main axis?",
                    "options": ["align-items", "justify-content", "font-size", "overflow"],
                    "answer": 1
                },
                {
                    "question": "Which property adds spacing between flex items?",
                    "options": ["gap", "color", "opacity", "z-index"],
                    "answer": 0
                },
                {
                    "question": "Which property allows flex items to move onto another line?",
                    "options": ["flex-wrap", "flex-grow", "font-style", "text-transform"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 9,
            "title": "CSS Grid and Responsive Design",
            "content": """
CSS Grid is a layout system for arranging content
in rows and columns.

Use display: grid to create a grid container.
grid-template-columns defines the column structure.
gap controls spacing between grid items.

Responsive design helps pages work across phones,
tablets and desktop screens.

Media queries apply CSS under specified conditions.
Relative units such as percentages and rem can help
create flexible layouts.
""",
            "code": """.grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
}

@media (max-width: 700px) {
    .grid {
        grid-template-columns: 1fr;
    }
}""",
            "quiz": [
                {
                    "question": "Which declaration enables CSS Grid?",
                    "options": [
                        "display: grid",
                        "position: grid",
                        "layout: table-only",
                        "grid: true"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which property defines grid columns?",
                    "options": [
                        "grid-template-columns",
                        "flex-direction",
                        "font-family",
                        "text-align"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is responsive design?",
                    "options": [
                        "A layout that adapts to different screen sizes",
                        "A database backup method",
                        "A programming language",
                        "A way to remove HTML"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which CSS feature applies styles under conditions such as screen width?",
                    "options": ["Media queries", "HTML comments", "SQL queries", "Form labels"],
                    "answer": 0
                },
                {
                    "question": "What does 1fr represent in CSS Grid?",
                    "options": [
                        "One fraction of the available grid space",
                        "One fixed pixel",
                        "One font family",
                        "One HTML form"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "Semantic HTML and Web Accessibility",
            "content": """
Semantic HTML uses elements that describe their purpose.

Examples:
- <header>: Introductory content.
- <nav>: Navigation links.
- <main>: Main page content.
- <section>: A thematic section.
- <article>: Independent content.
- <footer>: Footer information.

Accessibility helps people with different abilities
use websites.

Useful practices include:
- Providing meaningful image alt text.
- Connecting labels to form controls.
- Using headings in a logical order.
- Making links descriptive.
- Maintaining readable color contrast.

Semantic elements improve structure, but accessibility
also depends on how the page is designed and implemented.
""",
            "code": """<header>
    <h1>Study Pilot</h1>
</header>

<nav aria-label="Main navigation">
    <a href="/">Home</a>
    <a href="/courses">Courses</a>
</nav>

<main>
    <section>
        <h2>Learn HTML and CSS</h2>
        <p>Build accessible web pages.</p>
        <img src="study.jpg" alt="Student studying at a desk">
    </section>
</main>

<footer>
    <p>Keep learning every day.</p>
</footer>""",
            "quiz": [
                {
                    "question": "Which element represents the main page content?",
                    "options": ["<main>", "<footer>", "<nav>", "<title>"],
                    "answer": 0
                },
                {
                    "question": "Which element contains navigation links?",
                    "options": ["<nav>", "<aside-only>", "<meta>", "<style>"],
                    "answer": 0
                },
                {
                    "question": "Why is meaningful image alt text useful?",
                    "options": [
                        "It describes images to users who cannot see them",
                        "It automatically resizes images",
                        "It creates a database",
                        "It changes the HTML version"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which element is appropriate for footer information?",
                    "options": ["<footer>", "<input>", "<tr>", "<script>"],
                    "answer": 0
                },
                {
                    "question": "Which practice improves form accessibility?",
                    "options": [
                        "Use labels connected to form controls",
                        "Remove all labels",
                        "Use only color to communicate meaning",
                        "Make every input unnamed"
                    ],
                    "answer": 0
                }
            ]
        }
    ]
},
    {
    "id": "dbms-sql",
    "name": "DBMS and SQL",
    "icon": "🗄️",
    "description": "Learn databases, relational models, and SQL queries.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to DBMS",
            "content": """
A Database Management System (DBMS) is software used to create,
store, organize, retrieve, and manage data.

Examples include MySQL, PostgreSQL, SQLite, and Oracle Database.

Benefits of a DBMS:
- Reduces unnecessary data duplication.
- Helps maintain data accuracy.
- Controls access to information.
- Supports backup and recovery.
- Allows users to search and update data efficiently.

A database stores organized information, while a DBMS manages that information.

Exercise:
Write down three examples of database management systems.
""",
            "code": """-- Example SQL query
SELECT 'Welcome to DBMS' AS message;""",
            "quiz": [
                {
                    "question": "What does DBMS stand for?",
                    "options": [
                        "Database Management System",
                        "Data Backup Main Software",
                        "Digital Base Management Service",
                        "Database Memory Storage"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which is an example of a DBMS?",
                    "options": ["HTML", "MySQL", "CSS", "JavaScript"],
                    "answer": 1
                },
                {
                    "question": "What is a database used for?",
                    "options": [
                        "Storing organized information",
                        "Designing web pages only",
                        "Drawing pictures only",
                        "Playing music only"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which is a benefit of a DBMS?",
                    "options": [
                        "It prevents all computer errors",
                        "It eliminates every security risk",
                        "It helps manage and retrieve data",
                        "It replaces the operating system"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which system is commonly used for relational databases?",
                    "options": ["MySQL", "Paint", "Notepad", "PowerPoint"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 2,
            "title": "Tables, Rows, and Columns",
            "content": """
Relational databases organize information into tables.

A table contains:
- Rows: individual records.
- Columns: attributes or fields.
- Primary keys: values that uniquely identify records.

Example Student table:

| student_id | name | age |
| 1 | Anu | 18 |
| 2 | Ravi | 19 |

Here, student_id can be the primary key because each student has
a unique ID.

Exercise:
Create a Student table on paper with columns for ID, name, and age.
Add three sample records.
""",
            "code": """CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);""",
            "quiz": [
                {
                    "question": "What does a row represent?",
                    "options": [
                        "A database program",
                        "A single record",
                        "A column heading",
                        "A SQL command"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does a column represent?",
                    "options": [
                        "An attribute or field",
                        "A complete database server",
                        "A database backup",
                        "A user account"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is a primary key used for?",
                    "options": [
                        "Formatting a table",
                        "Sorting text only",
                        "Uniquely identifying a record",
                        "Deleting the database"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which SQL command creates a table?",
                    "options": ["SELECT", "CREATE TABLE", "UPDATE", "DROP"],
                    "answer": 1
                },
                {
                    "question": "Can a primary key contain duplicate values?",
                    "options": [
                        "Yes, always",
                        "Only in small tables",
                        "Only for text columns",
                        "No"
                    ],
                    "answer": 3
                }
            ]
        },
        {
            "id": 3,
            "title": "Introduction to SQL",
            "content": """
SQL stands for Structured Query Language. It is used to communicate
with relational database systems.

Common SQL commands:
- SELECT: retrieves data.
- INSERT: adds records.
- UPDATE: changes existing records.
- DELETE: removes records.
- CREATE: creates database objects.

SQL commands are often grouped into categories:
- DDL: defines database structures.
- DML: manipulates data.
- DQL: retrieves data.
- DCL: controls permissions.
- TCL: manages transactions.

Exercise:
Write down the purpose of SELECT, INSERT, UPDATE, and DELETE.
""",
            "code": """-- Retrieve all student records
SELECT * FROM Students;

-- Retrieve only student names
SELECT name FROM Students;""",
            "quiz": [
                {
                    "question": "What does SQL stand for?",
                    "options": [
                        "Structured Query Language",
                        "Simple Question List",
                        "System Quality Language",
                        "Standard Quick Link"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which command retrieves records?",
                    "options": ["DELETE", "SELECT", "DROP", "INSERT"],
                    "answer": 1
                },
                {
                    "question": "Which command adds a new record?",
                    "options": ["UPDATE", "SELECT", "INSERT", "ALTER"],
                    "answer": 2
                },
                {
                    "question": "What does SELECT * mean?",
                    "options": [
                        "Select no columns",
                        "Delete all records",
                        "Create a new table",
                        "Select all columns"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which command changes existing records?",
                    "options": ["UPDATE", "CREATE", "SELECT", "GRANT"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 4,
            "title": "Filtering and Sorting Data",
            "content": """
SQL allows you to filter and sort query results.

WHERE filters records according to a condition.
ORDER BY sorts the results.
ASC sorts in ascending order.
DESC sorts in descending order.
LIMIT restricts the number of returned rows in databases that support it.

Comparison operators include:
= equal to
<> not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to

Exercise:
Write a query to find students older than 18 and sort them by name.
""",
            "code": """-- Find students older than 18
SELECT *
FROM Students
WHERE age > 18;

-- Sort students by name
SELECT *
FROM Students
ORDER BY name ASC;

-- Return at most five records
SELECT *
FROM Students
LIMIT 5;""",
            "quiz": [
                {
                    "question": "Which clause filters records?",
                    "options": ["ORDER BY", "WHERE", "CREATE", "INSERT"],
                    "answer": 1
                },
                {
                    "question": "Which keyword sorts query results?",
                    "options": ["VALUES", "INTO", "ORDER BY", "TABLE"],
                    "answer": 2
                },
                {
                    "question": "What does DESC mean in ORDER BY?",
                    "options": [
                        "Descending order",
                        "Delete selected columns",
                        "Display every column",
                        "Create a database"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which condition finds ages greater than 18?",
                    "options": [
                        "age < 18",
                        "age = 18",
                        "age <> 18",
                        "age > 18"
                    ],
                    "answer": 3
                },
                {
                    "question": "What does LIMIT 5 do in supported databases?",
                    "options": [
                        "Deletes five records",
                        "Restricts results to at most five rows",
                        "Creates five tables",
                        "Changes five column names"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 5,
            "title": "Adding, Updating, and Deleting Records",
            "content": """
INSERT adds records to a table.
UPDATE changes existing records.
DELETE removes records.

Important:
Always use a suitable WHERE condition when updating or deleting
specific records. Without WHERE, an UPDATE or DELETE may affect
every row in the table.

You can use INSERT with named columns to make your queries clearer.

Exercise:
Write SQL statements to add a student, change that student's age,
and delete that student's record.
""",
            "code": """-- Add a student
INSERT INTO Students (student_id, name, age)
VALUES (3, 'Meera', 20);

-- Change the student's age
UPDATE Students
SET age = 21
WHERE student_id = 3;

-- Delete the student's record
DELETE FROM Students
WHERE student_id = 3;""",
            "quiz": [
                {
                    "question": "Which command inserts a new record?",
                    "options": ["INSERT", "SELECT", "ORDER BY", "WHERE"],
                    "answer": 0
                },
                {
                    "question": "Which command modifies existing records?",
                    "options": ["CREATE", "UPDATE", "SELECT", "DROP"],
                    "answer": 1
                },
                {
                    "question": "Which command removes records?",
                    "options": ["INSERT", "ALTER", "DELETE", "SELECT"],
                    "answer": 2
                },
                {
                    "question": "Why is WHERE important in an UPDATE query?",
                    "options": [
                        "It creates a new database",
                        "It sorts every record",
                        "It changes a table name",
                        "It targets the intended records"
                    ],
                    "answer": 3
                },
                {
                    "question": "What can happen if DELETE is used without WHERE?",
                    "options": [
                        "All rows may be deleted",
                        "Only the first row is always deleted",
                        "The table is automatically backed up",
                        "No rows can ever be deleted"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "SQL Functions and Grouping",
            "content": """
SQL provides aggregate functions for calculations over multiple rows.

COUNT() counts records or non-NULL values, depending on its argument.
SUM() calculates a total.
AVG() calculates an average.
MIN() returns the minimum value.
MAX() returns the maximum value.

GROUP BY groups records with matching values.
HAVING filters grouped results, often using aggregate conditions.

Exercise:
Imagine a Marks table with student_name and marks columns.
Write a query to calculate the average marks.
""",
            "code": """-- Count students
SELECT COUNT(*) AS total_students
FROM Students;

-- Calculate the average age
SELECT AVG(age) AS average_age
FROM Students;

-- Group records by age
SELECT age, COUNT(*) AS student_count
FROM Students
GROUP BY age
HAVING COUNT(*) > 1;""",
            "quiz": [
                {
                    "question": "Which function counts rows?",
                    "options": ["SUM()", "COUNT()", "AVG()", "MIN()"],
                    "answer": 1
                },
                {
                    "question": "Which function calculates an average?",
                    "options": ["MAX()", "COUNT()", "AVG()", "SUM()"],
                    "answer": 2
                },
                {
                    "question": "What does GROUP BY do?",
                    "options": [
                        "Groups rows with matching values",
                        "Deletes duplicate tables",
                        "Creates a new database",
                        "Changes every value"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which clause filters grouped results?",
                    "options": ["WHERE only", "ORDER BY", "LIMIT", "HAVING"],
                    "answer": 3
                },
                {
                    "question": "Which function returns the largest value?",
                    "options": ["MAX()", "MIN()", "AVG()", "COUNT()"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 7,
            "title": "Relationships and Foreign Keys",
            "content": """
Relational databases connect tables using relationships.

Common relationship types:
- One-to-one: one record corresponds to one record.
- One-to-many: one record can relate to multiple records.
- Many-to-many: multiple records relate to multiple records,
  usually through a junction table.

A foreign key refers to a key in another table and helps maintain
referential integrity.

Example:
One department can have many students. Each student can store
a department_id that refers to a department.

Exercise:
Design Departments and Students tables connected by department_id.
""",
            "code": """CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE StudentsWithDepartment (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
);""",
            "quiz": [
                {
                    "question": "What is a foreign key used for?",
                    "options": [
                        "Changing font styles",
                        "Connecting related tables",
                        "Sorting a spreadsheet",
                        "Creating passwords"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which relationship lets one department have many students?",
                    "options": [
                        "One-to-one only",
                        "Many-to-many only",
                        "One-to-many",
                        "No relationship"
                    ],
                    "answer": 2
                },
                {
                    "question": "What does a foreign key help maintain?",
                    "options": [
                        "Referential integrity",
                        "Screen brightness",
                        "File formatting",
                        "Internet speed"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is often used to represent a many-to-many relationship?",
                    "options": [
                        "A comment",
                        "A display heading",
                        "A password",
                        "A junction table"
                    ],
                    "answer": 3
                },
                {
                    "question": "What does a foreign key reference?",
                    "options": [
                        "A key in a related table",
                        "A random picture",
                        "A CSS rule",
                        "A file extension"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 8,
            "title": "SQL JOIN Operations",
            "content": """
JOIN combines related data from two or more tables.

Common joins:
- INNER JOIN: returns rows with matching values in both tables.
- LEFT JOIN: returns all rows from the left table and matching
  rows from the right table; unmatched right-side values are NULL.
- RIGHT JOIN: returns all rows from the right table and matches
  from the left, where supported.
- FULL OUTER JOIN: returns matched and unmatched rows from both
  tables, where supported.

Join conditions commonly compare a primary key with a foreign key.

Exercise:
Write a query that displays each student's name and department name.
""",
            "code": """SELECT
    s.name,
    d.department_name
FROM StudentsWithDepartment AS s
INNER JOIN Departments AS d
    ON s.department_id = d.department_id;""",
            "quiz": [
                {
                    "question": "What is the purpose of JOIN?",
                    "options": [
                        "To combine related table data",
                        "To delete a database",
                        "To rename the computer",
                        "To create a website style"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which join returns only matching rows?",
                    "options": ["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "FULL JOIN"],
                    "answer": 1
                },
                {
                    "question": "Which join preserves all rows from the left table?",
                    "options": ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "No JOIN"],
                    "answer": 2
                },
                {
                    "question": "What does the ON clause specify in a JOIN?",
                    "options": [
                        "The database password",
                        "The screen layout",
                        "The table's file location",
                        "The join condition"
                    ],
                    "answer": 3
                },
                {
                    "question": "What may appear for unmatched right-table columns in a LEFT JOIN?",
                    "options": ["NULL", "Always zero", "Always true", "A new table"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 9,
            "title": "Database Normalization",
            "content": """
Normalization organizes data to reduce unnecessary duplication and
help prevent update anomalies.

First Normal Form (1NF):
- Each field contains a single value.
- Repeating groups are avoided.

Second Normal Form (2NF):
- The table is in 1NF.
- Non-key attributes depend on the whole candidate key, not just
  part of a composite key.

Third Normal Form (3NF):
- The table is in 2NF.
- Non-key attributes do not depend transitively on a candidate key.

Normalization can improve consistency, although some systems use
careful denormalization for performance.

Exercise:
Create a student table and identify any information that is
unnecessarily repeated.
""",
            "code": """-- Example of a normalized design
CREATE TABLE StudentsNormalized (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    department_id INTEGER
);

CREATE TABLE DepartmentDetails (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);""",
            "quiz": [
                {
                    "question": "What is a main goal of normalization?",
                    "options": [
                        "Increase unnecessary duplication",
                        "Reduce data redundancy",
                        "Remove all relationships",
                        "Prevent every possible error"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does 1NF require about field values?",
                    "options": [
                        "Every field must contain a list",
                        "Every field must be a number",
                        "Each field should contain a single value",
                        "Every table must have exactly two rows"
                    ],
                    "answer": 2
                },
                {
                    "question": "What does 2NF address?",
                    "options": [
                        "Partial dependency on part of a candidate key",
                        "Screen resolution",
                        "SQL comments",
                        "Network cables"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which normal form addresses transitive dependencies?",
                    "options": ["1NF only", "No normal form", "0NF", "3NF"],
                    "answer": 3
                },
                {
                    "question": "What is data redundancy?",
                    "options": [
                        "Unnecessary repeated data",
                        "A unique primary key",
                        "A SQL query",
                        "A table relationship"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "Transactions, ACID, and Indexes",
            "content": """
A transaction is a group of database operations treated as one
logical unit.

ACID properties:
- Atomicity: all operations in the transaction succeed or none do.
- Consistency: constraints remain satisfied.
- Isolation: concurrent transactions are controlled to avoid
  interfering incorrectly.
- Durability: committed changes persist.

Indexes can speed up searches and joins, but they require storage
and can slow down some INSERT, UPDATE, and DELETE operations.

Transactions commonly use:
- BEGIN or START TRANSACTION
- COMMIT to save changes
- ROLLBACK to undo uncommitted changes

Exact syntax varies between database systems.

Exercise:
Explain each ACID property in your own words.
""",
            "code": """-- Example transaction; syntax varies by database
BEGIN TRANSACTION;

UPDATE Students
SET age = age + 1
WHERE student_id = 1;

COMMIT;

-- Example index
CREATE INDEX idx_students_name
ON Students(name);""",
            "quiz": [
                {
                    "question": "What does ACID stand for?",
                    "options": [
                        "Atomicity, Consistency, Isolation, Durability",
                        "Access, Control, Internet, Data",
                        "Automatic, Clear, Internal, Delete",
                        "Array, Class, Index, Database"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does COMMIT do?",
                    "options": [
                        "Deletes every table",
                        "Saves a transaction's changes",
                        "Creates a new user automatically",
                        "Sorts all records"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does ROLLBACK generally do?",
                    "options": [
                        "Creates an index",
                        "Displays all databases",
                        "Undoes uncommitted transaction changes",
                        "Renames every column"
                    ],
                    "answer": 2
                },
                {
                    "question": "What is a common purpose of an index?",
                    "options": [
                        "Guarantee every query is instant",
                        "Replace the whole database",
                        "Prevent all duplicate values",
                        "Improve lookup performance"
                    ],
                    "answer": 3
                },
                {
                    "question": "What does durability mean in ACID?",
                    "options": [
                        "Committed changes persist",
                        "Every field is text",
                        "Every query deletes data",
                        "Transactions never fail"
                    ],
                    "answer": 0
                }
            ]
        }
    ]
},
{
    "id": "c-programming",
    "name": "C Programming",
    "icon": "💻",
    "description": "Learn C programming from the basics to functions, arrays, pointers, and file handling.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to C",
            "content": """
C is a general-purpose programming language widely used for system
software, embedded systems, and performance-sensitive applications.

A C program typically contains:
- Header files
- The main() function
- Statements
- A return statement

The compiler translates C source code into executable code.

Exercise:
Write a C program that displays your name.
""",
            "code": """#include <stdio.h>

int main(void) {
    printf("Hello, World!\\n");
    return 0;
}""",
            "quiz": [
                {
                    "question": "Who developed the C programming language?",
                    "options": [
                        "Dennis Ritchie",
                        "James Gosling",
                        "Guido van Rossum",
                        "Bjarne Stroustrup"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which function is the usual entry point of a C program?",
                    "options": ["start()", "main()", "run()", "begin()"],
                    "answer": 1
                },
                {
                    "question": "Which header provides printf()?",
                    "options": ["<string.h>", "<stdlib.h>", "<stdio.h>", "<math.h>"],
                    "answer": 2
                },
                {
                    "question": "Which symbol usually ends a C statement?",
                    "options": [":", ",", ".", ";"],
                    "answer": 3
                },
                {
                    "question": "What does printf() do?",
                    "options": [
                        "Displays formatted output",
                        "Reads a file only",
                        "Creates a variable",
                        "Stops the compiler"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 2,
            "title": "Variables and Data Types",
            "content": """
Variables store values that a program can use.

Common C data types:
- int: integer values
- char: character values
- float: single-precision floating-point values
- double: double-precision floating-point values

A variable should be declared before it is used.

Use meaningful variable names and initialize variables before
reading their values.

Exercise:
Declare variables for your age, grade, and average score.
""",
            "code": """#include <stdio.h>

int main(void) {
    int age = 18;
    char grade = 'A';
    float average = 85.5f;

    printf("Age: %d\\n", age);
    printf("Grade: %c\\n", grade);
    printf("Average: %.1f\\n", average);

    return 0;
}""",
            "quiz": [
                {
                    "question": "Which data type stores an integer?",
                    "options": ["char", "int", "float", "void"],
                    "answer": 1
                },
                {
                    "question": "Which data type stores a single character?",
                    "options": ["int", "double", "char", "long"],
                    "answer": 2
                },
                {
                    "question": "Which format specifier is commonly used for int in printf()?",
                    "options": ["%d", "%c", "%s", "%f"],
                    "answer": 0
                },
                {
                    "question": "Which declaration initializes an integer to 10?",
                    "options": ["int = 10;", "10 int x;", "x int = 10;", "int x = 10;"],
                    "answer": 3
                },
                {
                    "question": "Which type is commonly used for decimal values?",
                    "options": ["float", "char", "void", "int"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 3,
            "title": "Operators in C",
            "content": """
Operators perform calculations and comparisons.

Arithmetic operators:
+ addition
- subtraction
* multiplication
/ division
% remainder for integer operands

Comparison operators include ==, !=, >, <, >=, and <=.

Logical operators:
&& means AND
|| means OR
! means NOT

Remember: = assigns a value, while == compares values.

Exercise:
Write a program that adds two integers and prints the result.
""",
            "code": """#include <stdio.h>

int main(void) {
    int a = 10;
    int b = 3;

    printf("Sum: %d\\n", a + b);
    printf("Product: %d\\n", a * b);
    printf("Remainder: %d\\n", a % b);

    return 0;
}""",
            "quiz": [
                {
                    "question": "Which operator performs multiplication?",
                    "options": ["+", "*", "/", "%"],
                    "answer": 1
                },
                {
                    "question": "What does == test?",
                    "options": ["Assignment", "Addition", "Equality", "Division"],
                    "answer": 2
                },
                {
                    "question": "What is 10 % 3 in C?",
                    "options": ["1", "3", "0", "10"],
                    "answer": 0
                },
                {
                    "question": "Which operator means logical AND?",
                    "options": ["||", "!", "&", "&&"],
                    "answer": 3
                },
                {
                    "question": "Which operator assigns a value?",
                    "options": ["=", "==", "!=", "<="],
                    "answer": 0
                }
            ]
        },
        {
            "id": 4,
            "title": "Conditional Statements",
            "content": """
Conditional statements let a program choose which code to execute.

The if statement runs code when a condition is true.
else provides an alternative.
else if checks another condition.
switch selects among cases based on an expression.

Use braces to make code blocks clear. Remember to use break in
switch cases when you do not want execution to continue into the
next case.

Exercise:
Write a program that checks whether an integer is positive,
negative, or zero.
""",
            "code": """#include <stdio.h>

int main(void) {
    int number = 7;

    if (number > 0) {
        printf("Positive\\n");
    } else if (number < 0) {
        printf("Negative\\n");
    } else {
        printf("Zero\\n");
    }

    return 0;
}""",
            "quiz": [
                {
                    "question": "Which statement checks a condition?",
                    "options": ["if", "include", "printf", "return"],
                    "answer": 0
                },
                {
                    "question": "Which keyword provides an alternative branch?",
                    "options": ["case", "else", "break", "define"],
                    "answer": 1
                },
                {
                    "question": "Which statement is useful for selecting among cases?",
                    "options": ["while", "for", "switch", "sizeof"],
                    "answer": 2
                },
                {
                    "question": "What does break commonly do inside a switch case?",
                    "options": [
                        "Starts the program again",
                        "Declares a variable",
                        "Prints a message",
                        "Exits the switch"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which operator means 'greater than'?",
                    "options": [">", "<", "=", "!="],
                    "answer": 0
                }
            ]
        },
        {
            "id": 5,
            "title": "Loops in C",
            "content": """
Loops repeat a block of code.

The for loop is useful when the iteration pattern is known.
The while loop checks its condition before each iteration.
The do-while loop executes its body at least once before checking
the condition.

Be careful to update loop variables so that loops eventually stop.

Exercise:
Write a loop that prints numbers from 1 to 10.
""",
            "code": """#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 10; i++) {
        printf("%d\\n", i);
    }

    return 0;
}""",
            "quiz": [
                {
                    "question": "Which loop is often used when the number of iterations is known?",
                    "options": ["switch", "for", "if", "typedef"],
                    "answer": 1
                },
                {
                    "question": "Which loop always executes its body at least once?",
                    "options": ["for", "while", "do-while", "if"],
                    "answer": 2
                },
                {
                    "question": "Which keyword skips to the next loop iteration?",
                    "options": ["continue", "return", "case", "struct"],
                    "answer": 0
                },
                {
                    "question": "Which keyword exits a loop immediately?",
                    "options": ["const", "void", "static", "break"],
                    "answer": 3
                },
                {
                    "question": "What can cause an unintended infinite loop?",
                    "options": [
                        "A condition that never becomes false",
                        "Using a valid variable",
                        "Printing one message",
                        "Including a header"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "Functions in C",
            "content": """
Functions organize programs into reusable blocks.

A function can have:
- A return type
- A function name
- Parameters
- A body

A function prototype tells the compiler about a function before
its definition is used.

Parameters receive values, and return sends a result back to the
caller when the return type is not void.

Exercise:
Create a function that receives two integers and returns their sum.
""",
            "code": """#include <stdio.h>

int add(int a, int b);

int main(void) {
    printf("Sum: %d\\n", add(4, 6));
    return 0;
}

int add(int a, int b) {
    return a + b;
}""",
            "quiz": [
                {
                    "question": "Why are functions useful?",
                    "options": [
                        "They make variables unnecessary",
                        "They support reusable code",
                        "They replace all data types",
                        "They prevent every bug"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does a function return type specify?",
                    "options": [
                        "The file name",
                        "The loop count",
                        "The type of value returned",
                        "The keyboard layout"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which keyword indicates that a function returns no value?",
                    "options": ["void", "int", "char", "switch"],
                    "answer": 0
                },
                {
                    "question": "What is a function prototype?",
                    "options": [
                        "A loop condition",
                        "A file extension",
                        "A printed result",
                        "A declaration describing a function"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which keyword sends a value back from a function?",
                    "options": ["return", "break", "continue", "case"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 7,
            "title": "Arrays and Strings",
            "content": """
An array stores multiple elements of the same type in consecutive
array positions. C array indexes begin at zero.

For an array with five elements, valid indexes are 0 through 4.
Accessing an index outside the valid range causes undefined behavior.

A C string is a character array terminated by the null character
'\\0'. The string functions declared in <string.h> can help
manipulate strings.

Exercise:
Create an array of five integers and calculate their total.
""",
            "code": """#include <stdio.h>
#include <string.h>

int main(void) {
    int numbers[] = {10, 20, 30, 40, 50};
    char name[] = "Study Pilot";

    printf("First number: %d\\n", numbers[0]);
    printf("Array size: %zu\\n",
           sizeof(numbers) / sizeof(numbers[0]));
    printf("Name length: %zu\\n", strlen(name));

    return 0;
}""",
            "quiz": [
                {
                    "question": "What is the index of the first array element?",
                    "options": ["1", "0", "-1", "Depends on the compiler"],
                    "answer": 1
                },
                {
                    "question": "What kind of elements does a normal C array store?",
                    "options": [
                        "Only functions",
                        "Only files",
                        "Elements of one declared type",
                        "Only strings"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which character terminates a C string?",
                    "options": ["'\\0'", "' '", "'\\n'", "'\\t'"],
                    "answer": 0
                },
                {
                    "question": "Which header declares strlen()?",
                    "options": ["<stdio.h>", "<stdlib.h>", "<math.h>", "<string.h>"],
                    "answer": 3
                },
                {
                    "question": "How many elements are in int a[] = {2, 4, 6}?",
                    "options": ["3", "2", "4", "6"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 8,
            "title": "Pointers",
            "content": """
A pointer stores the memory address of an object or function,
depending on its type.

The & operator obtains the address of an object.
The * operator dereferences a pointer to access the pointed-to
object.

Pointers are useful for working with arrays, dynamic memory,
and functions that need to modify caller-owned values.

Only dereference a pointer when it points to a valid object.
A null pointer does not point to a valid object.

Exercise:
Declare an integer and a pointer to that integer, then print
the value through the pointer.
""",
            "code": """#include <stdio.h>

int main(void) {
    int number = 25;
    int *pointer = &number;

    printf("Value: %d\\n", number);
    printf("Through pointer: %d\\n", *pointer);

    return 0;
}""",
            "quiz": [
                {
                    "question": "What does a pointer store?",
                    "options": [
                        "Only a character",
                        "A memory address",
                        "A loop condition",
                        "A file extension"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which operator obtains an object's address?",
                    "options": ["*", "%", "&", "!"],
                    "answer": 2
                },
                {
                    "question": "What does *pointer do in an expression?",
                    "options": [
                        "Accesses the pointed-to object",
                        "Creates a new database",
                        "Ends the program",
                        "Sorts an array"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does NULL represent for a pointer?",
                    "options": [
                        "A guaranteed valid object",
                        "The first array element",
                        "An integer multiplication",
                        "A pointer that does not point to a valid object"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which declaration defines a pointer to int?",
                    "options": ["int *p;", "int p*;", "*int p;", "pointer int p;"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 9,
            "title": "Structures and Dynamic Memory",
            "content": """
A structure groups related values, possibly of different types,
under one type.

The dot operator accesses a structure member.
The arrow operator accesses a member through a pointer to a
structure.

Dynamic memory allocation functions are declared in <stdlib.h>:
- malloc() allocates a block of memory.
- calloc() allocates and zero-initializes memory.
- realloc() changes the size of an allocation.
- free() releases allocated memory.

Check allocation results before using the returned pointer, and
release dynamically allocated memory when it is no longer needed.

Exercise:
Define a Student structure with an ID and a name.
""",
            "code": """#include <stdio.h>
#include <stdlib.h>

struct Student {
    int id;
    char grade;
};

int main(void) {
    struct Student student = {1, 'A'};
    int *value = malloc(sizeof *value);

    if (value == NULL) {
        return 1;
    }

    *value = 100;

    printf("Student ID: %d\\n", student.id);
    printf("Grade: %c\\n", student.grade);
    printf("Value: %d\\n", *value);

    free(value);
    return 0;
}""",
            "quiz": [
                {
                    "question": "What is a structure used for?",
                    "options": [
                        "Grouping related values of different types",
                        "Repeating a loop",
                        "Sorting source code",
                        "Creating a comment"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which operator accesses a member through a structure variable?",
                    "options": ["->", ".", "&", "%"],
                    "answer": 1
                },
                {
                    "question": "Which function allocates memory dynamically?",
                    "options": ["printf()", "strlen()", "malloc()", "strcmp()"],
                    "answer": 2
                },
                {
                    "question": "Which function releases memory allocated dynamically?",
                    "options": ["calloc()", "realloc()", "malloc()", "free()"],
                    "answer": 3
                },
                {
                    "question": "Why should malloc() results be checked?",
                    "options": [
                        "Allocation can fail",
                        "It always returns an integer",
                        "It automatically prints the result",
                        "It creates a structure every time"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "File Handling and Preprocessor",
            "content": """
C programs can read and write files using functions from <stdio.h>.

Common file functions:
- fopen() opens a file.
- fprintf() writes formatted text to a file.
- fscanf() reads formatted data.
- fgets() reads a line or part of a line.
- fclose() closes a file.

Always check whether fopen() returned NULL before using the file.
Close files when finished.

Preprocessor directives begin with #.
#include includes a header, while #define defines a macro.

Exercise:
Write a program that opens a text file, writes a message, and
closes the file.
""",
            "code": """#include <stdio.h>

int main(void) {
    FILE *file = fopen("study.txt", "w");

    if (file == NULL) {
        perror("Could not open file");
        return 1;
    }

    fprintf(file, "Welcome to Study Pilot!\\n");
    fclose(file);

    return 0;
}""",
            "quiz": [
                {
                    "question": "Which function opens a file?",
                    "options": ["fopen()", "fclose()", "printf()", "strlen()"],
                    "answer": 0
                },
                {
                    "question": "Which function closes an open file?",
                    "options": ["fgets()", "fclose()", "fopen()", "malloc()"],
                    "answer": 1
                },
                {
                    "question": "What does fopen() return when it cannot open a file?",
                    "options": ["An empty string", "The number zero as a file", "NULL", "A new file every time"],
                    "answer": 2
                },
                {
                    "question": "Which directive includes a header file?",
                    "options": ["#return", "#main", "#loop", "#include"],
                    "answer": 3
                },
                {
                    "question": "Which mode commonly opens a file for writing and truncates existing content?",
                    "options": ["\"w\"", "\"r\"", "\"a\"", "\"x\""],
                    "answer": 0
                }
            ]
        }
    ]
},
    {
    "id": "dsa",
    "name": "Data Structures and Algorithms",
    "icon": "🧠",
    "description": "Learn data structures, searching, sorting, trees, graphs, and algorithm analysis.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to Data Structures and Algorithms",
            "content": """
A data structure organizes data so it can be accessed and modified
efficiently.

An algorithm is a sequence of steps used to solve a problem.

Examples of data structures:
- Arrays
- Linked lists
- Stacks
- Queues
- Trees
- Graphs
- Hash tables

When choosing a data structure, consider how often you need to
search, insert, delete, or update data.

Exercise:
List three data structures and describe one use for each.
""",
            "code": """numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)""",
            "quiz": [
                {
                    "question": "What is a data structure?",
                    "options": [
                        "A way to organize and store data",
                        "A programming error",
                        "A computer monitor",
                        "A type of comment"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is an algorithm?",
                    "options": [
                        "A database table",
                        "A sequence of steps to solve a problem",
                        "A programming language only",
                        "A computer component"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which is a data structure?",
                    "options": ["Loop", "Variable name", "Stack", "Comment"],
                    "answer": 2
                },
                {
                    "question": "What should influence the choice of a data structure?",
                    "options": [
                        "The computer's wallpaper",
                        "The length of a comment",
                        "The programmer's keyboard",
                        "The operations the program needs"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which operation finds an item?",
                    "options": ["Searching", "Formatting", "Compiling", "Printing"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 2,
            "title": "Arrays and Lists",
            "content": """
An array stores elements in indexed positions. In Python, lists
provide a flexible sequence that can grow or shrink.

Python list indexes start at zero.

Common operations:
- Append: add an item to the end.
- Insert: add an item at a position.
- Remove: remove a matching item.
- Access: retrieve an item using its index.

Accessing an item by index is generally O(1).
Searching an unsorted list is generally O(n).

Exercise:
Create a list of five numbers and calculate their total.
""",
            "code": """numbers = [10, 20, 30, 40, 50]

numbers.append(60)
print("First item:", numbers[0])
print("All items:", numbers)
print("Total:", sum(numbers))""",
            "quiz": [
                {
                    "question": "What is the index of the first Python list item?",
                    "options": ["1", "0", "-1", "2"],
                    "answer": 1
                },
                {
                    "question": "Which method adds an item to the end of a list?",
                    "options": ["remove()", "insert()", "append()", "clear()"],
                    "answer": 2
                },
                {
                    "question": "What is the time complexity of accessing a list item by index?",
                    "options": ["O(1)", "O(n)", "O(n²)", "O(2ⁿ)"],
                    "answer": 0
                },
                {
                    "question": "Which function calculates the sum of numeric list items?",
                    "options": ["count()", "sort()", "len()", "sum()"],
                    "answer": 3
                },
                {
                    "question": "What is the usual time complexity of searching an unsorted list?",
                    "options": ["O(n)", "O(1) always", "O(log n) always", "O(0)"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 3,
            "title": "Stacks and Queues",
            "content": """
A stack follows LIFO: Last In, First Out.

A queue follows FIFO: First In, First Out.

Stack operations:
- Push: add an item.
- Pop: remove the most recently added item.

Queue operations:
- Enqueue: add an item.
- Dequeue: remove the oldest item.

Stacks are useful for undo operations and function calls.
Queues are useful for scheduling and processing requests.

Exercise:
Write a stack using a Python list and a queue using collections.deque.
""",
            "code": """from collections import deque

# Stack: last in, first out
stack = []
stack.append("A")
stack.append("B")
print("Stack pop:", stack.pop())

# Queue: first in, first out
queue = deque(["A", "B"])
print("Queue removal:", queue.popleft())""",
            "quiz": [
                {
                    "question": "What does LIFO mean?",
                    "options": [
                        "Last In, First Out",
                        "Last In, First Open",
                        "List Input, First Output",
                        "Least Input, Fast Output"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which data structure follows FIFO?",
                    "options": ["Stack", "Queue", "Tree", "Graph"],
                    "answer": 1
                },
                {
                    "question": "What is adding an item to a stack called?",
                    "options": ["Dequeue", "Search", "Push", "Sort"],
                    "answer": 2
                },
                {
                    "question": "Which structure is commonly useful for undo operations?",
                    "options": ["Queue only", "Graph only", "Hash table only", "Stack"],
                    "answer": 3
                },
                {
                    "question": "Which Python structure supports efficient removal from the front of a queue?",
                    "options": ["collections.deque", "A string", "A float", "A Boolean"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 4,
            "title": "Linked Lists",
            "content": """
A linked list contains nodes. Each node stores data and a reference
to another node.

In a singly linked list, each node points to the next node.
A doubly linked list has references to both the next and previous
nodes.

Advantages:
- Nodes do not need to be stored next to each other in memory.
- Insertion can be efficient when the relevant node is already known.

Disadvantages:
- Accessing an item by position requires traversal.
- Each node requires extra memory for references.

Exercise:
Create a simple linked list with three nodes.
""",
            "code": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

current = first
while current is not None:
    print(current.data)
    current = current.next""",
            "quiz": [
                {
                    "question": "What does a linked list contain?",
                    "options": [
                        "Only numbers without connections",
                        "Nodes connected by references",
                        "Only database tables",
                        "Only sorted values"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does a node in a singly linked list point to?",
                    "options": ["Every node automatically", "The previous node only", "The next node", "No node ever"],
                    "answer": 2
                },
                {
                    "question": "What is one disadvantage of a linked list?",
                    "options": [
                        "Access by position usually requires traversal",
                        "It cannot store data",
                        "It must always be sorted",
                        "It cannot contain nodes"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does the next reference represent?",
                    "options": [
                        "A file name",
                        "A numeric total",
                        "The list length",
                        "The link to the next node"
                    ],
                    "answer": 3
                },
                {
                    "question": "What extra cost do linked-list nodes commonly have?",
                    "options": [
                        "Memory for references",
                        "A mandatory database",
                        "A graphics card",
                        "A network connection"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 5,
            "title": "Searching Algorithms",
            "content": """
Searching algorithms locate a target value.

Linear search checks elements one by one. It works on unsorted
sequences and takes O(n) time in the worst case.

Binary search repeatedly halves the search range. It requires
the input to be sorted and takes O(log n) time in the usual case.

Exercise:
Implement linear search and binary search in Python.
""",
            "code": """def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


values = [10, 20, 30, 40, 50]
print(linear_search(values, 30))
print(binary_search(values, 40))""",
            "quiz": [
                {
                    "question": "Which search checks items one by one?",
                    "options": ["Binary search", "Linear search", "Merge sort", "Quick sort"],
                    "answer": 1
                },
                {
                    "question": "What condition does binary search require?",
                    "options": [
                        "Every item must be a string",
                        "The list must contain one item",
                        "The data must be sorted",
                        "The data must be random"
                    ],
                    "answer": 2
                },
                {
                    "question": "What is the worst-case time complexity of linear search?",
                    "options": ["O(n)", "O(1) always", "O(log n)", "O(n log n) always"],
                    "answer": 0
                },
                {
                    "question": "What is the usual time complexity of binary search?",
                    "options": ["O(n²)", "O(n)", "O(2ⁿ)", "O(log n)"],
                    "answer": 3
                },
                {
                    "question": "What does returning -1 commonly indicate in these examples?",
                    "options": ["The target was not found", "The target is at index zero", "The list was sorted", "The search succeeded"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "Sorting Algorithms",
            "content": """
Sorting arranges data in a chosen order.

Bubble sort repeatedly compares adjacent items and swaps them
when they are in the wrong order. Its worst-case time complexity
is O(n²).

Merge sort divides the data, sorts the parts, and merges them.
Its usual time complexity is O(n log n).

Python's built-in sorted() function is generally preferable in
ordinary Python programs because it is efficient and well tested.

Exercise:
Sort a list of numbers using sorted() and implement bubble sort.
""",
            "code": """def bubble_sort(items):
    result = items.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = (
                    result[j + 1], result[j]
                )
                swapped = True

        if not swapped:
            break

    return result


numbers = [5, 2, 8, 1, 3]
print(bubble_sort(numbers))
print(sorted(numbers))""",
            "quiz": [
                {
                    "question": "What does sorting do?",
                    "options": [
                        "Arranges data in an order",
                        "Deletes every value",
                        "Creates a database",
                        "Changes the programming language"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which sorting algorithm repeatedly compares adjacent items?",
                    "options": ["Binary search", "Bubble sort", "Linear search", "BFS"],
                    "answer": 1
                },
                {
                    "question": "What is the usual worst-case complexity of bubble sort?",
                    "options": ["O(1)", "O(log n)", "O(n²)", "O(log log n)"],
                    "answer": 2
                },
                {
                    "question": "What is the usual time complexity of merge sort?",
                    "options": ["O(n²)", "O(2ⁿ)", "O(n³)", "O(n log n)"],
                    "answer": 3
                },
                {
                    "question": "Which Python function returns a new sorted list?",
                    "options": ["sorted()", "append()", "pop()", "input()"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 7,
            "title": "Hash Tables and Dictionaries",
            "content": """
A hash table stores key-value pairs and uses a hash function to
help locate values.

Python dictionaries provide key-value storage.

Average lookup, insertion, and deletion are generally O(1), although
performance can vary and worst-case operations can take longer.

Keys must be hashable. Dictionary keys are unique; assigning a value
to an existing key replaces its previous value.

Exercise:
Create a dictionary of student names and marks, then retrieve one
student's marks.
""",
            "code": """marks = {
    "Anu": 85,
    "Ravi": 92,
    "Meera": 88
}

print("Ravi's marks:", marks["Ravi"])

marks["Kiran"] = 90
print("All marks:", marks)""",
            "quiz": [
                {
                    "question": "What does a dictionary store?",
                    "options": [
                        "Only sorted numbers",
                        "Key-value pairs",
                        "Only characters",
                        "Only functions"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which Python type provides dictionary functionality?",
                    "options": ["list", "tuple", "dict", "set"],
                    "answer": 2
                },
                {
                    "question": "What is the average lookup complexity of a Python dictionary?",
                    "options": ["O(1)", "O(n²)", "O(2ⁿ)", "O(n log n) always"],
                    "answer": 0
                },
                {
                    "question": "What happens when a value is assigned to an existing dictionary key?",
                    "options": [
                        "The whole dictionary disappears",
                        "The key must become a list",
                        "The program always stops",
                        "The value for that key is replaced"
                    ],
                    "answer": 3
                },
                {
                    "question": "What must a Python dictionary key be?",
                    "options": [
                        "Hashable",
                        "A list in every case",
                        "A floating-point number only",
                        "A function only"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 8,
            "title": "Trees and Binary Search Trees",
            "content": """
A tree is a hierarchical data structure made of nodes.

Important terms:
- Root: the top node.
- Parent: a node with children.
- Leaf: a node without children.
- Height: the length of the longest downward path, according
  to the convention used.

A binary tree has at most two children per node.

In a binary search tree, values in the left subtree are smaller
and values in the right subtree are larger, subject to the
implementation's duplicate-value policy.

Exercise:
Draw a binary search tree containing 50, 30, 70, 20, and 40.
""",
            "code": """class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


inorder(root)""",
            "quiz": [
                {
                    "question": "What is the top node of a tree called?",
                    "options": ["Leaf", "Root", "Edge", "Queue"],
                    "answer": 1
                },
                {
                    "question": "How many children can a binary tree node have at most?",
                    "options": ["One", "Three", "Two", "Unlimited"],
                    "answer": 2
                },
                {
                    "question": "What is a leaf node?",
                    "options": [
                        "A node without children",
                        "The top node in every tree",
                        "A sorting algorithm",
                        "A database column"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which traversal visits left subtree, node, then right subtree?",
                    "options": ["Level order", "Preorder", "Postorder", "Inorder"],
                    "answer": 3
                },
                {
                    "question": "What is a common property of a binary search tree?",
                    "options": [
                        "Left values are smaller and right values are larger, subject to its duplicate policy",
                        "Every node must have two children",
                        "Every value must be identical",
                        "It cannot be searched"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 9,
            "title": "Graphs and Graph Traversal",
            "content": """
A graph contains vertices (nodes) connected by edges.

Graphs may be:
- Directed or undirected.
- Weighted or unweighted.
- Connected or disconnected.

Breadth-first search (BFS) explores nearby vertices first and
commonly uses a queue.

Depth-first search (DFS) explores a path deeply before returning
to other branches. It can use recursion or a stack.

BFS and DFS commonly run in O(V + E) time with an adjacency-list
representation, where V is the number of vertices and E is the
number of edges.

Exercise:
Represent a small friendship network as a graph and traverse it.
""",
            "code": """from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}


def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, "A")""",
            "quiz": [
                {
                    "question": "What are the basic components of a graph?",
                    "options": [
                        "Functions and comments",
                        "Vertices and edges",
                        "Rows and columns only",
                        "Files and folders"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which structure is commonly used by BFS?",
                    "options": ["Stack only", "Tree only", "Queue", "String"],
                    "answer": 2
                },
                {
                    "question": "What does DFS stand for?",
                    "options": [
                        "Depth-First Search",
                        "Data-First Sorting",
                        "Direct File System",
                        "Double Function Search"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does V represent in graph complexity notation?",
                    "options": ["Variables only", "Versions", "Values only", "Vertices"],
                    "answer": 3
                },
                {
                    "question": "What does an edge represent?",
                    "options": [
                        "A connection between vertices",
                        "The program's title",
                        "A sorting result",
                        "A Python keyword"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "Algorithm Complexity and Recursion",
            "content": """
Algorithm analysis estimates how resource usage grows as input
size increases.

Big O notation describes an asymptotic upper bound and is commonly
used to discuss worst-case growth.

Examples:
- O(1): constant time
- O(log n): logarithmic time
- O(n): linear time
- O(n log n): linearithmic time
- O(n²): quadratic time

Recursion occurs when a function calls itself. A recursive solution
needs a base case to stop the calls.

Exercise:
Write a recursive function that calculates the factorial of a
non-negative integer.
""",
            "code": """def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))  # 120""",
            "quiz": [
                {
                    "question": "What does O(1) describe?",
                    "options": [
                        "Constant-time growth",
                        "Quadratic growth",
                        "Exponential growth",
                        "Linear growth"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which complexity grows linearly with input size?",
                    "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
                    "answer": 1
                },
                {
                    "question": "What is recursion?",
                    "options": [
                        "Sorting a list",
                        "Creating a dictionary",
                        "A function calling itself",
                        "Removing a variable"
                    ],
                    "answer": 2
                },
                {
                    "question": "Why does a recursive function need a base case?",
                    "options": [
                        "To make every value a string",
                        "To sort the result",
                        "To create a graph",
                        "To stop recursion from continuing indefinitely"
                    ],
                    "answer": 3
                },
                {
                    "question": "What is 5 factorial (5!)?",
                    "options": ["120", "25", "15", "10"],
                    "answer": 0
                }
            ]
        }
    ]
},
        
    {
    "id": "data-science",
    "name": "Data Science",
    "icon": "📊",
    "description": "Learn Python, data analysis, visualization, statistics, and machine learning fundamentals.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to Data Science",
            "content": """
Data Science uses data, statistics, programming, and domain knowledge
to answer questions and support decisions.

A typical data science workflow includes:
1. Define the problem.
2. Collect relevant data.
3. Clean and prepare the data.
4. Explore and analyze the data.
5. Visualize important patterns.
6. Build and evaluate models when appropriate.
7. Communicate findings.

Data science is used in healthcare, education, business, science,
transportation, and many other fields.

Exercise:
Choose a real-world question that could be investigated using data.
List three types of data that might help answer it.
""",
            "code": """# A tiny example of analyzing data

scores = [75, 80, 90, 85, 70]

average = sum(scores) / len(scores)

print("Number of scores:", len(scores))
print("Average score:", average)""",
            "quiz": [
                {
                    "question": "What is a major goal of data science?",
                    "options": [
                        "Extract useful insights from data",
                        "Replace all human decisions",
                        "Create computer hardware",
                        "Design websites only"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which skill is useful in data science?",
                    "options": [
                        "Typing only",
                        "Statistics",
                        "Drawing only",
                        "Gaming only"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is data cleaning?",
                    "options": [
                        "Deleting every dataset",
                        "Changing all values to zero",
                        "Finding and correcting data problems",
                        "Designing a logo"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which is a possible data science application?",
                    "options": [
                        "Predicting demand",
                        "Replacing electricity",
                        "Preventing every error",
                        "Making all data perfect"
                    ],
                    "answer": 0
                },
                {
                    "question": "Why communicate data science results?",
                    "options": [
                        "To hide the analysis",
                        "To make the dataset larger",
                        "To avoid checking results",
                        "To explain findings and limitations"
                    ],
                    "answer": 3
                }
            ]
        },
        {
            "id": 2,
            "title": "Python for Data Science",
            "content": """
Python is widely used in data science because it has a readable
syntax and many useful libraries.

Important libraries include:
- NumPy for numerical computing.
- pandas for working with structured data.
- Matplotlib for plotting.
- scikit-learn for machine learning.

Python lists, dictionaries, loops, functions, and conditions are
useful foundations.

Install libraries in your development environment when needed.
For example: pip install numpy pandas matplotlib scikit-learn

Exercise:
Create a list of measurements and calculate their average.
""",
            "code": """measurements = [12, 15, 18, 14, 16]

total = sum(measurements)
average = total / len(measurements)

print("Total:", total)
print("Average:", average)""",
            "quiz": [
                {
                    "question": "Which language is commonly used in data science?",
                    "options": ["HTML only", "Python", "CSS only", "SQL is a programming language"],
                    "answer": 1
                },
                {
                    "question": "Which library is widely used for numerical arrays?",
                    "options": ["Flask", "BeautifulSoup", "NumPy", "Django"],
                    "answer": 2
                },
                {
                    "question": "Which library is useful for tabular data analysis?",
                    "options": ["pandas", "turtle only", "pygame only", "tkinter only"],
                    "answer": 0
                },
                {
                    "question": "Which Python function calculates a total for numeric values?",
                    "options": ["len()", "type()", "range()", "sum()"],
                    "answer": 3
                },
                {
                    "question": "What is a Python library?",
                    "options": [
                        "A collection of reusable code",
                        "A physical computer",
                        "A database row only",
                        "A programming error"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 3,
            "title": "Understanding Data Types",
            "content": """
Data can appear in several forms.

Numerical data represents quantities, such as age or temperature.
Categorical data represents groups, such as subject or city.
Ordinal data has a meaningful order, such as beginner, intermediate,
and advanced.
Text data contains words or sentences.
Time-series data records measurements over time.

Correctly identifying data types helps you choose suitable
summaries, visualizations, and analysis methods.

Exercise:
Classify age, city, satisfaction rating, and daily temperature.
Explain your choices.
""",
            "code": """records = [
    {"city": "Hyderabad", "temperature": 32.5},
    {"city": "Chennai", "temperature": 34.0},
    {"city": "Delhi", "temperature": 30.5}
]

for record in records:
    print(
        record["city"],
        record["temperature"]
    )""",
            "quiz": [
                {
                    "question": "Which is an example of numerical data?",
                    "options": ["City name", "Temperature", "Favorite color", "Book title"],
                    "answer": 1
                },
                {
                    "question": "Which is an example of categorical data?",
                    "options": ["Height in cm", "Weight in kg", "Type of vehicle", "Temperature in Celsius"],
                    "answer": 2
                },
                {
                    "question": "What characterizes ordinal data?",
                    "options": [
                        "Categories have a meaningful order",
                        "It always contains only decimals",
                        "It has no categories",
                        "It must contain images"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which is an example of time-series data?",
                    "options": [
                        "A list of colors",
                        "A collection of names without dates",
                        "A single book title",
                        "Daily rainfall measurements over a month"
                    ],
                    "answer": 3
                },
                {
                    "question": "Why identify data types before analysis?",
                    "options": [
                        "To select appropriate methods",
                        "To remove every record",
                        "To make all values identical",
                        "To avoid understanding the problem"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 4,
            "title": "Data Cleaning and Preparation",
            "content": """
Real-world data may contain missing values, duplicates, inconsistent
formats, and incorrect entries.

Data cleaning involves detecting and handling these problems.

Common steps:
- Check missing values.
- Find duplicate records.
- Correct inconsistent formats.
- Check values against reasonable rules.
- Convert columns to suitable types.
- Document important changes.

Do not automatically remove every unusual value. Investigate it
first because it may be a genuine observation.

Exercise:
Create a small dataset with a missing value and a duplicate.
Describe how you would handle each problem.
""",
            "code": """import pandas as pd

data = {
    "name": ["Anu", "Ravi", "Anu", "Meera"],
    "score": [85, None, 85, 92]
}

df = pd.DataFrame(data)

print("Missing values:")
print(df.isna().sum())

# Remove exact duplicate rows
cleaned = df.drop_duplicates()

# Fill missing scores with the column average
cleaned["score"] = cleaned["score"].fillna(
    cleaned["score"].mean()
)

print(cleaned)""",
            "quiz": [
                {
                    "question": "What is data cleaning?",
                    "options": [
                        "Finding and handling data quality problems",
                        "Decorating a chart",
                        "Creating a new programming language",
                        "Increasing every value"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which pandas method detects missing values?",
                    "options": ["sort_values()", "isna()", "head()", "rename()"],
                    "answer": 1
                },
                {
                    "question": "Which method removes duplicate rows?",
                    "options": ["fillna()", "describe()", "drop_duplicates()", "groupby()"],
                    "answer": 2
                },
                {
                    "question": "What should you do before removing an unusual value?",
                    "options": [
                        "Always replace it with zero",
                        "Delete the entire dataset",
                        "Ignore every data quality issue",
                        "Investigate whether it is an error or a genuine observation"
                    ],
                    "answer": 3
                },
                {
                    "question": "Why document data-cleaning steps?",
                    "options": [
                        "To make the process understandable and reproducible",
                        "To hide the changes",
                        "To make every dataset identical",
                        "To avoid checking data"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 5,
            "title": "Exploratory Data Analysis",
            "content": """
Exploratory Data Analysis (EDA) helps you understand a dataset
before drawing conclusions or building models.

Useful activities include:
- Inspecting the first few rows.
- Checking the number of rows and columns.
- Examining data types.
- Calculating descriptive statistics.
- Checking missing values.
- Looking for patterns and unusual observations.

Mean is the arithmetic average.
Median is the middle value after sorting.
Mode is the most frequent value.

The median is often less affected by extreme values than the mean.

Exercise:
Calculate the mean and median of five numbers and compare them.
""",
            "code": """import pandas as pd

df = pd.DataFrame({
    "score": [65, 70, 75, 80, 95]
})

print(df.head())
print(df.shape)
print(df.describe())
print("Mean:", df["score"].mean())
print("Median:", df["score"].median())""",
            "quiz": [
                {
                    "question": "What does EDA stand for?",
                    "options": [
                        "External Data Access",
                        "Exploratory Data Analysis",
                        "Electronic Design Application",
                        "Estimated Database Average"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is the mean?",
                    "options": [
                        "The largest value",
                        "The smallest value",
                        "The arithmetic average",
                        "The most frequent text label"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which statistic is the middle value after sorting?",
                    "options": ["Median", "Mean", "Range", "Variance"],
                    "answer": 0
                },
                {
                    "question": "Which pandas method provides descriptive statistics?",
                    "options": ["drop()", "rename()", "tail()", "describe()"],
                    "answer": 3
                },
                {
                    "question": "Which statistic is often less affected by extreme values?",
                    "options": ["Median", "Mean", "Maximum", "Sum"],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "Data Visualization",
            "content": """
Data visualization communicates patterns using charts and graphs.

Common charts:
- Bar chart: compares categories.
- Line chart: shows changes over an ordered sequence, often time.
- Histogram: displays the distribution of numerical data.
- Scatter plot: shows the relationship between two numerical variables.
- Pie chart: shows parts of a whole when categories are limited.

Choose a chart that matches the question. Include readable labels,
a clear title, and appropriate scales.

Charts can reveal patterns, but they do not automatically prove
that one variable causes another.

Exercise:
Choose a chart to compare marks across subjects and explain why.
""",
            "code": """import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
scores = [85, 92, 78]

plt.bar(subjects, scores)
plt.title("Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.show()""",
            "quiz": [
                {
                    "question": "Which chart is useful for comparing categories?",
                    "options": ["Scatter plot only", "Bar chart", "Histogram only", "Map only"],
                    "answer": 1
                },
                {
                    "question": "Which chart commonly shows trends over time?",
                    "options": ["Pie chart only", "Single number", "Line chart", "Word cloud only"],
                    "answer": 2
                },
                {
                    "question": "Which chart shows the distribution of numerical data?",
                    "options": ["Histogram", "Logo", "Flowchart", "Network diagram only"],
                    "answer": 0
                },
                {
                    "question": "What does a scatter plot help examine?",
                    "options": [
                        "Only category names",
                        "Only spelling",
                        "Only database structure",
                        "The relationship between two numerical variables"
                    ],
                    "answer": 3
                },
                {
                    "question": "Do charts alone prove causation?",
                    "options": [
                        "No, additional evidence and analysis are needed",
                        "Yes, always",
                        "Only bar charts do",
                        "Only colorful charts do"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 7,
            "title": "Statistics and Probability",
            "content": """
Statistics summarizes data and helps us draw conclusions.

Population means the full group of interest.
A sample is a subset of that population.

Variance describes spread around the mean.
Standard deviation is the square root of variance.
Probability measures how likely an event is, on a scale from
0 to 1.

A probability of 0 means impossible under the model.
A probability of 1 means certain under the model.

Sampling methods and sample size affect how well a sample
represents a population.

Exercise:
Calculate the average of a small dataset and explain what it tells
you and what it does not tell you.
""",
            "code": """import statistics

values = [4, 6, 6, 8, 10]

print("Mean:", statistics.mean(values))
print("Median:", statistics.median(values))
print("Population variance:",
      statistics.pvariance(values))
print("Population standard deviation:",
      statistics.pstdev(values))""",
            "quiz": [
                {
                    "question": "What is a sample?",
                    "options": [
                        "The entire population in every case",
                        "A subset of a population",
                        "A chart title",
                        "A programming statement"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does standard deviation describe?",
                    "options": [
                        "The dataset's file name",
                        "The number of columns only",
                        "The spread of values around the mean",
                        "The number of charts"
                    ],
                    "answer": 2
                },
                {
                    "question": "What is the usual range of probability?",
                    "options": ["0 to 1", "1 to 100 only", "-10 to -1", "10 to 1000"],
                    "answer": 0
                },
                {
                    "question": "What does a probability of 1 mean?",
                    "options": [
                        "Impossible",
                        "Unknown in every model",
                        "A negative event",
                        "Certain under the model"
                    ],
                    "answer": 3
                },
                {
                    "question": "Why is representative sampling important?",
                    "options": [
                        "It helps conclusions apply to the population of interest",
                        "It guarantees every prediction is correct",
                        "It removes the need for analysis",
                        "It makes all values equal"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 8,
            "title": "Introduction to Machine Learning",
            "content": """
Machine Learning (ML) uses data to learn patterns that can support
predictions or decisions.

Common types:
- Supervised learning uses labeled examples.
- Unsupervised learning looks for structure in unlabeled data.
- Reinforcement learning learns through interactions and rewards.

In supervised learning:
- Features are the input variables.
- A target is the value the model tries to predict.
- Training data is used to fit the model.

Examples include predicting house prices and classifying emails.

A model's usefulness depends on data quality, evaluation, and the
problem it is designed to solve.

Exercise:
Describe a prediction problem and identify its features and target.
""",
            "code": """# A simple supervised learning example
from sklearn.tree import DecisionTreeClassifier

# Features: study hours
X = [[1], [2], [3], [4], [5], [6]]

# Labels: example pass/fail outcomes
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[5]])
print("Predicted class:", prediction[0])""",
            "quiz": [
                {
                    "question": "What does machine learning try to do?",
                    "options": [
                        "Learn patterns from data",
                        "Replace all databases",
                        "Guarantee every outcome",
                        "Remove the need for evaluation"
                    ],
                    "answer": 0
                },
                {
                    "question": "What kind of data does supervised learning use?",
                    "options": [
                        "Only unlabeled images",
                        "Labeled examples",
                        "No data",
                        "Only file names"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is a feature?",
                    "options": [
                        "A model error message",
                        "A chart title",
                        "An input variable used by a model",
                        "The computer's wallpaper"
                    ],
                    "answer": 2
                },
                {
                    "question": "What is a target in supervised learning?",
                    "options": [
                        "The programming editor",
                        "The dataset's file size",
                        "A random feature name",
                        "The value the model is trained to predict"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which is an example of machine learning?",
                    "options": [
                        "Classifying emails as spam or not spam",
                        "Manually changing a font",
                        "Renaming a folder",
                        "Turning on a monitor"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 9,
            "title": "Training, Testing, and Model Evaluation",
            "content": """
A model should be evaluated on data that was not used to train it.

A common workflow separates data into:
- Training set: fits the model.
- Validation set: helps select settings or compare models.
- Test set: provides a final evaluation.

Overfitting happens when a model learns training-specific details
that do not generalize well to new data.

For classification, common metrics include accuracy, precision,
recall, and F1 score.

Accuracy is the fraction of predictions that are correct.
Precision measures the proportion of predicted positives that are
actually positive.
Recall measures the proportion of actual positives identified.

Exercise:
Explain why testing a model only on its training data can be
misleading.
""",
            "code": """from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))""",
            "quiz": [
                {
                    "question": "Why keep a test set separate from training data?",
                    "options": [
                        "To evaluate performance on unseen examples",
                        "To increase the number of labels",
                        "To remove all features",
                        "To make every prediction correct"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is overfitting?",
                    "options": [
                        "The model has no parameters",
                        "The model fits training details but generalizes poorly",
                        "The dataset has no rows",
                        "The model never trains"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does accuracy measure?",
                    "options": [
                        "The time to open a file",
                        "The number of features only",
                        "The fraction of predictions that are correct",
                        "The model's file size"
                    ],
                    "answer": 2
                },
                {
                    "question": "What does recall measure?",
                    "options": [
                        "The number of columns",
                        "The speed of a computer",
                        "The fraction of all records that are positive",
                        "The proportion of actual positives identified"
                    ],
                    "answer": 3
                },
                {
                    "question": "What is the purpose of a validation set?",
                    "options": [
                        "To help select model settings and compare models",
                        "To replace all training data",
                        "To guarantee perfect predictions",
                        "To store program comments"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "Data Science Project",
            "content": """
A data science project combines problem-solving, data preparation,
analysis, and communication.

A practical project workflow:
1. Define a clear question.
2. Obtain relevant data responsibly.
3. Check permissions and privacy.
4. Clean and explore the data.
5. Visualize important findings.
6. Apply a suitable statistical or machine learning method.
7. Evaluate results.
8. Communicate conclusions and limitations.

A good project should be reproducible. Record the data source,
important cleaning decisions, software versions, and evaluation
method.

Avoid sharing personal information without permission. Explain
uncertainty and limitations rather than overstating conclusions.

Exercise:
Plan a small project using public or sample data. Write its goal,
data source, analysis steps, and expected output.
""",
            "code": """import pandas as pd
import matplotlib.pyplot as plt

data = {
    "subject": ["Math", "Science", "English", "History"],
    "score": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print("Summary:")
print(df.describe())

plt.bar(df["subject"], df["score"])
plt.title("Sample Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.show()""",
            "quiz": [
                {
                    "question": "What is a useful first step in a data science project?",
                    "options": [
                        "Define the problem",
                        "Build a complicated model immediately",
                        "Delete the data",
                        "Publish results without checking them"
                    ],
                    "answer": 0
                },
                {
                    "question": "Why document a project workflow?",
                    "options": [
                        "To hide the analysis",
                        "To help others understand and reproduce the work",
                        "To make results impossible to check",
                        "To replace data cleaning"
                    ],
                    "answer": 1
                },
                {
                    "question": "Why evaluate a model?",
                    "options": [
                        "To make the charts colorful",
                        "To increase file size",
                        "To understand its performance and limitations",
                        "To remove all data"
                    ],
                    "answer": 2
                },
                {
                    "question": "What should a report explain?",
                    "options": [
                        "Only the project title",
                        "Only the programming language",
                        "Only the number of files",
                        "Findings, methods, and limitations"
                    ],
                    "answer": 3
                },
                {
                    "question": "How should personal data be handled?",
                    "options": [
                        "Respect privacy and use data responsibly",
                        "Publish it without permission",
                        "Ignore access restrictions",
                        "Share every record publicly"
                    ],
                    "answer": 0
                }
            ]
        }
    ]
},
    {
    "id": "devops",
    "name": "DevOps Fundamentals",
    "icon": "⚙️",
    "description": "Learn DevOps, Git, CI/CD, Docker, cloud computing, and automation.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Introduction to DevOps",
            "content": """
DevOps combines Development (Dev) and Operations (Ops).

Its goal is to help teams build, test, release, and maintain software more efficiently.

WHY DEVOPS IS IMPORTANT
- Faster software releases.
- Better teamwork.
- Fewer manual mistakes.
- More reliable applications.
- Faster identification of problems.

DEVELOPMENT AND OPERATIONS
Developers write application code. Operations teams help deploy, monitor, and maintain applications. DevOps encourages these teams to work together.

DEVOPS LIFECYCLE
1. Plan
2. Code
3. Build
4. Test
5. Release
6. Deploy
7. Operate
8. Monitor

EXAMPLE
A team develops a website. Instead of manually uploading every update, it automates testing and deployment so approved changes can be released consistently.

EXERCISE
Write three ways DevOps can improve a software project.
""",
            "code": """# A simple example of an automated quality check

def check_application():
    application_name = "Study Pilot"
    is_ready = True

    if is_ready:
        print(application_name, "is ready for testing.")
    else:
        print(application_name, "needs more work.")

check_application()
""",
            "quiz": [
                {
                    "question": "What does DevOps combine?",
                    "options": [
                        "Development and Operations",
                        "Design and Painting",
                        "Data and Printing",
                        "Documents and Pictures"
                    ],
                    "answer": 0
                },
                {
                    "question": "What is one goal of DevOps?",
                    "options": [
                        "Avoid testing",
                        "Improve software delivery",
                        "Remove teamwork",
                        "Stop monitoring"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which is a DevOps lifecycle activity?",
                    "options": [
                        "Cooking",
                        "Drawing",
                        "Testing",
                        "Typing without saving"
                    ],
                    "answer": 2
                },
                {
                    "question": "Why is monitoring useful?",
                    "options": [
                        "It detects application problems",
                        "It deletes every file",
                        "It prevents collaboration",
                        "It replaces all developers"
                    ],
                    "answer": 0
                },
                {
                    "question": "DevOps encourages which approach?",
                    "options": [
                        "Teams working separately",
                        "No communication",
                        "Manual work only",
                        "Development and operations collaboration"
                    ],
                    "answer": 3
                }
            ]
        },
        {
            "id": 2,
            "title": "Version Control with Git",
            "content": """
Git is a version control system that tracks changes in files.

WHY USE GIT?
- Review previous changes.
- Work with other developers.
- Create separate branches for features.
- Restore earlier versions when needed.

IMPORTANT TERMS
Repository: A project tracked by Git.
Commit: A saved snapshot of changes.
Branch: A separate line of development.
Merge: Combining changes from branches.
Clone: Copying a remote repository to your computer.

COMMON COMMANDS

git init
Creates a Git repository in the current folder.

git status
Shows the state of your files.

git add .
Stages changes for a commit.

git commit -m "Add new feature"
Saves staged changes.

git log
Shows previous commits.

git branch
Lists branches.

git switch -c new-feature
Creates and switches to a new branch.

EXERCISE
Create a test folder, initialize Git, create a file, and inspect its status.
""",
            "code": """# Typical Git workflow (run these in your terminal)

git init
git status
git add .
git commit -m "Initial project commit"
git log
""",
            "quiz": [
                {
                    "question": "What is Git?",
                    "options": [
                        "A database table",
                        "A version control system",
                        "A web browser",
                        "An operating system"
                    ],
                    "answer": 1
                },
                {
                    "question": "Which command checks file status?",
                    "options": [
                        "git status",
                        "git erase",
                        "git paint",
                        "git stop"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does a commit represent?",
                    "options": [
                        "A deleted computer",
                        "A network cable",
                        "A saved snapshot of changes",
                        "A programming language"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which command stages files?",
                    "options": [
                        "git close",
                        "git sleep",
                        "git remove-all",
                        "git add"
                    ],
                    "answer": 3
                },
                {
                    "question": "Why create a branch?",
                    "options": [
                        "To delete Git",
                        "To develop changes separately",
                        "To turn code into hardware",
                        "To remove version history"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 3,
            "title": "GitHub and Remote Repositories",
            "content": """
GitHub is an online platform for hosting Git repositories and collaborating on software.

GIT AND GITHUB
Git tracks changes on your computer. GitHub can store a remote copy of your repository and provide collaboration tools.

IMPORTANT COMMANDS

git clone REPOSITORY_URL
Copies a remote repository to your computer.

git remote -v
Shows configured remote repositories.

git push
Uploads local commits to a remote repository.

git pull
Fetches and integrates changes from a remote repository.

git fetch
Downloads remote updates without integrating them into your current branch.

BASIC WORKFLOW
1. Make changes locally.
2. Review them with git status.
3. Stage and commit the changes.
4. Push the commits to GitHub.

COLLABORATION
Pull requests allow team members to review proposed changes before merging them.

SECURITY
Never upload passwords, secret keys, access tokens, or private credentials to a public repository.

EXERCISE
Open your project repository on GitHub and identify its files and commit history.
""",
            "code": """# Example commands for a repository
# Replace the remote URL with your own repository URL.

git remote -v
git status
git add .
git commit -m "Update documentation"
git push
""",
            "quiz": [
                {
                    "question": "What is GitHub commonly used for?",
                    "options": [
                        "Hosting Git repositories",
                        "Replacing a computer",
                        "Editing physical hardware",
                        "Printing documents only"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which command uploads local commits?",
                    "options": [
                        "git pull",
                        "git push",
                        "git status",
                        "git log"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does git clone do?",
                    "options": [
                        "Deletes a repository",
                        "Changes the programming language",
                        "Copies a repository",
                        "Turns off the internet"
                    ],
                    "answer": 2
                },
                {
                    "question": "What is a pull request used for?",
                    "options": [
                        "Removing all files",
                        "Changing a computer screen",
                        "Creating a password",
                        "Reviewing proposed changes"
                    ],
                    "answer": 3
                },
                {
                    "question": "What should never be committed to a public repository?",
                    "options": [
                        "Secret keys and passwords",
                        "A README file",
                        "Public documentation",
                        "Example source code without secrets"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 4,
            "title": "Linux and Command-Line Basics",
            "content": """
Linux is an operating system widely used on servers and cloud platforms.

A command-line interface lets you interact with a computer by entering commands.

COMMON COMMANDS

pwd
Displays the current directory.

ls
Lists files and directories.

cd folder_name
Changes the current directory.

mkdir project
Creates a directory named project.

touch app.py
Creates an empty file on many Linux systems.

cat app.py
Displays a file's contents.

cp source destination
Copies a file.

mv old_name new_name
Moves or renames a file.

grep "error" app.log
Searches a file for matching text.

IMPORTANT SAFETY
Check your current directory before changing or deleting files. Some commands can permanently remove data.

PATHS
An absolute path begins from the filesystem root. A relative path is interpreted from the current directory.

EXERCISE
Practice pwd, ls, and cd in a test directory.
""",
            "code": """# Linux commands (run in a Linux terminal)

pwd
ls
mkdir devops-practice
cd devops-practice
touch notes.txt
ls
""",
            "quiz": [
                {
                    "question": "Which command displays the current directory?",
                    "options": [
                        "pwd",
                        "mkdir",
                        "touch",
                        "clear-all"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which command lists files?",
                    "options": [
                        "cd",
                        "ls",
                        "pwd",
                        "rename-system"
                    ],
                    "answer": 1
                },
                {
                    "question": "What does mkdir do?",
                    "options": [
                        "Lists network devices",
                        "Displays a file",
                        "Creates a directory",
                        "Starts a browser"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which command changes directories?",
                    "options": [
                        "cat",
                        "grep",
                        "pwd",
                        "cd"
                    ],
                    "answer": 3
                },
                {
                    "question": "What should you do before deleting files?",
                    "options": [
                        "Check the location and intended target",
                        "Ignore the command",
                        "Delete everything",
                        "Turn off version control"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 5,
            "title": "Continuous Integration and Continuous Delivery",
            "content": """
Continuous Integration (CI) automatically builds and tests code changes.

Continuous Delivery means changes are kept ready for release after passing the required checks. Releasing to production may still require approval.

Continuous Deployment automatically releases qualifying changes to production without a separate manual release approval.

TYPICAL PIPELINE
1. A developer pushes code.
2. The pipeline installs dependencies.
3. Automated checks run.
4. Tests execute.
5. The application is packaged.
6. An approved release is deployed.

BENEFITS
- Finds problems earlier.
- Makes releases more consistent.
- Reduces repetitive manual work.
- Provides repeatable checks.

IMPORTANT PRACTICES
Keep tests reliable. Store credentials in protected environment variables or a secrets manager. Avoid deploying when required checks fail.

EXAMPLE
A Python project can run its unit tests whenever a change is pushed to its repository.

EXERCISE
Write the stages you would include in a pipeline for Study Pilot.
""",
            "code": """# A simple test file: test_math.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

# Run with pytest after installing it:
# python -m pip install pytest
# python -m pytest
""",
            "quiz": [
                {
                    "question": "What does CI commonly automate?",
                    "options": [
                        "Building and testing code",
                        "Buying computers",
                        "Writing all requirements",
                        "Removing source control"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does continuous delivery aim to keep software ready for?",
                    "options": [
                        "Permanent deletion",
                        "Release",
                        "Hardware repair",
                        "Manual typing"
                    ],
                    "answer": 1
                },
                {
                    "question": "What usually happens when a required test fails?",
                    "options": [
                        "The failure should be ignored",
                        "All tests should be removed",
                        "The pipeline should report failure",
                        "The repository should be deleted"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which is a benefit of automated tests?",
                    "options": [
                        "They guarantee no bug can ever exist",
                        "They remove the need for reviews",
                        "They eliminate every deployment risk",
                        "They help detect regressions"
                    ],
                    "answer": 3
                },
                {
                    "question": "Where should deployment credentials be stored?",
                    "options": [
                        "In protected secrets or environment settings",
                        "In public source code",
                        "In a public README",
                        "In every commit message"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 6,
            "title": "Docker and Containers",
            "content": """
Docker is a platform for building and running containers.

A container packages an application and its required dependencies so it can run consistently in different environments.

IMPORTANT TERMS
Image: A template used to create containers.
Container: A running instance of an image.
Dockerfile: Instructions for building an image.
Registry: A place to store and distribute images.
Volume: Storage used to keep data outside a container's temporary writable layer.

WHY USE CONTAINERS?
- More consistent environments.
- Easier application packaging.
- Convenient testing and deployment.
- Isolation between application processes.

EXAMPLE DOCKERFILE
A Python application can use a Dockerfile to install requirements and start its application.

BASIC COMMANDS
docker build -t my-app .
Builds an image.

docker images
Lists local images.

docker run my-app
Runs a container from an image.

docker ps
Lists running containers.

docker logs CONTAINER_ID
Shows container logs.

SECURITY
Use trusted base images, avoid embedding secrets in images, and keep dependencies updated.

EXERCISE
Explain the difference between an image and a container.
""",
            "code": """# Example Dockerfile for a small Flask application

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

# Build from the folder containing this file:
# docker build -t study-pilot .
""",
            "quiz": [
                {
                    "question": "What is a Docker image?",
                    "options": [
                        "A database password",
                        "A template used to create containers",
                        "A physical computer",
                        "A Git branch"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is a container?",
                    "options": [
                        "A source-control commit",
                        "A web address",
                        "A running instance of an image",
                        "A spreadsheet"
                    ],
                    "answer": 2
                },
                {
                    "question": "What file defines Docker image build instructions?",
                    "options": [
                        "Dockerfile",
                        "README-only",
                        "requirements.lock-only",
                        "index.photo"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which command lists running containers?",
                    "options": [
                        "docker build",
                        "docker images",
                        "docker create-file",
                        "docker ps"
                    ],
                    "answer": 3
                },
                {
                    "question": "What should not be embedded in a Docker image?",
                    "options": [
                        "Application source code",
                        "Secret credentials",
                        "A non-sensitive configuration example",
                        "A Dockerfile"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 7,
            "title": "Cloud Computing and Deployment",
            "content": """
Cloud computing provides computing resources such as servers, storage, and databases over a network.

COMMON SERVICE MODELS
IaaS: Infrastructure as a Service. You manage much of the operating system and application stack.
PaaS: Platform as a Service. The provider manages more of the underlying platform.
SaaS: Software as a Service. Users access a complete software application.

DEPLOYMENT STEPS
1. Prepare application code.
2. Install dependencies.
3. Configure environment variables.
4. Connect a suitable database.
5. Configure the start command.
6. Deploy the application.
7. Review logs and test the live site.

ENVIRONMENT VARIABLES
They provide configuration without hardcoding values in source files.

DATABASE CONSIDERATIONS
A database stored only on a temporary local filesystem may lose data when a hosted service restarts or replaces the instance. Use a supported persistent database or persistent disk when required.

EXAMPLE
Study Pilot can be hosted on a platform that installs Python dependencies and starts its Flask application.

EXERCISE
List the configuration items needed to deploy a Flask app.
""",
            "code": """# Example Flask application start command
# Use the command appropriate for your hosting setup.

python main.py

# For production, a WSGI server such as Gunicorn
# is commonly used on supported Python hosts:
# gunicorn main:app
""",
            "quiz": [
                {
                    "question": "What does cloud computing provide?",
                    "options": [
                        "Computing resources over a network",
                        "Only paper documents",
                        "Only offline games",
                        "Physical notebooks"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which model provides a complete application to users?",
                    "options": [
                        "IaaS",
                        "SaaS",
                        "CPU",
                        "HTML"
                    ],
                    "answer": 1
                },
                {
                    "question": "Why use environment variables?",
                    "options": [
                        "To remove the need for configuration",
                        "To make every setting public",
                        "To configure an app outside its source code",
                        "To replace all application code"
                    ],
                    "answer": 2
                },
                {
                    "question": "What should you check after deployment?",
                    "options": [
                        "Only the browser theme",
                        "Only the project name",
                        "Nothing at all",
                        "Logs and application functionality"
                    ],
                    "answer": 3
                },
                {
                    "question": "What can happen to data on a temporary filesystem?",
                    "options": [
                        "It may be lost when the instance is replaced",
                        "It is always permanent",
                        "It is automatically copied to every database",
                        "It cannot be read by the application"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 8,
            "title": "Infrastructure as Code",
            "content": """
Infrastructure as Code (IaC) means defining infrastructure through files or code rather than configuring every resource manually.

WHY USE IaC?
- Repeatable environments.
- Easier reviews of infrastructure changes.
- Consistent configuration.
- Faster recreation of resources.
- Better documentation of infrastructure.

DECLARATIVE APPROACH
You describe the desired final state. A tool works to make the real infrastructure match it.

IMPERATIVE APPROACH
You describe the steps to perform.

TOOLS
Terraform is commonly used to define infrastructure across supported providers.
Ansible is commonly used for configuration management and automation.

IMPORTANT PRACTICES
- Review changes before applying them.
- Protect state files and credentials.
- Avoid committing secrets.
- Use version control.
- Test changes in a safe environment.

EXAMPLE
A team can describe a cloud server, network, and database in configuration files.

EXERCISE
Describe one infrastructure task that could be automated.
""",
            "code": """# Illustrative Terraform-style configuration.
# The provider and resource details must be configured
# for the cloud service you actually use.

terraform {
  required_version = ">= 1.0.0"
}

# A real infrastructure resource would be declared
# here using the appropriate provider.
""",
            "quiz": [
                {
                    "question": "What does IaC stand for?",
                    "options": [
                        "Internet and Computers",
                        "Infrastructure as Code",
                        "Internal Application Connection",
                        "Integrated Access Control"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is a benefit of IaC?",
                    "options": [
                        "No need for reviews",
                        "Guaranteed absence of all errors",
                        "Repeatable infrastructure configuration",
                        "Automatic removal of security risks"
                    ],
                    "answer": 2
                },
                {
                    "question": "Which is an infrastructure automation tool?",
                    "options": [
                        "Terraform",
                        "A text editor alone",
                        "A calculator",
                        "A photo viewer"
                    ],
                    "answer": 0
                },
                {
                    "question": "What should be done before applying infrastructure changes?",
                    "options": [
                        "Publish all secrets",
                        "Delete the configuration",
                        "Ignore the plan",
                        "Review the proposed changes"
                    ],
                    "answer": 3
                },
                {
                    "question": "How should credentials be handled?",
                    "options": [
                        "Commit them publicly",
                        "Store and manage them securely",
                        "Put them in every example",
                        "Share them in commit messages"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "id": 9,
            "title": "Application Monitoring and Logging",
            "content": """
Monitoring helps you understand an application's health and performance over time.

LOGGING
Logs record events such as application startup, warnings, errors, and important operations.

METRICS
Metrics are numerical measurements, such as response time, request count, memory usage, and error rate.

ALERTS
Alerts notify a team when a defined condition occurs, such as an unusually high error rate.

WHAT TO MONITOR
- Application availability.
- Request failures.
- Response times.
- Resource usage.
- Background job failures.
- Database connection problems.

TROUBLESHOOTING
1. Reproduce the problem if possible.
2. Check recent changes.
3. Read relevant logs.
4. Inspect metrics.
5. Identify the cause.
6. Apply a fix and verify it.

SECURITY AND PRIVACY
Do not log passwords, access tokens, or sensitive personal information. Limit access to logs and keep only necessary data.

EXERCISE
Imagine your website returns an error. List three things you would inspect.
""",
            "code": """import logging

logging.basicConfig(level=logging.INFO)

logging.info("Study Pilot application started")
logging.warning("A sample warning was recorded")
logging.error("A sample error was recorded")

# In a real application, record useful context
# without including passwords or secret tokens.
""",
            "quiz": [
                {
                    "question": "What are logs used for?",
                    "options": [
                        "Recording application events",
                        "Replacing all tests",
                        "Storing every password",
                        "Deleting the application"
                    ],
                    "answer": 0
                },
                {
                    "question": "Which is an application metric?",
                    "options": [
                        "A logo",
                        "Response time",
                        "A folder name",
                        "A comment in code"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is an alert designed to do?",
                    "options": [
                        "Hide every error",
                        "Replace the database",
                        "Notify a team about a defined condition",
                        "Delete old code automatically"
                    ],
                    "answer": 2
                },
                {
                    "question": "What should you avoid putting in logs?",
                    "options": [
                        "A non-sensitive status message",
                        "A general error description",
                        "A request duration",
                        "Passwords and secret tokens"
                    ],
                    "answer": 3
                },
                {
                    "question": "What is a sensible first troubleshooting step?",
                    "options": [
                        "Inspect relevant evidence and reproduce the problem",
                        "Delete the entire project",
                        "Ignore all error messages",
                        "Disable every security control"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "DevOps Security and Final Project",
            "content": """
DevSecOps integrates security into the software development and delivery process.

SECURITY PRACTICES
- Keep dependencies updated.
- Review code changes.
- Use automated security checks.
- Protect credentials.
- Apply least-privilege access.
- Back up important data.
- Monitor application activity.
- Respond to vulnerabilities promptly.

LEAST PRIVILEGE
Give each user, service, or application only the permissions needed for its task.

DEPENDENCY SECURITY
Libraries may contain vulnerabilities. Track dependencies, review advisories, and update affected packages carefully.

SECRET MANAGEMENT
Store secret keys and tokens in protected environment settings or a suitable secrets manager. Do not put them in source code.

FINAL PROJECT: STUDY PILOT
Create a small deployment checklist:
1. Store the code in Git.
2. Keep dependencies in requirements.txt.
3. Run tests before release.
4. Configure environment variables.
5. Use a persistent database when required.
6. Deploy to a hosting platform.
7. Test login and key application features.
8. Inspect logs and errors.
9. Review access permissions.
10. Plan backups and updates.

EXERCISE
Write a DevOps checklist for deploying a small Flask application securely.
""",
            "code": """# Example dependency check workflow idea.
# Run these commands in your project's virtual environment.

python -m pip install --upgrade pip
python -m pip check

# Inspect installed packages:
python -m pip list

# Review requirements.txt and update packages
# deliberately after testing compatibility.
""",
            "quiz": [
                {
                    "question": "What does DevSecOps integrate into software delivery?",
                    "options": [
                        "Security practices",
                        "Only graphic design",
                        "Only manual data entry",
                        "Physical construction"
                    ],
                    "answer": 0
                },
                {
                    "question": "What does least privilege mean?",
                    "options": [
                        "Give everyone administrator access",
                        "Give only the permissions needed",
                        "Remove all user accounts",
                        "Share one password with everyone"
                    ],
                    "answer": 1
                },
                {
                    "question": "How should secret keys be stored?",
                    "options": [
                        "In public source code",
                        "In public commit messages",
                        "In protected environment settings or a secrets manager",
                        "In a public issue report"
                    ],
                    "answer": 2
                },
                {
                    "question": "Why review software dependencies?",
                    "options": [
                        "To guarantee the app never needs testing",
                        "To remove version control",
                        "To make every package public",
                        "To identify updates and possible vulnerabilities"
                    ],
                    "answer": 3
                },
                {
                    "question": "Which belongs in a deployment checklist?",
                    "options": [
                        "Test important features after deployment",
                        "Ignore application errors",
                        "Publish secret credentials",
                        "Skip database planning"
                    ],
                    "answer": 0
                }
            ]
        }
    ]
},
    {
    "id": "aptitude",
    "name": "Quantitative Aptitude",
    "icon": "🧮",
    "description": "Improve your mathematical reasoning, calculations, and problem-solving skills.",
    "level": "Beginner",
    "lessons": [
        {
            "id": 1,
            "title": "Number System",
            "content": """
A number system is a way of representing and classifying numbers.

TYPES OF NUMBERS

Natural numbers: 1, 2, 3, 4, ...
Whole numbers: 0, 1, 2, 3, ...
Integers: ..., -2, -1, 0, 1, 2, ...
Rational numbers: Numbers expressible as p/q, where q is not zero.
Irrational numbers: Numbers that cannot be expressed as a ratio of integers, such as sqrt(2).

EVEN AND ODD NUMBERS
Even numbers are divisible by 2.
Odd numbers are not divisible by 2.

PRIME NUMBERS
A prime number has exactly two positive factors: 1 and itself.
Examples: 2, 3, 5, 7, 11.
Remember: 1 is not a prime number.

DIVISIBILITY RULES
Divisible by 2: Last digit is even.
Divisible by 3: Sum of digits is divisible by 3.
Divisible by 5: Last digit is 0 or 5.
Divisible by 10: Last digit is 0.

EXAMPLE
Is 234 divisible by 3?
2 + 3 + 4 = 9. Since 9 is divisible by 3, 234 is divisible by 3.

EXERCISE
Check whether 125 is divisible by 5 and whether 246 is divisible by 3.
""",
            "code": """number = 234

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

digit_sum = sum(int(digit) for digit in str(number))

if digit_sum % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")
""",
            "quiz": [
                {
                    "question": "Which number is prime?",
                    "options": ["9", "11", "15", "21"],
                    "answer": 1
                },
                {
                    "question": "Which is a whole number?",
                    "options": ["-3", "-1", "0", "1.5"],
                    "answer": 2
                },
                {
                    "question": "Which number is divisible by 5?",
                    "options": ["123", "142", "167", "125"],
                    "answer": 3
                },
                {
                    "question": "What is the only even prime number?",
                    "options": ["2", "4", "6", "8"],
                    "answer": 0
                },
                {
                    "question": "Is 246 divisible by 3?",
                    "options": ["No", "Yes", "Only by 2", "Cannot be determined"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 2,
            "title": "Simplification and BODMAS",
            "content": """
Simplification means calculating an expression using the correct order of operations.

BODMAS
B: Brackets
O: Orders, powers, and roots
D: Division
M: Multiplication
A: Addition
S: Subtraction

Division and multiplication have equal priority. Work from left to right.
Addition and subtraction also have equal priority. Work from left to right.

EXAMPLE 1
Calculate: 8 + 4 × 3
First multiply: 4 × 3 = 12.
Then add: 8 + 12 = 20.

EXAMPLE 2
Calculate: (8 + 4) × 3
First calculate the brackets: 8 + 4 = 12.
Then multiply: 12 × 3 = 36.

EXAMPLE 3
Calculate: 20 ÷ 5 × 2
Work from left to right:
20 ÷ 5 = 4.
4 × 2 = 8.

COMMON MISTAKE
Do not automatically perform multiplication before division or addition before subtraction when the operations have equal priority.

EXERCISE
Calculate:
1. 5 + 3 × 4
2. (5 + 3) × 4
3. 18 ÷ 3 × 2
""",
            "code": """# Simplification examples in Python

print(8 + 4 * 3)       # 20
print((8 + 4) * 3)     # 36
print(20 / 5 * 2)      # 8.0
print(2 ** 3 + 4)      # 12
""",
            "quiz": [
                {
                    "question": "What is 8 + 4 × 3?",
                    "options": ["36", "20", "24", "12"],
                    "answer": 1
                },
                {
                    "question": "What is (8 + 4) × 3?",
                    "options": ["20", "24", "30", "36"],
                    "answer": 3
                },
                {
                    "question": "What is 18 ÷ 3 × 2?",
                    "options": ["12", "3", "9", "6"],
                    "answer": 0
                },
                {
                    "question": "Which operation is performed first in 2 + 3²?",
                    "options": ["Addition", "Subtraction", "Exponentiation", "Division"],
                    "answer": 2
                },
                {
                    "question": "What is 20 - 8 + 2?",
                    "options": ["10", "14", "18", "6"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 3,
            "title": "Fractions and Decimals",
            "content": """
A fraction represents part of a whole.

A fraction has a numerator and denominator.
Example: In 3/4, 3 is the numerator and 4 is the denominator.

PROPER FRACTION
The numerator is smaller than the denominator.
Example: 2/5.

IMPROPER FRACTION
The numerator is greater than or equal to the denominator.
Example: 7/4.

EQUIVALENT FRACTIONS
Fractions such as 1/2 and 2/4 have the same value.

ADDING FRACTIONS
For fractions with the same denominator, add the numerators.
Example: 2/7 + 3/7 = 5/7.

For different denominators, first find a common denominator.
Example: 1/2 + 1/3 = 3/6 + 2/6 = 5/6.

MULTIPLICATION
Multiply numerators together and denominators together.
Example: 2/3 × 3/4 = 6/12 = 1/2.

DECIMALS
A decimal represents a number using a decimal point.
Examples: 0.5 = 1/2 and 0.25 = 1/4.

EXERCISE
Calculate 1/4 + 1/2 and convert 0.75 into a fraction.
""",
            "code": """from fractions import Fraction

a = Fraction(1, 2)
b = Fraction(1, 3)

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Decimal:", float(a))
""",
            "quiz": [
                {
                    "question": "What is 1/2 + 1/4?",
                    "options": ["2/6", "3/4", "1/8", "1/4"],
                    "answer": 1
                },
                {
                    "question": "What is 2/3 × 3/4?",
                    "options": ["5/7", "6/7", "1/2", "3/4"],
                    "answer": 2
                },
                {
                    "question": "What is 0.5 as a fraction in simplest form?",
                    "options": ["1/2", "1/5", "5/1", "2/5"],
                    "answer": 0
                },
                {
                    "question": "Which fraction is equivalent to 1/2?",
                    "options": ["1/3", "2/5", "3/5", "2/4"],
                    "answer": 3
                },
                {
                    "question": "What is 3/8 + 2/8?",
                    "options": ["5/16", "5/8", "1/8", "6/8"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 4,
            "title": "Ratio and Proportion",
            "content": """
A ratio compares two quantities.

Example:
If there are 2 red balls and 3 blue balls, the ratio of red to blue is 2:3.

SIMPLIFYING RATIOS
Divide both terms by their greatest common factor.
Example: 12:18 = 2:3.

PROPORTION
Two ratios are proportional when they are equal.
Example: 2:3 = 4:6.

CROSS MULTIPLICATION
If a/b = c/d, then a × d = b × c, provided the denominators are nonzero.

EXAMPLE
Find x if 2/3 = x/12.
Cross multiply:
3x = 24.
x = 8.

DIVIDING AN AMOUNT IN A RATIO
Divide ₹600 in the ratio 2:3.
Total parts = 2 + 3 = 5.
One part = 600 ÷ 5 = ₹120.
First share = 2 × 120 = ₹240.
Second share = 3 × 120 = ₹360.

EXERCISE
Divide ₹800 in the ratio 3:5.
""",
            "code": """from math import gcd

a, b = 12, 18
factor = gcd(a, b)

print("Simplified ratio:", a // factor, ":", b // factor)

amount = 600
first_parts = 2
second_parts = 3
total_parts = first_parts + second_parts

print("First share:", amount * first_parts / total_parts)
print("Second share:", amount * second_parts / total_parts)
""",
            "quiz": [
                {
                    "question": "What is the simplified form of 12:18?",
                    "options": ["3:4", "2:3", "4:5", "6:9"],
                    "answer": 1
                },
                {
                    "question": "If 2/3 = x/12, what is x?",
                    "options": ["6", "4", "8", "9"],
                    "answer": 2
                },
                {
                    "question": "Divide 100 in the ratio 2:3. What is the first share?",
                    "options": ["40", "50", "30", "60"],
                    "answer": 0
                },
                {
                    "question": "What is the total number of parts in the ratio 4:7?",
                    "options": ["3", "7", "28", "11"],
                    "answer": 3
                },
                {
                    "question": "Which ratio is equivalent to 3:4?",
                    "options": ["6:10", "6:8", "9:16", "12:9"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 5,
            "title": "Percentages",
            "content": """
A percentage expresses a quantity out of 100.

FORMULA
Percentage = (Part / Whole) × 100

EXAMPLE 1
What percentage is 25 out of 100?
(25 / 100) × 100 = 25%.

EXAMPLE 2
Find 20% of 300.
20/100 × 300 = 60.

CONVERTING FRACTIONS TO PERCENTAGES
Multiply the fraction by 100%.
Example: 3/4 × 100% = 75%.

PERCENTAGE INCREASE
Increase from 200 to 250:
Increase = 250 - 200 = 50.
Percentage increase = (50 / 200) × 100 = 25%.

PERCENTAGE DECREASE
Decrease from 200 to 150:
Decrease = 50.
Percentage decrease = (50 / 200) × 100 = 25%.

IMPORTANT
The original value is used as the denominator when calculating percentage change.

EXERCISE
Find 15% of 400 and calculate the percentage increase from 80 to 100.
""",
            "code": """def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole must not be zero")
    return part / whole * 100

print("Percentage:", percentage(25, 100))
print("20% of 300:", 20 / 100 * 300)

old_value = 80
new_value = 100
increase = new_value - old_value

print("Increase percentage:", increase / old_value * 100)
""",
            "quiz": [
                {
                    "question": "What is 20% of 300?",
                    "options": ["30", "50", "60", "80"],
                    "answer": 2
                },
                {
                    "question": "What is 3/4 as a percentage?",
                    "options": ["75%", "25%", "50%", "80%"],
                    "answer": 0
                },
                {
                    "question": "What is 10% of 500?",
                    "options": ["5", "50", "100", "25"],
                    "answer": 1
                },
                {
                    "question": "A value rises from 100 to 120. What is the percentage increase?",
                    "options": ["10%", "15%", "25%", "20%"],
                    "answer": 3
                },
                {
                    "question": "What is 25% of 80?",
                    "options": ["10", "20", "25", "40"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 6,
            "title": "Profit, Loss, and Discount",
            "content": """
These concepts are frequently used in shopping and business calculations.

COST PRICE (CP)
The price paid to purchase an item.

SELLING PRICE (SP)
The price received when an item is sold.

PROFIT
Profit = Selling Price - Cost Price

LOSS
Loss = Cost Price - Selling Price

PROFIT PERCENTAGE
Profit % = (Profit / Cost Price) × 100

LOSS PERCENTAGE
Loss % = (Loss / Cost Price) × 100

EXAMPLE
An item costs ₹500 and is sold for ₹600.
Profit = 600 - 500 = ₹100.
Profit percentage = 100/500 × 100 = 20%.

DISCOUNT
Discount = Marked Price - Selling Price.

Discount percentage = (Discount / Marked Price) × 100.

EXAMPLE
Marked price = ₹1,000.
Discount = 10%.
Discount amount = ₹100.
Selling price after discount = ₹900.

EXERCISE
An item costs ₹800 and sells for ₹720. Calculate the loss and loss percentage.
""",
            "code": """cost_price = 500
selling_price = 600

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
    print("Profit percentage:", profit / cost_price * 100)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
    print("Loss percentage:", loss / cost_price * 100)
else:
    print("No profit and no loss")
""",
            "quiz": [
                {
                    "question": "An item costs ₹500 and sells for ₹600. What is the profit?",
                    "options": ["₹50", "₹100", "₹150", "₹200"],
                    "answer": 1
                },
                {
                    "question": "Profit percentage is calculated using which denominator?",
                    "options": ["Selling price only", "Discount", "Cost price", "Profit"],
                    "answer": 2
                },
                {
                    "question": "A ₹1,000 item has a 10% discount. What is the discount amount?",
                    "options": ["₹100", "₹10", "₹200", "₹900"],
                    "answer": 0
                },
                {
                    "question": "An item costs ₹800 and sells for ₹720. What is the loss?",
                    "options": ["₹20", "₹40", "₹100", "₹80"],
                    "answer": 3
                },
                {
                    "question": "If cost price equals selling price, what happens?",
                    "options": ["Profit of 100%", "No profit and no loss", "Loss of 50%", "Discount of 100%"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 7,
            "title": "Simple and Compound Interest",
            "content": """
Interest is the amount paid or earned for using money over time.

PRINCIPAL (P)
The initial amount of money.

RATE (R)
The annual interest rate, usually expressed as a percentage.

TIME (T)
The period for which interest is calculated.

SIMPLE INTEREST
SI = (P × R × T) / 100

EXAMPLE
P = ₹1,000, R = 5% per year, T = 2 years.
SI = (1000 × 5 × 2) / 100 = ₹100.
Total amount = ₹1,100.

COMPOUND INTEREST
Compound interest adds earned interest to the principal for later periods.

For annual compounding:
A = P(1 + R/100)^T
CI = A - P

EXAMPLE
P = ₹1,000, R = 10%, T = 2 years.
A = 1000 × 1.1 × 1.1 = ₹1,210.
CI = ₹210.

KEY DIFFERENCE
Simple interest is calculated on the original principal. Compound interest is calculated on the accumulated amount, according to the compounding schedule.

EXERCISE
Calculate simple interest on ₹2,000 at 5% per year for 3 years.
""",
            "code": """principal = 1000
rate = 5
time = 2

simple_interest = principal * rate * time / 100
print("Simple interest:", simple_interest)
print("Total amount:", principal + simple_interest)

annual_rate = 0.10
years = 2
compound_amount = principal * (1 + annual_rate) ** years

print("Compound amount:", compound_amount)
print("Compound interest:", compound_amount - principal)
""",
            "quiz": [
                {
                    "question": "What is the formula for simple interest?",
                    "options": ["P + R + T", "(P × R × T) / 100", "P × T", "R / P"],
                    "answer": 1
                },
                {
                    "question": "Find SI on ₹1,000 at 5% for 2 years.",
                    "options": ["₹50", "₹200", "₹100", "₹150"],
                    "answer": 2
                },
                {
                    "question": "What is the total amount after earning ₹100 interest on ₹1,000?",
                    "options": ["₹1,100", "₹1,000", "₹900", "₹1,200"],
                    "answer": 0
                },
                {
                    "question": "Compound interest is based on what?",
                    "options": ["Only the interest rate", "Only the time", "Only the original interest", "The accumulated amount under the compounding schedule"],
                    "answer": 3
                },
                {
                    "question": "What is the compound amount on ₹1,000 at 10% annually for 2 years?",
                    "options": ["₹1,200", "₹1,210", "₹1,100", "₹1,020"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 8,
            "title": "Time and Work",
            "content": """
Time and work problems describe how quickly people or machines complete a job.

WORK RATE
If a person completes a job in 5 days, their rate is 1/5 of the job per day, assuming a constant rate.

COMBINED WORK
If A completes a job in 4 days and B completes it in 6 days:
A's rate = 1/4 job per day.
B's rate = 1/6 job per day.

Combined rate = 1/4 + 1/6 = 5/12 job per day.

Time together = 1 ÷ (5/12) = 12/5 = 2.4 days.

FORMULA
Combined rate = Sum of individual rates.
Time required = Total work / Combined rate.

ASSUMPTIONS
These calculations assume that work rates stay constant and that the workers can work together without interfering with each other.

EXAMPLE
If a machine completes a job in 8 hours, it completes 1/8 of the job per hour.

EXERCISE
A completes a job in 3 days and B in 6 days. How long will they take together?
""",
            "code": """from fractions import Fraction

a_days = 4
b_days = 6

a_rate = Fraction(1, a_days)
b_rate = Fraction(1, b_days)

combined_rate = a_rate + b_rate
time_together = 1 / combined_rate

print("Combined work rate:", combined_rate)
print("Time together:", time_together, "days")
""",
            "quiz": [
                {
                    "question": "If A completes work in 5 days, what is A's daily work rate?",
                    "options": ["5", "1/5", "1/2", "1/10"],
                    "answer": 1
                },
                {
                    "question": "A finishes in 4 days and B in 4 days. How long together?",
                    "options": ["8 days", "4 days", "2 days", "1 day"],
                    "answer": 2
                },
                {
                    "question": "A's rate is 1/3 and B's rate is 1/6 job per day. What is their combined rate?",
                    "options": ["1/2 job per day", "1/9 job per day", "1/3 job per day", "1/6 job per day"],
                    "answer": 0
                },
                {
                    "question": "What assumption is commonly made in basic time-and-work problems?",
                    "options": ["Work rate always doubles", "Work is never completed", "Time is irrelevant", "Work rates remain constant"],
                    "answer": 3
                },
                {
                    "question": "A completes a job in 3 days and B in 6 days. How long together?",
                    "options": ["3 days", "2 days", "6 days", "9 days"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 9,
            "title": "Time, Speed, and Distance",
            "content": """
These problems connect distance travelled, travel time, and speed.

FORMULAS
Speed = Distance / Time
Distance = Speed × Time
Time = Distance / Speed

UNITS
If distance is in kilometres and time in hours, speed is in km/h.
If distance is in metres and time in seconds, speed is in m/s.

CONVERSION
1 km/h = 5/18 m/s.
1 m/s = 18/5 km/h.

EXAMPLE 1
A vehicle travels 120 km in 3 hours.
Speed = 120 / 3 = 40 km/h.

EXAMPLE 2
A person travels at 60 km/h for 2 hours.
Distance = 60 × 2 = 120 km.

AVERAGE SPEED
Average speed = Total distance / Total time.
Do not simply average two speeds unless the situation makes that valid.

EXERCISE
A car travels 150 km in 3 hours. Find its average speed.
""",
            "code": """distance = 120
time = 3

speed = distance / time
print("Speed:", speed, "km/h")

speed_kmh = 36
speed_ms = speed_kmh * 5 / 18
print("Speed in m/s:", speed_ms)

# Convert 10 m/s to km/h
print("10 m/s in km/h:", 10 * 18 / 5)
""",
            "quiz": [
                {
                    "question": "What is the formula for speed?",
                    "options": ["Distance × Time", "Distance / Time", "Time / Distance", "Distance + Time"],
                    "answer": 1
                },
                {
                    "question": "A car travels 120 km in 3 hours. What is its average speed?",
                    "options": ["30 km/h", "60 km/h", "40 km/h", "90 km/h"],
                    "answer": 2
                },
                {
                    "question": "How far does a vehicle travel at 50 km/h for 2 hours?",
                    "options": ["100 km", "25 km", "52 km", "150 km"],
                    "answer": 0
                },
                {
                    "question": "How many metres per second is 18 km/h?",
                    "options": ["18 m/s", "10 m/s", "15 m/s", "5 m/s"],
                    "answer": 3
                },
                {
                    "question": "How is average speed calculated?",
                    "options": ["Total time / Total distance", "Total distance / Total time", "Speed × Time × Distance", "Distance - Time"],
                    "answer": 1
                }
            ]
        },
        {
            "id": 10,
            "title": "Averages and Data Interpretation",
            "content": """
An average summarizes a set of numbers.

ARITHMETIC MEAN
Average = Sum of all values / Number of values.

EXAMPLE
Find the average of 10, 20, and 30.
Sum = 60.
Number of values = 3.
Average = 60 / 3 = 20.

FINDING A MISSING VALUE
The average of 4 numbers is 15.
Their total must be 4 × 15 = 60.
If three numbers total 45, the missing number is 60 - 45 = 15.

DATA INTERPRETATION
Data interpretation means understanding information shown in tables, charts, and graphs.

COMMON CHARTS
Bar chart: Compares categories.
Line chart: Shows changes over time.
Pie chart: Shows proportions of a whole.
Table: Organizes values into rows and columns.

PERCENTAGE FROM DATA
If 40 students out of 100 prefer Python:
Percentage = 40/100 × 100 = 40%.

EXERCISE
Find the average of 12, 18, 20, and 30. If 25 out of 50 students choose Java, what percentage is that?
""",
            "code": """numbers = [10, 20, 30]

average = sum(numbers) / len(numbers)
print("Average:", average)

students = 50
java_students = 25

percentage = java_students / students * 100
print("Students choosing Java:", percentage, "%")

# Find a missing value from a known average
known_values = [10, 15, 20]
required_average = 15
total_required = required_average * 4
missing_value = total_required - sum(known_values)

print("Missing value:", missing_value)
""",
            "quiz": [
                {
                    "question": "What is the average of 10, 20, and 30?",
                    "options": ["10", "15", "20", "30"],
                    "answer": 2
                },
                {
                    "question": "The average of 4 numbers is 15. What is their total?",
                    "options": ["60", "45", "15", "30"],
                    "answer": 0
                },
                {
                    "question": "25 out of 50 students choose Java. What percentage is that?",
                    "options": ["25%", "50%", "75%", "40%"],
                    "answer": 1
                },
                {
                    "question": "Which chart is commonly used to show changes over time?",
                    "options": ["A folder", "A text file", "A password list", "A line chart"],
                    "answer": 3
                },
                {
                    "question": "What is the average of 12, 18, 20, and 30?",
                    "options": ["18", "20", "22", "25"],
                    "answer": 1
                }
            ]
        }
    ]
},
]