"""
1926. Nearest Exit from Entrance
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75
What is the question?
Given a maze with an entrance, find the nearest exit.

Final algorithm followed:
1. The intuition is to use BFS as it is guaranteed that the first valid exit we find is the shortest path!
2. Start from entrance, use the maze value '+' to mark as visited!
3. Keep moving as long as the cell is valid, use the queue itself to store distance (row,col,distance).
4. Stop when you arrive at a valid exit and return distance!

Summary of common mistakes/tricks:
A common mistake is to take DFS route and get stuck into not calculating distance properly.
I couldn't arrive at the right solution satisfying all test cases trying DFS + backtracking.
"""
# Solution with comments
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Flip maze cell value to '+' to mark visited
        # mark maze entrance as visited, as it can't be exit
        maze[entrance[0]][entrance[1]] = '+'

        # start from entrance and search for nearest exit
        que = [[entrance[0], entrance[1], 0]]

        while que:
            curr_r, curr_c, curr_d = que.pop(0)

            # for all neighbors
            for d in dirs:
                next_r = curr_r + d[0]
                next_c = curr_c + d[1]

                # check if any next_r or next_c is a valid step
                if next_r >= 0 and next_r < rows and next_c >= 0 and next_c < cols and maze[next_r][next_c] == '.':
                    if next_r in [0,rows-1] or next_c in [0,cols-1]:
                        return curr_d + 1
                    else:
                        maze[next_r][next_c] = '+'
                        que.append([next_r, next_c, curr_d+1])
        return -1