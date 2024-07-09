# Import libraries
import random
import time

# Define dice functions
def d6():
    d6 = random.randint(1,6)
    return d6

# Define external modifiers - CHANGE AS NECESSARY
domain = "Life"
proficiencyBonus = 4
abilityBonus = 0
remainingUses = proficiencyBonus + abilityBonus
if remainingUses < 2:
    remainingUses = 2


# Define spell variables
total = 0
level = 0

# Verify the spell is being cast at a valid level
while level > 9 or level < 2:
    level = int(input("What level are you casting the spell at? Level must be between 2 and 9 inclusive "))    

# Roll and output dice, then add to a running total
while remainingUses >= 1:
    total = 0
    for i in range (level-1):
        roll = d6()
        print(roll, end=" ")
        total += roll

    # Calculate and output final total
    if domain == "Life":
        lifeBonus = 2 + level
    else:
        lifeBonus = 0

    print("\n")
    print("Total: " + str(total))
    print("Domain bonus: " + str(lifeBonus))
    total += lifeBonus
    print("Grand total: " + str(total))
    print("Don't forget to roll the d4")

    # Subtracts one heal from Healing Spirits. If it reaches 0, the spell will end. Otherwise, the program will wait 60 seconds and run again

    remainingUses -= 1
    print("Remaining Uses: " + str(remainingUses))
    if remainingUses <= 0:
        print("Spell has ended")
        break
    else:
        time.sleep(60)
