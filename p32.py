# Top score

# Write a function that takes:

# 1. a list of unsorted_scores
# 2. the highest_possible_score in the game

# and returns a sorted list of scores in less than O(nlgn) time.

def sort_scores(scores, highest_possible_score):
    sorted = []
    counts = [0] * (highest_possible_score + 1)

    for score in scores:
        counts[score] += 1

    for score in reversed(range(len(counts))):
        for i in range(counts[score]):
            sorted.append(score)

    return sorted

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

print sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# returns [91, 89, 65, 53, 41, 37]
