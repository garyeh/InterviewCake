# Parenthesis matching

# "Sometimes (when I nest them (my parentheticals) too much
# (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above,
# along with the position of an opening parenthesis,
# finds the corresponding closing parenthesis.

def find_closing(string, open_pos):
    additional_open_parentheses = 0

    idx = open_pos + 1
    while idx < len(string):
        if string[idx] == ')' and additional_open_parentheses == 0:
            return idx
        elif string[idx] == ')':
            additional_open_parentheses -= 1
        elif string[idx] == '(':
            additional_open_parentheses += 1

        idx += 1

    return 'No matching closing parenthesis'

test = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print find_closing(test, 10)
