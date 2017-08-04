# Simulate 7-sided die

# You have a function rand5() that generates a random integer from 1 to 5.
# Use it to write a function rand7() that generates a random integer from 1 to 7.

from random import randint
# use randint(0,4)

def rand7():
    roll = randint(0,4) * 5 + randint(0,4) + 1
    while (roll > 21):
        roll = randint(0,4) * 5 + randint(0,4) + 1

    return roll % 7 + 1

print rand7()
