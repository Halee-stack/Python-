# A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we write it once in a function and call it whenever we need it.
# There we can also pass information (called parameters) to a function.
# You can make a function return a value:
# Whereas Input()function lets the user type something using the keyboard. It always returns the user's input as a string.
# Function (def): A named block of code that performs a task and can be reused.
# input(): Reads input from the user as a string.
# Use int(input(...)) or float(input(...)) when you want numeric input instead of text.
# When you store the result of input() in a variable, the variable holds the user's input.
# Variable = a container that stores a value.
# Function = a piece of code that does something, like getting input, printing output, or performing a calculation.


def greet():
    print("Hello")
    print(input("How are you?"))
    print("Isn't the weather nice?")

greet()

# functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print("Hey there!")
    print(input(f"How are you {name}?"))
greet_with_name("Kate") # write name here to see the result