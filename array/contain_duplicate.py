"""
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def contain_duplicate(nums):
    tmp = {}
    for num in nums:
        if num not in tmp:
            tmp[num] = 1
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 5, 6]
    print(contain_duplicate(nums))
