"""
File: khansole_academy.py
-------------------------
This program can be used to test the user's capability of adding 2 digit numbers. 
They will continue to receive addition problems until they can answer 3 correct in a row. 
"""

import random


def main():
    """
   generate 2 random numbers to add
   get input as addition answer
   check if correct, if right countdown to get 3 in a row right to end program
   if wrong lets keep adding and restart the 3 in a row count down
    """
    min_random = 10 #keeping constant for the min random number range
    max_random = 99 #keeping constant for the max random number range
    count = 0 #creating a counter variable to keep track of user's answers in a row


    while count != 3: #this loop will keep goin until user get 3 answers correct in a row
        num1 = random.randint(min_random, max_random) #generating a random number each new equations
        num2 = random.randint(min_random, max_random)

        print("What is " + str(num1) + "+" + str(num2) + "?")
        user_input = int(input("Your answer is: ")) #takign the user's input and converting it into an integer

        total = num1 + num2 #keeping track of the actual answer to compare with the user's response
"""
This if/else statement will keep track of how many equations the user gives the correct answer to. 
If the user gets a correct answer they will keeping adding to the counter until they get 3 answers correct in a row. 
Once the counter reaches three it will break out of this loop. 
Else if the user's answer is wrong it will restart the counter to 0 and continue to ask the addition questions. 
"""
        if (user_input == total) :
            count += 1
            print("Congrats you got " + str(count) + " right so far!")
        else:
            print("The correct answer is " + str(total))
            count = 0

    print("You mastered addition!") #Once the loop breaks the user will get a message that they mastered addition.




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
