# Import libraries
import random

# Define dice functions
def d4():
    d4 = random.randint(1,4)
    return d4

# Define external modifiers - CHANGE AS NECESSARY
proficiencyBonus = 4
wisdomBonus = 0
spellcastingModifier = proficiencyBonus + wisdomBonus


# Healing Word
def healingWord():
    total = 0
    level = 0
    while level > 9 or level < 1:
        level = int(input("What level are you casting the spell at? Level must be between 1 and 9 inclusive "))    
    for i in range (level):
        roll = d4()
        print(roll, end=" ")
        total += roll
    total += spellcastingModifier
    print("\n")
    print(total)
        
healingWord()
