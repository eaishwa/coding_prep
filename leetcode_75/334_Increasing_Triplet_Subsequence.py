"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Final algorithm followed:
1. It is a greedy approach, assign two variables first and second, initialize them to infinity.
2. Iterate through the array and greedily update first and second variables.
    a. if n <= first, first = n
    b. elif n <= second, second = n. We will reach here if n > first.
    c. else we have n > first and second, we have found a triplet of increasing order, so return True.
3. return False by default.

Space complexity - O(1), Time Complexity - O(n)

Summary of common mistakes/tricks:
One mistake to do is to assign first and second to -infinity and having conditions 2a, 2b to be >=.
This is wrong, because you will find a triplet of decreasing order by this method.

Other resources / videos to help understand this question better: 
NA
"""
# Solution with comments
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False