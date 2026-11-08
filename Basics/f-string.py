# Formatted string literal


"""

Concepts:

1. Literal:

A literal is any value which is entered into the code space in the IDE.

EX:

  3.14 - float literal

  "hello" - string literal

   3 - int literal

2. String Literal:

Any value which is enclosed in a bracket, "", ''.

3. Formatted String Literal:

A formatted sting literal is an argument which directly lets the coder to
edit the string literal by placing a {}, inside of the string literal.




"""

name = "abhiram"

print("My name is " + name)

print(f"My name is {name}") # Example of a string literal


"""

Adding commas using the f-string:-



"""

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

z = round(x+y)

print(f"The sum of the numbers is: {z:,}")  # Auto comma placed




