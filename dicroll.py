import random
import time
import os

def roll_dice():
    seed_value = int(time.time() * 1000) + os.getpid()
    random.seed(seed_value)
    dice_roll = random.randint(1, 6)
    return dice_roll

if __name__ == "__main__":
    print("Rolling the dice... You got:", roll_dice())
