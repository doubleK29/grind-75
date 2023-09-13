"""
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def three_sum_bf(nums: list[int]):
    n = len(nums)
    res = []
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

    return res


def three_sum_optim(nums: list[int]):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triple = [nums[i], nums[left], nums[right]]
                res.append(triple)
                while left < right and nums[left] == triple[1]:
                    left += 1
                while left < right and nums[right] == triple[2]:
                    right -= 1

    return res
# def insert_interval(intervals: list[list[int]], newInterval: list[int]):
#     result = []
#     for i in range(len(intervals)):
#         if newInterval[1] < intervals[i][0]:
#             result.append(newInterval)
#             return result + intervals[i:]
#         elif newInterval[0] > intervals[i][1]:
#             result.append(intervals[i])
#         else:
#             newInterval

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum_optim(nums))
