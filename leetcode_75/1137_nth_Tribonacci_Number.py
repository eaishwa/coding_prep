"""
1137. Nth Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given n, return nth tribonacci number where Tn = Tn-3 + Tn-2 + Tn-1

Final algorithm followed:
1. Keep storing the Tribonacci numbers in an array until nth number.

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0,1,1]
        for i in range(3, n+1):
            trib.append(trib[i-3]+trib[i-2]+trib[i-1])
        return trib[n]