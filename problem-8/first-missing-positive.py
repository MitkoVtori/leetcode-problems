'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''


def first_missing_positive(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    for i in range(len(nums)):

        index = abs(nums[i]) - 1

        if len(nums) > index > -1:
            if nums[index] == 0:
                nums[index] = -(len(nums) + 1)
            else:
                nums[index] = -1 * abs(nums[index])

    for i in range(1, len(nums) + 1):
        index = i - 1
        if nums[index] >= 0:
            return i

    return len(nums) + 1
