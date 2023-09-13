"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1
"""


def two_sum_bf(nums, target):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_opt(nums, target):
    tmp = {}
    for i in range(len(nums)):
        if nums[i] in tmp:
            return [tmp[nums[i]], i]
        tmp[target - nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_opt(nums, target))
