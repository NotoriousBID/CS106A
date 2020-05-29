"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    x = 10 # setting up the number to be counted down
    for i in range(x): # for loop will run for 10 iterations
        print(x) # as the iterations count down it will print out the updated x variable
        x -= 1 # with each new run through the loop it will subtract 1 and update the new x variable
    print("Liftoff!") # once it exits the loop it will print the lift off string

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
