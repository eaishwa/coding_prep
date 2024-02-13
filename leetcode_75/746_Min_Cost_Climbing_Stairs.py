"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Find min cost of climbing stais given you can take one or two steps at a time and you have a cost to pay at each step.

Final algorithm followed:
1. Keep maintaining min cost upto step i, assign initial costs to be 0 to steps 0 and 1.
2. Start from step 2, and store min cost between reaching there from step i-1 or step i-2.

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # stores the min cost paid to reach upto each step
        min_cost = [0] * (len(cost)+1)
        # cost paid to reach 0 and 1th steps is 0
        for i in range(2, len(cost)+1):
            # min of whether you will take 1 step or 2 steps to reach current step
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
        return min_cost[-1]