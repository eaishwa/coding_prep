"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array nums, return an array such that answer[i] = product of all elements except nums[i].
You can't use division operation and the algo should run in O(n) time!

Final algorithm followed:
1. The intuition is to compute product of left and right parts of the number considered. Finally multiply both the parts for each number.
2. Maintain 2 arrays of len(nums), left and right with first and last elements assigned to 1.
3. For each i, Left array maintain preducts upto nums[i-1], right array maintains product from nums[i:]
4. Fill up left and right arrays as described above. 
5. Multiply left[i] and right[i] for each i, return the answer. 
Space complexity - O(n)
Time Complexity - O(n)
"""
# Solution with comments
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left,right = [0]*len(nums), [0]*len(nums)
        left[0], right[len(nums)-1] = 1,1
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        output = []
        print(left, right)
        for i in range(0,len(nums)):
            output.append(left[i]*right[i])
        return output