'''
You are given an integer array nums containing distinct numbers,
and you can perform the following operations until the array is empty:

If the first element has the smallest value, remove it

Otherwise, put the first element at the end of the array.

Return an integer denoting the number of operations it takes to make nums empty.

Example 1:

Input: nums = [3,4,-1]
Output: 5

Operation	Array
1	[4, -1, 3]
2	[-1, 3, 4]
3	[3, 4]
4	[4]
5	[]

Example 2:

Input: nums = [1,2,4,3]
Output: 5

Operation	Array
1	[2, 4, 3]
2	[4, 3]
3	[3, 4]
4	[4]
5	[]

Example 3:

Input: nums = [1,2,3]
Output: 3

Operation	Array
1	[2, 3]
2	[3]
3	[]


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
All values in nums are distinct.
'''


def count_operations_to_empty_array(nums):
    pos = {v: i for i, v in enumerate(nums)}
    res = n = len(nums)
    nums.sort()
    for i in range(1, n):
        if pos[nums[i]] < pos[nums[i - 1]]:
            res += n - i
    return res

    # n = len(nums)
    # pos = sorted(range(n), key=lambda i: nums[i])
    # return n + sum(n - i for i in range(1, n) if pos[i] < pos[i - 1])


# def count_operations_to_empty_array(nums):
#     operations = 0
#     while nums:
#         operations += 1
#         n = nums.pop(0)
#         if nums:
#             if n > min(nums):
#                 nums.append(n)
#     return operations

# def count_operations_to_empty_array(nums, count=0):
#     if not nums:
#         return count
#
#     n = nums.pop(0)
#
#     if nums:
#         if n > min(nums):
#             nums.append(n)
#
#     return count_operations_to_empty_array(nums, count+1)
