"""
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge_intervals(intervals):
    res = []
    intervals.append([1e5, 1e6])
    tmp = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] > tmp[1]:
            res.append(tmp)
            tmp = intervals[i]
        else:
            tmp = [min(intervals[i][0], tmp[0]), max(intervals[i][1], tmp[1])]

    return res


def merge_intervals_2(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1] = [min(interval[0], res[-1][0]), interval[1]]

    return res


if __name__ == "__main__":
    intervals = [[1, 4], [4, 5]]
    print(merge_intervals_2(intervals))
