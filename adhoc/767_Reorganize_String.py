"""
767. Reorganize String
https://leetcode.com/problems/reorganize-string/description/

What is the question?
Reorganize string such that no 2 chars are adjacent each other

Final algorithm followed:
1. Fill most freq chars first, fill the rest greedily

Summary of common mistakes/tricks:
"""
# Solution with comments
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Know the composition of the string along with character freq
        # know the max freq char and the freq itself
        ctr = Counter(s)
        max_ct, letter = 0, ''
        for k,v in ctr.items():
            if v > max_ct:
                letter = k
                max_ct = v
            if v > (len(s)+1) / 2:
                return ""

        output = ['']*len(s)
        idx = 0
        # fill the max freq char first
        while max_ct != 0:
            output[idx] = letter
            idx += 2
            max_ct -= 1
            ctr[letter] -= 1
        # fill in the rest, once idx go past len(s), bring it back to 1
        for k,v in ctr.items():
            while v > 0:
                if idx >= len(s):
                    idx = 1
                output[idx] = k
                idx += 2
                v -= 1
        return ''.join(output)