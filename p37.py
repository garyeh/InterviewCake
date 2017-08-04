# Simulate 5-sided die

# You have a function rand7() that generates a random integer from 1 to 7.
# Use it to write a function rand5() that generates a random integer from 1 to 5.

from random import randint
# use randint(0,6)

def rand5():
    roll = randint(0,6)
    while (roll == 0 or roll == 6):
        roll = randint(0,6)

    return roll

print rand5()
