"""
198. House Robber
https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Find out max money you could rob given series of homes but you just can't rob from adjacent homes.

Final algorithm followed:
See comments

Summary of common mistakes/tricks:
Common mistake is to assume you rob alternate houses! You needn't, you can skip any number of houses but steal max money.
"""
# Solution with comments
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        # You either rob a house or skip a house, look at all possibilities and make a decision.
        # rob array stores max money robbed if you robbed house i
        rob = [nums[0]]
        # skip array stores max money robbed if you skipped house i
        skip = [0]
        answer = max(nums[0], 0)

        for i in range(1, len(nums)):
            # if you rob i, you skipped i-1
            rob.append(skip[i-1]+nums[i])
            # if you skip i, you could have either robbed i-1 or skipped i-1
            skip.append(max(rob[i-1], skip[i-1]))
            # store the max money robbed until house i
            answer = max(answer, rob[i], skip[i])
        return answer