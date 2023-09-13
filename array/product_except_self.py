"""
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def product_except_self_1(nums: list[int]):
    length = len(nums)
    prefix = 1
    postfix = 1
    left = [1] * length
    right = [1] * length
    res = [1] * length
    for i in range(length - 1):
        prefix *= nums[i]
        left[i + 1] = prefix
    for i in range(length - 1, 0, -1):
        postfix *= nums[i]
        right[i - 1] = postfix
    for i in range(len(nums)):
        res[i] = left[i] * right[i]

    return res


def product_except_self_2(nums: list[int]):
    length = len(nums)
    postfix = 1
    left = [1] * length
    # right = [1] * length
    # res = [1] * length
    for i in range(length - 1):
        postfix *= nums[i]
        left[i + 1] = postfix
    postfix = 1
    for i in range(length - 1, -1, -1):
        left[i] = left[i] * postfix
        postfix *= nums[i]

    return left


if __name__ == "__main__":
    nums = [1, -1 , 3, 0, 2, 6]
    print(product_except_self_2(nums))
