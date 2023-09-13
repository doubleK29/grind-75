"""
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Explaination:
the major element will occur more than n/2 times
"""


def major_element_sorting(nums):
    nums.sort()
    n = len(nums)
    return nums[n // 2]


def major_element_hash(nums):
    tmp = {}
    n = len(nums) // 2
    for i in range(len(nums)):
        if nums[i] not in tmp:
            tmp[nums[i]] = 1
        else:
            tmp[nums[i]] += 1

    for key, value in tmp.items():
        if value > n:
            return key


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(major_element_hash(nums))
