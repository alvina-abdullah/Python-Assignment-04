import math

def main():
    print(""" 
          
          AC = Hyp 
          BC = Base
          AB = Perp 

            """)

    AB: float = float(input("Enter the length of AB:"))
    AC: float = float(input("Enter the length of AC:"))
    BC: float = math.sqrt(AB ** 2 + AC ** 2)
    print(f"The Lenght of BC (the Hyp) is:" + str(BC))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()