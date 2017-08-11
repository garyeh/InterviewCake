# Highest product of 3

# Given a list of integers, find the highest product you can get
# from three of the integers.

def max_product(A):
    max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
    min1, min2 = float("inf"), float("inf")

    for i in range(len(A)):
        if A[i] > max1:
            max3 = max2
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            max3 = max2
            max2 = A[i]
        elif A[i] > max3:
            max3 = A[i]
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]

    return max([max1 * max2 * max3, max1 * min1 * min2])

A = [1,-10,-20,8,4,6]
print max_product(A)
