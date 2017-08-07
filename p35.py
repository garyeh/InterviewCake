# In-place shuffle

# Write a function for doing an in-place shuffle of a list.

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling)

def shuffle(list):
    for idx in range(len(list)):
        rand_idx = get_random(idx, len(list))
        list[idx], list[rand_idx] = list[rand_idx], list[idx]

    return list

print shuffle([1,2,3,4,5])
