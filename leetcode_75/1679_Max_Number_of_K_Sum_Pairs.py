"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given a list of numbers, and you're allowed to remove 2 numbers at once that sum upto k, how many such pairs do you remove?

Final algorithm followed:
1. Track live state of list in a hashmap using counter
2. Iterate through every element in the array and figure out if you can remove it
3. Keep counting the number of pairs removed

Summary of common mistakes/tricks:
Iterating through the hashmap itself is a common mistake, it goes through one number only once.
"""
# Solution with comments
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # Use hashmap to track live status of the array
        hm = Counter(nums)
        op = 0
        # Traverse the original array instead of hashmap to process all elements correctly
        for key in nums:
            # if this number is still not removed from array
            if hm[key] > 0:
                # remove it
                hm[key] -= 1
                # if the pair exists
                if k-key in hm and hm[k-key] > 0:
                    # found a pair to remove
                    op += 1
                    # remove the pair too
                    hm[k-key] -= 1
                else:
                    # keep the number back in
                    hm[key]+=1
        return op