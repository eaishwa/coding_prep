"""
1055. Shortest Way to Form String
https://leetcode.com/problems/shortest-way-to-form-string/description/

What is the question?
Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Final algorithm followed:
1. Expand your sliding window until the substring is a subsequence of source
2. Count the number of times you needed to split the target string
3. Cover the base case of mismatch in characters between the strings

Summary of common mistakes/tricks:
The above process is not an efficient solution, you could rather count the number of times you ran out of source and had to reset it when looking for subsequences.
"""
# Solution 1
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        def subseq(s,t):
            '''
            determines if s is a subseq of t
            '''
            i = 0
            for c in t:
                if c == s[i]:
                    i+=1
                    if i == len(s):
                        return True
            return False
            
        s = set(source)
        t = set(target)
        if s != t and len(s) <= len(t):
            return -1
        b,e = 0,0
        ans = 0
        # while we don't reach end of target
        while e < len(target):
            # while string upto current end is a subseq of source, expand
            while subseq(target[b:e+1], source) and e < len(target):
                e+=1
            # if not, you've reached the end of a substring, time to split
            ans +=1
            b = e
        return ans
# Solution 2 with comments
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        source_set = set(source)

        for char in target:
            if char not in source_set:
                return -1
        b,e = 0,0
        ans = 0
        while e < len(target):
            while source[b] != target[e]:
                b += 1
                if b >= len(source):
                    ans+=1
                    b = 0
            b += 1
            e += 1
            if e >= len(target) or b >= len(source):
                ans += 1
                b = 0
        return ans