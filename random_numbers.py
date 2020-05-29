"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""
import random

def main():
    num_random = 10
    min_random = 0
    max_random = 100
    for i in range(num_random):
        print(random.randint(min_random, max_random))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
