"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given m*n path to traverse and constraints, determine number of unique paths to go from start to end point

Final algorithm followed:
1. Use DP, keep storing num paths at each cell and return num paths in the destination cell

Summary of common mistakes/tricks:
Initialize correctly, handle edge case ahead!
"""
# Solution with comments
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # edge case, if start and end points are same, then return 1
        if m == 1 and n == 1:
            return 1
        # initialize result that will store num unique paths until each cell
        res = [[0 for i in range(n)] for j in range(m)]
        # all cells in 1st row and 1st col except start cell to be initialized to 1
        # because there is only 1 unique path to reach these cells
        for i in range(1,n):
            res[0][i] = 1
        for j in range(1,m):
            res[j][0] = 1
        # from (1,1) onwards, sum up num of uniq paths until left and top of current cell
        for r in range(1,m):
            for c in range(1,n):
                res[r][c] = res[r-1][c] + res[r][c-1]
        # return ans from the destination cell!
        return res[m-1][n-1]