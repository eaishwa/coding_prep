"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given piles of bananas and upper limit on number of hrs, find the least eating speed that koko can finish eating all bananas.

Final algorithm followed:
1. Define lower and upper limit on the answer, lower limit is 1 and upper limit is max bananas per pile.
2. Start binary search with mid eating speed, check if it is an eatable speed.
3. If yes, reduce the eating speed, if no, increase the eating speed.
4. Return the right pointer as it stores the least eating speed answer.

Summary of common mistakes/tricks:
Framing the conditions inside while loop is tricky, you don't always need to return mid idx. Think how other ptrs can be useful too.
"""
# Solution with comments
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # answer should be between 1 and max pile values
        # find the least eating speed such that eat time <= h

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r) // 2
            eat_hrs = 0

            for b in piles:
                eat_hrs += math.ceil(b/mid)

            # If it is an eatable mid, reduce eating speed
            if eat_hrs <= h:
                r = mid
            # Else, increase eating speed
            else:
                l = mid + 1
        # Has the least eating speed within h hours
        return r