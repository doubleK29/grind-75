"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, \
    the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""


def max_water_area_bf(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            tmp_area = (j - 1) * min(height[i], height[j])
            if tmp_area > max_area:
                max_area = tmp_area
    return max_area


def max_water_area_optim(height):
    max_area = 0
    n = len(height)
    left = 0
    right = n - 1
    while left < right:
        tmp_area = (right - left) * min(height[left], height[right])
        if tmp_area > max_area:
            max_area = tmp_area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_water_area_optim(height))
