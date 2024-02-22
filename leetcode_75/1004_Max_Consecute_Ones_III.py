"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of 1s and 0s with max 0 flips to be k, find max consecutive number of 1s.

Final algorithm followed:
1. Use a sliding window, the crux is to define the conditions inside the for loop.
2. Track number of 0s in the window, whenever it exceeds limit, shrink window until you get allowed numz.

Summary of common mistakes/tricks:
Window shrink logic is tough to determine right off the bat, the trick is to be greedy.
"""
# Solution with comments
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Use sliding window, b represents begin, e is end
        # use a variable to track number of zeroes in the window
        b, numz, ans = 0, 0, 0
        for e in range(len(nums)):
            # if you encounter 0, increase numz
            if nums[e] == 0:
                numz += 1
            # when num zeroes cross k, shrink window until numz <= k
            while numz > k:
                b += 1
                if nums[b-1] == 0:
                    numz -= 1
            # update the answer, it is always a valid window
            ans = max(ans, e-b+1)
            
        return ans