# Import libraries
import random

# Define dice functions
def d4():
    d4 = random.randint(1,4)
    return d4

# Define external modifiers - CHANGE AS NECESSARY
proficiencyBonus = 4
abilityBonus = 0
spellcastingModifier = proficiencyBonus + abilityBonus
domain = "Life"

# Define spell variables
total = 0
level = 0

# Verify the spell is being cast at a valid level
while level > 9 or level < 1:
    level = int(input("What level are you casting the spell at? Level must be between 1 and 9 inclusive "))    

# Roll and output dice, then add to a running total
for i in range (level):
    roll = d4()
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
print("Grand total: " + str(total)
