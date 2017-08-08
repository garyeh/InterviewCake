# Single riffle shuffle

# Write a function to tell us if a full deck of cards shuffled_deck
# is a single riffle of two other halves half1 and half2

def is_riffle(shuffled_deck, half1, half2):
    idx1 = 0
    idx2 = 0

    for card in shuffled_deck:

        if idx1 < len(half1) and card == half1[idx1]
            idx1 += 1

        elif idx2 < len(half2) and card == half2[idx2]
            idx2 += 1

        else:
            return False

    return True
