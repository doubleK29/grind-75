"""
Example 1:

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]

Output: [4,9,9,49,121]
"""


def sorted_squares(nums: list[int]):
    n = len(nums)
    nums[0] = nums[0] ** 2

    for i in range(1, n):
        nums[i] = nums[i] ** 2
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            nums[j] = key
            j -= 1

    return nums


if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    print(sorted_squares(nums))
