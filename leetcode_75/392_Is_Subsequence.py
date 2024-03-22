"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Final algorithm followed:
1. The intuition is that we are searching for the subseq s in string t. Address base cases.
2. Have a pointer curr to s, denoting which letter we are at in s.
3. Iterate through t, whenever you find curr letter, move curr by 1 step. Immediately check if it is end of source.
4. Return true if yes, else False
"""
# Solution with comments
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        i = 0

        for c in t:
            if c == s[i]:
                i+=1
                if i == len(s):
                    return True
        return False