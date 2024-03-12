"""
1732. Find the highest altitude
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of altitude gains and starting point, return the max altitude reached.

Final algorithm followed:
1. Keep storing altitude at every point, keep summing the gain to the most recent altitude
2. Return the max altitude

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        ans = 0

        for i in range(len(gain)):
            alt.append(alt[i]+gain[i])
            ans = max(ans, alt[i+1])
        return ans