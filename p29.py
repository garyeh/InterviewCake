# Bracket validator

# Write an efficient function that tells us whether or not
# an input string's openers and closers are properly nested.

def validate_brackets(string):
    map = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
    stack = []
    for char in string:
        # Found opening bracket
        if char in map:
            stack.append(char)

        elif len(stack) == 0 or char != map[stack[-1]]:
            return False

        # Found closing bracket + matching opening bracket at top of stack
        else:
            stack.pop()

    return stack == []

print validate_brackets("{[]()}")
print validate_brackets("{[(])}")
print validate_brackets("{[}")
print validate_brackets("{[]}(")
