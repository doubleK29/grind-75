"""
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


def move_zero(nums: list[int]):
    idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[idx] = nums[idx], nums[i]
            idx += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zero(nums)
    print(nums)
