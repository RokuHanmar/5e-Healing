# Import libraries
import random

# Define dice functions
def d8():
    d8 = random.randint(1,8)
    return d8

# Define external modifiers - CHANGE AS NECESSARY
proficiencyBonus = 4
abilityBonus = 0
spellcastingModifier = proficiencyBonus + abilityBonus

domain = "Life"

# Define spell variables
totalDamage = 0
totalHealth = 0
level = 0


# Verify the spell is being cast at a valid level
while level > 9 or level < 5:
    level = int(input("What level are you casting the spell at? Level must be between 5 and 9 inclusive "))    

# Check if the target saved
save = input("Did the target save? y/n ")
if save.lower() == "y":
    level = level // 2
elif save.lower() == "n":
    level -= 1

# Roll and output dice, then add to a running total
for i in range (level):
    roll = d8()
    print(roll, end=" ")
    totalDamage += roll

# Calculate and output final total
if domain == "Life":
    lifeBonus = 2 + level
else:
    lifeBonus = 0

print("\n")
print("Total Damage: " + str(totalDamage))
totalHealth = totalDamage // 2
print("Total Healing: " + str(totalHealth))
print("Domain Bonus: " + str(lifeBonus))
totalHealth += lifeBonus
print("Grand Total Healed: " + str(totalHealth))
