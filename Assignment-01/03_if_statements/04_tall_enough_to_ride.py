def main():
    while True:
        #input height 
        height = input("How tall are you? ")

        if height == "":
            print("Exiting the program. Have a great day!")
            break

        # convert input to number
        height = int(height)

        #Check Height 
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()