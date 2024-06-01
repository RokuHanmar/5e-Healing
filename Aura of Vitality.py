# Import libraries
import random
import time

# Define dice functions
def d6():
    d6 = random.randint(1,6)
    return d6

# Define external modifiers - CHANGE AS NECESSARY
domain = "Life"

# Define spell variables
total = 0
level = 3

# Roll and output dice, then add to a running total
total = 0
for i in range (2):
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
