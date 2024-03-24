"""
759. Employee Free Time
https://leetcode.com/problems/employee-free-time/description/

What is the question?
Given a bunch of employee schedules, find their free times.

Final algorithm followed:
1. Unroll schedules
2. Merge them all
3. Find the gaps!

Summary of common mistakes/tricks:
"""
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # unroll all the intervals
        intervals = []
        for sch in schedule:
            for i in range(len(sch)):
                intervals.append([sch[i].start, sch[i].end])
        # sort it
        intervals.sort()
        # merge it all
        if len(intervals) <= 1:
            return []
        merged = [intervals[0]]
        for s,e in intervals[1:]:
            if merged[-1][1] >= s:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s,e])
        # determine gaps from the merged intervals
        output = []
        for i in range(1,len(merged)):
            inter = Interval(merged[i-1][1], merged[i][0])
            output.append(inter)
        return output

        