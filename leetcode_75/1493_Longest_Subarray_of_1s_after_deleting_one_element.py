"""
1493. Longest Subarray of 1s after deleting one element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given a binary array nums, you should delete one element from it. Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Final algorithm followed:
1. Sliding window approach with 2 ptrs and a for loop
2. Track number of 0s, when you encounter one, until your current window shrinks to no 0s, shrink the window
3. Once achieved, account current 0 to be deleted
4. Update answer

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window with begin and end variables
        b=0
        # tracker to track number of deletions done
        num_del = 0
        ans = 0
        for e in range(len(nums)):
            # if you encounter 0
            if nums[e] == 0:
                # unless num_del is > 0, shrink the window
                while num_del > 0:
                    b += 1
                    # if you just passed a 0, reduce num_del by 1
                    if nums[b-1] == 0:
                        num_del -= 1
                # add 1 to num_del as you'll be deleting this current element
                num_del += 1
                # update answer to be len of the window always short by 1 element as we always delete one
            ans = max(ans, e-b)
        return ans