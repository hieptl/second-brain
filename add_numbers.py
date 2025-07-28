#!/usr/bin/env python3
"""
A simple Python program for adding two numbers.

This program provides functionality to add two numbers with support for
both integer and floating-point numbers.
"""


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of the two numbers
    """
    return a + b


def get_number_input(prompt):
    """
    Get a number input from the user with error handling.
    
    Args:
        prompt (str): Prompt message to display to the user
    
    Returns:
        float: The number entered by the user
    """
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the number addition program."""
    print("Welcome to the Number Addition Program!")
    print("=" * 40)
    
    # Get input from user
    first_number = get_number_input("Enter the first number: ")
    second_number = get_number_input("Enter the second number: ")
    
    # Calculate the sum
    result = add_numbers(first_number, second_number)
    
    # Display the result
    print(f"\nResult: {first_number} + {second_number} = {result}")


if __name__ == "__main__":
    main()