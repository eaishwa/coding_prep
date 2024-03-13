"""
2390. Removing Stars from a String
https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Remove stars along with one character preceding it in a string and return the answer.

Final algorithm followed:
1. Keep adding characters into answer string, when you encounter *,  overwrite answer by removing last element from it.

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        # keep adding current element to answer as long as it is not *
        # when it is *, overwrite answer by excluing the last element in answer
        for e in range(len(s)):
            if s[e] != '*':
                ans = ans + s[e]
            else:
                ans = ans[:-1]
        return ans