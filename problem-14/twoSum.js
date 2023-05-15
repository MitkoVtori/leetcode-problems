/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
      for (let n = 0; n < nums.length; n++) {
        if (i != n && nums[i] + nums[n] == target)
          return [i, n]
      }
    }
};