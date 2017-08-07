# Recursive string permutations

# Write a recursive function for generating all permutations
# of an input string. Return them as a set.

def generate_permutations(string):
    if len(string) <= 1:
        return {string}

    result = set()
    pivot = string[0]
    sub_permutations = generate_permutations(string[1:])

    for sub in sub_permutations:
        for idx in range(len(sub) + 1):
            permutation = sub[:idx] + pivot + sub[idx:]
            result.add(permutation)

    return result

print generate_permutations("abc")
