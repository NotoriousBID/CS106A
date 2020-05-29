"""
File: moon_weight.py
--------------------
This program will take in your weight (lbs) and calculate your weight on the moon.
"""


def main():
    weight = int(input("Enter your weight:")) #take in the weight from the reader
    if weight <=0: # if their weight is negative, return this message below
        print("Sorry, there's no way you weight that little")
    else: #otherwises calculate their moon weight
        moon_weight = weight * 0.165
        print("Your moon weight is: " + str(moon_weight)) #give back moon_weight in the form of a string

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
