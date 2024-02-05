"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Words in a sequence are separated by at least a space. Return the sequence with words reversed!

Final algorithm followed:
1. Split sequence by space.
2. Traverse from the end of the list and construct the output sequence
Space Complexity: O(n), Time Complexity: O(n)

"""
# Solution with comments
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        ans = ""

        for i in range(len(words)-1,-1,-1):
            ans = ans + words[i].strip() + " "
        
        return ans.strip()