# Product of other numbers
# O(n) time
# O(n) space

def products_except_at_index(nums):
    products = [1] * len(nums)

    left_product = 1
    for i in range(len(nums)):
        products[i] *= left_product
        left_product *= nums[i]

    right_product = 1
    for i in reversed(range(len(nums))):
        products[i] *= right_product
        right_product *= nums[i]

    return products


print products_except_at_index([1,7,3,4])
