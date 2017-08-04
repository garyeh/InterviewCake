# Which appears twice

# I have a list of n + 1n+1 numbers. Every number in the range 1..n
# appears once except for one number that appears twice.
# Write a function for finding the number that appears twice.

def which_appears_twice(nums):
    n = max(nums)
    series_sum = (n ** 2 + n) / 2
    return sum(nums) - series_sum

print which_appears_twice([1,2,2,3,4,5])
