"""
980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/submissions/1211194812/

What is the question?
Given a grid, go from start to end by covering all non obstacled paths, return number of such paths.

Final algorithm followed:
1. DFS + backtracking
2. You need backtracking to be able to retract if a given path does not lead to destination

Summary of common mistakes/tricks:
"""
"""
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # DFS + Backtracking!
        nonobs, self.ans = 0, 0
        rows, cols = len(grid), len(grid[0])
        sr,sc = 0,0
        # calculate non obsolete number of cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>=0:
                    nonobs+=1
                if grid[r][c] == 1:
                    sr,sc = r,c

        def traverse(r, c, remain):
            # if at the end cell and traversed all nonobs cells
            if grid[r][c] == 2 and remain == 1:
                self.ans += 1
                return
            temp = grid[r][c]
            # mark current cell as visited
            grid[r][c] = -4
            remain -= 1
            options = [[r, c+1], [r, c-1], [r-1, c], [r+1, c]]
            for x,y in options:
                if x < 0 or x >= rows or y < 0 or y >= cols:
                    continue
                if grid[x][y] != -1 and grid[x][y]!=-4:
                    traverse(x, y, remain)
            # restore value as you backtrack
            grid[r][c] = temp
        
        traverse(sr, sc, nonobs)
        return self.ans