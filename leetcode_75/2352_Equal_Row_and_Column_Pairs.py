"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Count the number of col and row pairs that match in a grid

Final algorithm followed:
1. Store rows in the form of hashmap
2. For every col, if the same row is found in hm, add number of such rows to the answer
3. Return answer

Summary of common mistakes/tricks:
Know that you need to add the number of rows to the answer, not 1.
"""
# Solution with comments
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = {}
        n = len(grid)
        ans = 0
        # store rows in the form of hashmap to keep track of counts
        for r in range(n):
            if tuple(grid[r]) in rows:
                rows[tuple(grid[r])] += 1
            else:
                rows[tuple(grid[r])] = 1
        # for every col, if a matching row is found, add number of rows to the answer
        # this way, we count number of matching rows to a column individually
        for c in range(n):
            c_str = []
            for r in range(n):
                c_str.append(grid[r][c])

            if tuple(c_str) in rows:
                    ans += rows[tuple(c_str)]

        return ans