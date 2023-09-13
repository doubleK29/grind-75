"""
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""


def sort_colors(nums):
    n = len(nums)

    blue_idx = 0
    for i in range(n):
        if nums[i] != 2:
            nums[i], nums[blue_idx] = nums[blue_idx], nums[i]
            blue_idx += 1

    red_idx = n - 1
    for i in range(n - 1, -1, -1):
        if nums[i] != 0:
            nums[i], nums[red_idx] = nums[red_idx], nums[i]
            red_idx -= 1

    return nums


if __name__ == "__main__":
    nums = [0, 1, 1, 2, 1, 0]
    print(sort_colors(nums))
