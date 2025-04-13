import random

# Constants
PROMPT = "Type a (Joke):______"
SORRY = "Sorry I only tell jokes"

# List of jokes
JOKES = [
    "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. "
    "A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. "
    "The programmer asks why and Sophia replies: 'because they had eggs'",

    "There are only 10 kinds of people in this world: those who understand binary, and those who don't.",

    "Why did the developer go broke? Because he used up all his cache.",

    "Why do Python programmers wear glasses? Because they can’t C.",

    "Why did the computer get cold? Because it left its Windows open.",

    "Why don’t bachelors like Git? Because they are afraid to commit.",

    "Knock knock. Who’s there? Recursion. Knock knock. Who’s there? Recursion.",

    "What’s a computer’s favorite beatle song? Help!"
]

# Get user input
user_input = input(PROMPT)

# Conditional logic
if user_input == "Joke":
    JOKE = random.choice(JOKES)
    print(JOKE)
else:
    print(SORRY)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()