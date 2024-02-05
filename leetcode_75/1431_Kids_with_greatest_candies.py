"""
1431. Kids with greatest candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
There are n kids with candies and you have a few extraCandies. You already know how many candies each kid has.
Return an array of size n, where for each kid, mark True if after giving extraCandies to that kid, they will have 
the greatest numnber of candies. Multiple kids can have greatest number of candies.

Final algorithm followed:
1. Initialize result array of size n with all False values.
2. Note down current the max candies.
2. Iterate through all the kids, give them extraCandies and see if they'd have >= current max candies
    a. If yes, mark that kid as True in your result array
    b. Else keep moving
3. Return result
"""
# Solution with comments
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        dup_candies = candies.copy()
        # Sort candies in O(log n) time and get max candies value
        dup_candies.sort()
        max_c = dup_candies[len(candies)-1]
        # Go through all kids and give them extra candies
        # See if they will have >= max candies
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_c:
                result[i] = True
        return result