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
total = 0
level = 0

# Verify the spell is being cast at a valid level
while level > 9 or level < 2:
    level = int(input("What level are you casting the spell at? Level must be between 2 and 9 inclusive "))    

# Roll and output dice, then add to a running total
for i in range (level):
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
print("Spellcasting bonus: " + str(spellcastingModifier))
print("Domain bonus: " + str(lifeBonus))
total += spellcastingModifier + lifeBonus
print("Grand total: " + str(total))
print("Don't forget to roll the d4")
