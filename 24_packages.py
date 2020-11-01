# Task # 1: Create a function called dice and each time we roll t gives randon numbers
# Step 1. Create a class called Dice
# Step 2. Create a function called roll()

import random
from pathlib import Path

path = Path()
for file in path.glob("*.py"):
    print(file)
# glob method is used to find a file in directory


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
