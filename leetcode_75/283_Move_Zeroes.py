"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Final algorithm followed:
1. Iterate through the array and delete whenever you find 0, also keep counting it.
2. Append as many 0s you deleted to the array.
"""
# Solution with comments
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count,i = 0,0
        # Always compute len(nums) as it changes inside the loop when we delete 0s.
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                count = count + 1
            # Increment i only when you did not delete a 0.
            else:
                i = i+1
        nums.extend([0]*count)