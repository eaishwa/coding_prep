"""
1456. Maximum Number of Vowels in a Substring with given length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given a string and length k, find max number of vowels in substring of length k.

Final algorithm followed:
1. Initialize num vowels in the first k letter substring
2. For every additional step you take count vowels in O(1) time by checking prev last and curr last letter
3. Keep maintaining the answer

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        # Initialize
        hm = Counter(s[:k])
        ans = sum(hm[key] for key in vowels)
        
        curr = ans
        for i in range(1, len(s)-k+1):
            # check if prev first letter was a vowel
            if s[i-1] in vowels:
                if s[i+k-1] not in vowels:
                    curr -= 1
            else:
                if s[i+k-1] in vowels:
                    curr += 1
            ans = max(ans, curr)

        return ans