"""
72. Edit Distance
https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given 2 strings return the min number of operations to convert word1 to word2.

Final algorithm followed:
1. It has a DP solution which is pretty intuitive.
2. Keep filling bottom up.

Summary of common mistakes/tricks:
Common mistake is to not allocate empty string in 0th row and col, it leads to errors if not done.
"""
# Solution with comments
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m,n = len(word1), len(word2)

        # 2d array with m+1 * n+1 size, 0th row and col are for empty strings
        # you will solve subproblems bottom up
        res = [[0 for i in range(n+1)] for j in range(m+1)]
        # 0th row and col have monotonically increasing number of operations needed
        for i in range(m+1):
            res[i][0] = i
        for i in range(n+1):
            res[0][i] = i
        
        for r in range(m):
            for c in range(n):
                # if both characters are same, no operation needed
                if word1[r] == word2[c]:
                    res[r+1][c+1] = res[r][c]
                # take the min value of various options and add 1
                else:
                    res[r+1][c+1] = min(res[r][c], res[r][c+1], res[r+1][c]) + 1
        return res[m][n]