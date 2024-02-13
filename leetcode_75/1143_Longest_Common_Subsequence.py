"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
FInd the longest common subsequence in 2 strings.

Final algorithm followed:
1. Initialize 2D array of len(text1)*len(text2) size of 0s.
2. Fill up the cells counting max subseq len upto that point.

Summary of common mistakes/tricks:
Order of conditions inside the for loop is important.
"""
# Solution with comments
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r,c = len(text1), len(text2)
        res = [[0 for i in range(c)] for j in range(r)]

        for i in range(r):
            for j in range(c):
                if i==0 and j==0 and text1[i]==text2[i]:
                    res[i][j] = 1
                # cases to cover 1st row and 1st col
                elif i == 0:
                    if text1[i] == text2[j]:
                        res[i][j] = 1
                    else:
                        res[i][j] = res[i][j-1]
                elif j == 0:
                    if text1[i] == text2[j]:
                        res[i][j] = 1
                    else:
                        res[i][j] = res[i-1][j]
                # if matching letters are found, incr subseq length by 1
                elif text1[i] == text2[j] and i!= 0 and j != 0:
                    res[i][j] = res[i-1][j-1] + 1
                # else keep recording the max len so far
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        return res[r-1][c-1]