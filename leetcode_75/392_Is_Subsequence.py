"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Final algorithm followed:
1. The intuition is that we are searching for the subseq s in string t. Address base cases.
2. Have a pointer curr to s, denoting which letter we are at in s.
3. Iterate through t, whenever you find curr letter, move curr by 1 step.
4. If curr-1 >= len(s)-1, then s is subseq of t.
"""
# Solution with comments
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if t == s:
            return True
        if len(t) == len(s) and t!=s:
            return False

        curr = 0
        for c in t:
            if curr >= len(s):
                break
            if c == s[curr]:
                curr = curr + 1

        if curr-1 >= len(s)-1:
            return True
        else:
            return False