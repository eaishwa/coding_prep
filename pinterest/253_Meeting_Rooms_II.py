"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/submissions/1186216804/

What is the question?
Given a bunch of meeting intervals, find out min number of rooms for them!

Final algorithm followed:
1. Sort start and end times separately.
2. Only issue a meeting room when current meeting starts before the prior soonest ending meeting hasn't ended.
3. Else, move to the next end time and do not issue any new meeting rooms.

Summary of common mistakes/tricks:
Isolating the intervals and taking out start and end times is the crux.
"""
# Solution with comments
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort start times and end times separately
        start_times, end_times = [],[]
        for (x,y) in intervals:
            start_times.append(x)
            end_times.append(y)
        start_times.sort()
        end_times.sort()

        e = 0
        nrooms = 0
        # for every meeting start time, decide if a new room is needed
        for s in start_times:
            # you have a meeting starting before the soonest end time for another meeting
            if s < end_times[e]:
                nrooms += 1
            # else, your soonest meeting has ended, so update it
            else:
                e += 1
        return nrooms
