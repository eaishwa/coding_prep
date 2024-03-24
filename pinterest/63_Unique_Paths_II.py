"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

What is the question?
Given a grid, go from start to end by not using obstacled cells. Return total number of paths.

Final algorithm followed:
1. DP

Summary of common mistakes/tricks:
"""
"""
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        res = [[0 for i in range(cols)] for i in range(rows)]
        c = 0
        while c < cols and obstacleGrid[0][c] != 1:
            res[0][c] = 1
            c+=1
        r = 0
        while r < rows and obstacleGrid[r][0] != 1:
            res[r][0] = 1
            r+=1
        # DP to fill up number of paths to reach a given cell
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != 1:
                    res[r][c] = res[r-1][c] + res[r][c-1]
        
        return res[rows-1][cols-1]