"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of numbers, return the index of any peak element.

Final algorithm followed:
1. Use binary search, frame the conditions inside the while loop wisely.
2. You need to know whether you are ascending or descending the peak, use mid+1th number to know that.
3. If you are ascending a slope, move left ptr towards the peak, else bring right ptr towards peak.
4. Return left pointer in the end

Summary of common mistakes/tricks:
Framing the conditions inside while loop is tricky, you don't always need to return mid idx. Think how other ptrs can be useful too.
"""
# Solution with comments
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums)-1

        while l < r:
            mid = (l+r) // 2
            
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l