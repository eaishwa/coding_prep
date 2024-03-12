"""
1657. Determine if two strings are close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Read the question link directly!

Final algorithm followed:
1. Use Counters to store the words
2. Just check for equality in sorted keys and values

Summary of common mistakes/tricks:
Think about the conditions and do not always try brute force, street smart method is to use hashmaps.
"""
# Solution with comments
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Just check if they have the same common letters
        # and have equal number of occurrences of letters in general
        hm1 = Counter(word1)
        hm2 = Counter(word2)
        hm1_keys, hm1_vals = list(hm1.keys()), list(hm1.values())
        hm2_keys, hm2_vals = list(hm2.keys()), list(hm2.values())
        hm1_keys.sort()
        hm1_vals.sort()
        hm2_keys.sort()
        hm2_vals.sort()
        if hm1_keys == hm2_keys and hm1_vals == hm2_vals:
            return True
        return False