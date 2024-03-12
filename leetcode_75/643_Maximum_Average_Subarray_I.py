"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array, find the max avg subarray of size k

Final algorithm followed:
1. Maintain averages in the form of sum, denominator is constant
2. Store answer in a separate variable

Summary of common mistakes/tricks:
Beware of which number you are adding to the sum! It has to be the right most new element.
"""
# Solution with comments
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize sum and avg with first k numbers
        ans = sum(nums[:k]) / k
        curr_sum = sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            # remove previous left most number and add a number to the right
            curr_sum = curr_sum - nums[i-1] + nums[i+k-1]
            # update the average
            ans = max(ans, curr_sum/k)
        return ans