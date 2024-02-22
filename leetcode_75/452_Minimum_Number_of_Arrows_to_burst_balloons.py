"""
452. Minimum Number of Arrows to burst balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of balloons which could be overlapping, find the minimum number of arrows needed to burst them.

Final algorithm followed:
1. Sort by end, be greedy and increase arrows if the next balloon starts after previous balloon.

Summary of common mistakes/tricks:
Think greedy! this is something that does not occur immediately. You gotta kill the first balloon anyway!
Lay out the sorted intervals in front and aim to kill the first balloon and see how to encompass as many balloons as possible.
This will give the overall logic.
"""
# Solution with comments
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end point, we need to greedily shoot each balloon
        points.sort(key=lambda x: x[1])
        # you need to shoot the 1st balloon anyway
        ans = 1
        # keep track of previous arrow's end limit
        prev_end = points[0][1]
        for start, end in points:
            # if your current balloon starts after previous arrow's end, then we need new arrow
            if start > prev_end:
                ans += 1
                # update previous arrow's end
                prev_end = end
        return ans