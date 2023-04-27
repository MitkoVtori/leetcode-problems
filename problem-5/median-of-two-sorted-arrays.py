'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


def find_median_sorted_arrays(nums1, nums2):
    numbers = nums1 + nums2  # [1, 3, 2, 4]
    numbers.sort()  # [1, 2, 3, 4]
    length = len(numbers) # 4
    if len(numbers) % 2 == 0:
        slice_method = int(length/2)
        median = numbers[slice_method-1] + numbers[slice_method]  # [1, 2], [3, 4]. result = 2 + 3
        return median*0.5 # median / 2
    else:
        median = numbers[(length-1)/2]  # [1, 2, 3], result = 2
        return median
