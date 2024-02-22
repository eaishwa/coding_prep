"""
435. Non Overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Final algorithm followed:
1. Sort by end times of the intervals, this is because you wanna greedily consider only one interval among all overlapping and that is the one that ends earliest.
2. The idea is to find out max non overlapping intervals.
3. Keep a ptr to prev valid interval, add to your answer as you find non overlapping intervals
4. Return num_intervals - answer.

Summary of common mistakes/tricks:
The trick is to find which sort key to use.
"""
# Solution with comments
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # The idea is to count the max number of non overlapping intervals possible
        # For that, be greedy and keep the earlier ending interval when you encounter overlapping intervals

        # sort by end time
        intervals.sort(key = lambda x: x[1])
        # always keep first interval because it ends the soonest
        ans = 1
        # have a pointer to the immediate previous interval
        j = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = intervals[j]
            # if current interval starts after past interval ends, it is non-overlapping
            if curr[0] >= prev[1]:
                # increment answer by including this interval
                ans += 1
                # make this interval the immediate past
                j = i
        return len(intervals) - ans