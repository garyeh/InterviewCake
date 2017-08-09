# Merge sorted arrays

# We have our lists of orders sorted numerically already, in lists.
# Write a function to merge our lists of orders into one sorted list.

def merge(list1, list2):
    result = []
    idx1 = 0
    idx2 = 0

    while idx1 != len(list1) and idx2 != len(list2):
        if list1[idx1] < list2[idx2]:
            result.append(list1[idx1])
            idx1 += 1
        else:
            result.append(list2[idx2])
            idx2 += 1

    return result + list1[idx1:] + list2[idx2:]

a = [1,3,5,7,9]
b = [2,4,6,8]
print merge(a, b)
