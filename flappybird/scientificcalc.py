"""A simple scientific calculator"""
import math
from typing import Tuple, Union

import typer

cli = typer.Typer()

def add(x, y):
    "Adds the given numbers"
    return x + y


def subtract(x, y):
    "Performs Subtraction with the given numbers"
    return x - y


def multiply(x, y):
    "Performs Multiplication with the given numbers"
    return x * y


def divide(x, y):
    "Performs division with the given numbers"
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y


def square(x):
    "Calculates the square of a number"
    return x ** 2


def square_root(x):
    "Calculates the square root of a number"
    if x < 0:
        return "Cannot calculate square root of a negative number!"
    else:
        return math.sqrt(x)


def exponentiate(x, y):
    "Calculates the exponent of a number"
    return x ** y


@cli.command()
def calculate_quadratic_equation_roots(
    a: float, b: float, c: float
) -> Tuple[Union[float, complex], Union[float, complex]]:
    """Calculate the roots of a quadratic equation."""
    # Use the source code example on page 21 of the
    # "Doing Math with Python" to implement this function.
    D = (b * b - 4 * a * c) ** 0.5
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    return x_one, x_two


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")
print("7. Exponentiate")
print("8. Calculate Quadratics")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        if choice != '5' and choice != '6':
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square(num1))
        elif choice == '6':
            print("Result:", square_root(num1))
        elif choice == '7':
            print("Result:", exponentiate(num1, num2))
    elif choice == '8':
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        roots = calculate_quadratic_equation_roots(a, b, c)
        print("Roots:", roots)
    else:
        print("Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
