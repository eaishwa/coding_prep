"""
2300. Successful Pairs of Spells and Potions
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given spells, potions and success metric, for each spell find out how many potions will be successful (spell * potion >= success)

Final algorithm followed:
1. For each spell, find the least product >= success using binary search.

Summary of common mistakes/tricks:
Multiplying spell with all elements in potion is O(n) process, rather only multiply with spell when you make comparisons in binary search which is O(1).
"""
# Solution with comments
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        def bs(arr, s, n):
            l,r = 0, n-1
            while l <= r:
                mid = (l+r) // 2
                # Handle scenario when 0th idx is the answer
                if (mid == 0 and s*arr[mid] >= success) or (s*arr[mid] >= success and s*arr[mid-1] < success):
                    return n-mid
                elif s*arr[mid] < success:
                    l = mid + 1
                else:
                    r = mid - 1
            return 0

        for s in spells:
            pairs.append(bs(potions, s, len(potions)))

        return pairs