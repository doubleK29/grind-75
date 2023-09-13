"""
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""


def combination_sum(nums, target):
    """
    [2, 3, 6, 7] and target = 7
        0   1   2   3   4   5   6       7
    2   0   0   2   0   2,2 0   2,2,2   0
    3   0   0   0   3   0   3, 2
    6
    7
    """
    dp = [[] for _ in range(target + 1)]
    for num in nums:
        for i in range(1, target + 1):
            if num > i:
                continue
            elif num == i:
                dp[i].append([num])
            else:
                for j in dp[i - num]:
                    dp[i].append(j + [num])

    return dp[-1]


if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    # target = 7
    # print(combination_sum(candidates, target))
    pairs = dict(("()", "{}"))
    print(pairs)