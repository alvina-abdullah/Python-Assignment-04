import random  # Generate Random number 

def main():
    # Choose any one num in 0 to 100
    Your_number = random.randint(0, 100)
    
    print("I am thinking of a number between 0 and 100...")
    
    while True:
        # User input
        guess = int(input("Enter a guess: "))

        # Conditions checkkkk 
        if guess > Your_number:
            print("Your guess is too high")
        elif guess < Your_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {Your_number}")
            break  # if correct answer loop endddddd!

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()