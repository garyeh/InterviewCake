def reverse_string(string):
    letters = list(string)

    midpoint = len(letters) / 2
    for idx in range(midpoint):
        letters[idx], letters[len(letters) - idx - 1] = letters[len(letters) - idx - 1], letters[idx]

    return ''.join(letters)

print reverse_string("abcde")
