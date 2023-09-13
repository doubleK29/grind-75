"""
Example 1:
Input:
[[0,30],[5,10],[15,20]]
Output:
 false

Example 2:
Input:
 [[7,10],[2,4]]
Output:
 true
"""


def meeting_room(intervals: list[list[int]]):
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True


if __name__ == "__main__":
    intervals = [[0, 5], [5, 10], [15, 20]]
    print(meeting_room(intervals))
