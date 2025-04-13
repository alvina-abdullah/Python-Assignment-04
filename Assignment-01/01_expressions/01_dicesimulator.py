import random

DICE_NUM_SIDES = 6

def roll_dice():

    dice1: int = random.randint(1, DICE_NUM_SIDES)
    dice2: int = random.randint(1, DICE_NUM_SIDES)
    total: int = dice1 + dice2
    print(f"Total of two dice : {total}")

def main():
    roll_dice()
    roll_dice()
    roll_dice()

# to call the main() function.
if __name__ == '__main__':
    main()


    