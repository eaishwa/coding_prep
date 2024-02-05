"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given 2 strings, we gotta merge them by alternately choosing letters
from the words. If one string is longer than the other, then append 
the remaining letters as is to the answer.

Final algorithm followed:
1. Take a 2 pointer approach. Assign them initial values. Create answer string.
2. Move the pointers alternatively, as you keep appending the smaller pointer's letter to the output string.
3. When one of the pointers reach end of string, append the remaining letters of the other string to answer.
4. Return answer.
Space complexity - O(l1+l2), Time Complexity - O(l1+l2)

Summary of common mistakes/tricks:
1. Take care of initial assignment.
2. While loop condition should be "and", not "or".
3. Do not forget to append remaning letters of the lengthier string in the end.

Other resources / videos to help understand this question better: 
NA
"""
# Solution with comments
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 1. Initialize answer variable "ans" to first letter of word1
        ans = word1[0]
        # 2. Create two pointers, p1 points to letter idx 1 of word1, p2 points to letter idx 0 of word2.
        p1, p2 = 1, 0

        # 3. Iterate until either of the pointers reach the end of the word
        while p1 < len(word1) and p2 < len(word2):
            # 4. Append the letter of the smaller pointer to output and move it one step ahead to the next letter.
            if p2 < p1:
                ans += word2[p2]
                p2 += 1
            else:
                ans += word1[p1]
                p1 += 1
        # 5. One of the pointers have reached the end of word.
        # 6. Append the remaining letters of the word whose ptr has not reached the end of.
        if p1 >= len(word1):
            ans += word2[p2:]
        else:
            ans += word1[p1:]
        return ans