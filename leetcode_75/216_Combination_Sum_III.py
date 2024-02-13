"""
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Find all valid combinations of k numbers that sum up to n such that the numbers through 1 and 9 are used and no repetitions allowed on the combo.

Final algorithm followed:
1. Frame a function that takes in intermediate result + any other info needed for logic inside. Remember you are processing one combo at a time!
2. Write satisfying conditions and append to results.
3. Write non satisfying conditions to stop and return.
4. For loop on the pool of eligible elements, recurse with each candidate and backtrack!!

Summary of common mistakes/tricks:
Remember to stop and return when encountering non satisfying conditions.
"""
# Solution with comments
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        def comb(remaining, cand, next):
            # if we've found a satisfying candidate, append to results
            if remaining == 0 and len(cand) == k:
                result.append(list(cand))
            # if we did not find one and surpassed constraints, return
            elif remaining < 0 or len(cand) == k:
                return
            # for pool of eligible elements to choose for my combination
            for idx in range(next,10):
                # choose one
                cand.append(idx)
                # recurse to see if this is good enough
                comb(remaining-idx, cand, idx+1)
                # pop out recent element added as it is done processing
                cand.pop()

        comb(n, [], 1)
        return result