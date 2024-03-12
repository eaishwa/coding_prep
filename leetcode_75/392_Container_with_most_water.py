"""
11. Container with most water
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of container heights, make a container with x axis and heights as y axis to find a container with most water.

Final algorithm followed:
1. 2 ptr approach
2. Greedily move ptrs and store answer in every step

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        # Have a left and right pointer
        l,r = 0, len(height)-1
        # You're looking at a rectangular area in every computation
        # Greedily move the pointers and keep storing the max answer
        while l < r:
            # find the length and breadth of the rectangle to compute area
            area = min(height[l], height[r]) * (r-l)
            ans = max(ans, area)
            # Greedily move left ptr if it is hindering the area measure
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
        return ans