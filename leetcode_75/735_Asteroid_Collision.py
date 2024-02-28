"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given asteroids traveling left/right with their own magnitudes, figure out what asteroids will survive after collisions.

Final algorithm followed:
1. Process one asteroid after the other, a stack is helpful.
2. For each asteroid, you determine if it will stay in the stack or not.
3. Also for each top asteroid in stack, decide it stays or not.
4. You deal with every collision possible, in the end when you have a decision, carry it out and move on to the next asteroid.

Summary of common mistakes/tricks:
You can have a while loop inside for loop!
"""
# Solution with comments
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            curr = asteroids[i]
            flag = True
            # resolve collisions as long as thy exist
            while len(stack) != 0 and stack[-1] > 0 and curr < 0:
                # if curr asteroid is bigger, explode top asteroid and continue
                if abs(stack[-1]) < abs(curr):
                    stack.pop()
                    continue
                # if they are equal sizes, explode the top asteroid
                elif abs(stack[-1]) == abs(curr):
                    stack.pop()
                # if we reach here, we know current asteroid had exploded
                flag = False
                # after making the decision, break from while loop
                break
            # add current asteroid in if it is supposed to be alivve
            if flag:
                stack.append(curr)
        return stack