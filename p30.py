# Permutation palindrome

# Write an efficient function that checks whether any permutation
# of an input string is a palindrome.

def is_permutation_palindrome(string):
    seen_letters = set()

    for char in string:
        if char in seen_letters:
            seen_letters.remove(char)
        else:
            seen_letters.add(char)

    return len(seen_letters) <= 1

print is_permutation_palindrome("civic")
print is_permutation_palindrome("ivicc")
print is_permutation_palindrome("civil")
print is_permutation_palindrome("livci")
