"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

def print_welcome():
    print("Welcome to my mini subtraction calculator! This problem subtracts 2 numbers you give me")

def subtract_num():
    num1 = int(input("Give me the first number to subtract:"))
    num2 = int(input("Awesome! Gimme another one:"))  # take in the second number to store in variable
    total = num1 - num2  # subtract the two values in int form
    print("The total is: " + str(total) + ".")  # returns the result in the form of a string


def main():
    print_welcome()
    subtract_num()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
