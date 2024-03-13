"""
2211. Count Collisions on Road
https://leetcode.com/problems/count-collisions-on-a-road/description/

What is the question?
Count collisions on road given series of directions of cars as input.

Final algorithm followed:
1. Use a stack and make decision on collision every single time

Summary of common mistakes/tricks:
Know when and how to count collisions.
"""
# Solution with comments
class Solution:
    def countCollisions(self, directions: str) -> int:
        
        c = 0
        # store the first car direction in stack
        stack = [directions[0]]
        for i in range(1, len(directions)):
            curr = directions[i] 
            # If current car is gonna collide with topmost car on stack, count collisions           
            if len(stack)>0 and stack[-1]+curr in ['RL','RS','SL']:
                if stack[-1]+curr == 'RL':
                    c+=2
                else:
                    c+=1
                # replace top of stack with stationary S
                stack.pop()
                stack.append('S')
            # if no collision, append to stack
            else:
                stack.append(directions[i])
        return c