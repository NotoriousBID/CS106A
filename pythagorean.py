"""
File: pythagorean.py
--------------------
This program finds the 'c' value in a triangle using the pythaorean theorem
"""

import math #math library needed for math.sqrt() function

def pythagorean_theorean (a, b):
    c = math.sqrt(((a ** 2) + (b ** 2)))  # use equation to find value of c
    print("c = " + str(c) + "!") #return value of c in the form of a string

def main():
    print("Enter Values to compute the Pythagorean Theorem")
    a = float(input("a: ")) #take the first user input and convert it to a float number
    b = float(input("b: ")) #take the second user input and convert it to a float number
    pythagorean_theorean (a, b)

if __name__ == '__main__':
    main()
