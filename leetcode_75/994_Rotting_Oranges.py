"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75
What is the question?
Given a grid of oranges, it might contain fresh and rotten oranges. Find out the time to rotting of the entire grid.

Final algorithm followed:
1. The intuition is to use BFS! Batch process all rotten oranges at once and increment minutes once a batch is completely processed.
2. To demarcate batches, append an identifier to the queue.

Summary of common mistakes/tricks:
The crux is to identify how to increment minutes after all current rotten oranges at once are processed.
"""
# Solution with comments
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        que = []
        # variable to track if all oranges are getting rotten
        fresh = 0
        # identify initial rotten oranges and put them all in que
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    que.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        # demarcate
        que.append((-1,-1))
        
        mins = -1
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while que:
            r,c = que.pop(0)
            # if demarcation is found, increment minutes
            if r == -1:
                mins += 1
                # if more oranges are in que, demarcate end of the batch
                if que:
                    que.append((-1,-1))
            else:
                for d in dirs:
                    next_r, next_c = r+d[0], c+d[1]
                    if next_r >= 0 and next_r < rows and next_c >= 0 and next_c < cols:
                        if grid[next_r][next_c] == 1:
                            grid[next_r][next_c] = 2
                            fresh -= 1
                            que.append((next_r, next_c))
        return mins if fresh == 0 else -1