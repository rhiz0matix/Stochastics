# A script that simulates playing Wheel of Fortune.
# Requires Python3

import random
import sys

total = 0
rd = 0

def simulate():
    spin = random.randrange(12)
    global total
    global rd
    rd += 1

    if spin == 0:
        total = 0
        print("Bankrupt on round {}!".format(rd))
        return False
    else:
        total += 100 * spin
        return True

while True:
    print("Your current winnings are:", total, "after", rd, "rounds.")
    print("Would you like to keep playing?")

    choice = sys.stdin.readline()
    if choice == "y\n":
        if not simulate():
            break
    else:
        break

