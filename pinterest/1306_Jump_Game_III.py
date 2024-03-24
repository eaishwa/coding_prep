"""
1306. Jump Game III
https://leetcode.com/problems/jump-game-iii/description/

What is the question?
Given an array and start idx and traverse criteria, find if you can reach val 0.

Final algorithm followed:
1. BFS! 
2. or DFS!

Summary of common mistakes/tricks:
Trying recursion the wrong way!
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS, start from the start index in the queue
        l = len(arr)
        q = [start]
        while q:
            curr = q.pop(0)
            # when you find the right answer, return
            if arr[curr] == 0:
                return True
            # if you've already visited this idx, continue because
            # you know you did not find the right answer here
            if arr[curr] < 0:
                continue
            # these are your neighbors
            options = [curr+arr[curr], curr-arr[curr]]
            for o in options:
                # if they're legit and not visited, enque them
                if o >= 0 and o < l:
                    q.append(o)
            # visit the current idx
            arr[curr] = -arr[curr]
        return False
# DFS
class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        def jump(idx, mem):
            if idx >= len(arr) or idx < 0:
                return
            if arr[idx] == 0:
                return True
            if idx not in mem:
                mem.add(idx)
                return jump(idx+arr[idx], mem) or jump(idx-arr[idx], mem)
            return False
        return jump(start, set())