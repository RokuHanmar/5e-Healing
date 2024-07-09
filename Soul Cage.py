# Import libraries
import random

# Define dice functions
def d8():
    d8 = random.randint(1,8)
    return d8

# Define external modifiers - CHANGE AS NECESSARY
domain = "Life"

# Define spell variables
total = 0
level = 6
remainingUses = 6

# Soul Cage can be used to heal 6 times
while remainingUses >= 1:
    
# Roll and output dice, then add to a running total    
    total = 0
    for i in range (2):
        roll = d8()
        print(roll, end=" ")
        total += roll

    # Calculate and output final total
    if domain == "Life":
        lifeBonus = 2 + level
    else:
        lifeBonus = 0

    print("\n")
    print("Total: " + str(total))
    print("Domain Bonus: " + str(lifeBonus))
    total += lifeBonus
    print("Grand total: " + str(total))
    print("Don't forget to roll the d4")

    # Check if Soul Cage can be used again
    remainingUses -= 1
    print("Remaining Uses: " + str(remainingUses))
    if remainingUses <= 0:
        print("No more uses")
        break
    else:
        reuse = False
        if input("Use again? y/n ").lower() == "n":
            break
