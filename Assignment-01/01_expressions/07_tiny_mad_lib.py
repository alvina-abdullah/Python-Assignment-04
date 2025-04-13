# Sentence beginning
Sentence: str = "I am learned to program and used Python to make my "

def main():
    # Get the three inputs from the user
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    print(Sentence + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()