"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Final algorithm followed:
1. Eliminate the condition when GCD can't exist
    if str1 + str2 != str2 + str1, then GCD can't exist! That's a brilliant condition that doesn't strike easily.
2. Find the mathematical gcd of the lengths of both the strings and the substring of length GCD.
Space complexity - O(1), Time Complexity - O(n)

Summary of common mistakes/tricks:
Common mistake is to use a 2 ptr approach and iterate through both strings until the letter are equal and the first letter repeats.
Before that, checking if unique letters in both words are equal can also be done as an early check. The gotcha with this approach is
that, it assumes that the substring identified satisfies the divisibility criteria discussed in this question.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(l1,l2)]

"""
Solution 2:
1. The answer should be part of the smaller string, so find the smaller string.
2. Iterate through the smaller string length, each time shrinking the size by 1.
3. Verify if the length considered above (k) gives a valid GCD.
4. To be a valid GCD -
    a. k should be divisible by both string lengths.
    b. we should be able to reconstruct both the strings by making the substring of length k repeat l1/k and l2/k times respectively.
5. Return at once when you find a valid length.
"""
# Solution 2 with comments
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        # function to determine if k is a valid GCD length
        def valid(k):
            # if l1 and l2 are not divible by k, it is not a valid GCD length
            if l1 % k or l2 % k:
                return False
            # Get the repeat factor to multiply GCD string by, for both strings
            n1, n2 = l1 // k , l2 // k
            base = str1[:k]
            # Check if repetition criterion for GCD is met
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(l1,l2),0,-1):
            if valid(i):
                return str1[:i]
        return ""