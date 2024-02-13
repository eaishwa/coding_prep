"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given a string of digits, return all combinations of strings that could be formed from those digits.

Final algorithm followed:
1. The intuition is to form one combination at a time, append it to result when the combination is ready
2. Process one idx at a time in your input digit.
3. When a combo is done, append it to results.
4. Otherwise, read the next digit letters and append it to element one by one and each time check if you have valid ans.
5. Pop the top most letter in the end to make way for another letter in the for loop.

Summary of common mistakes/tricks:
Framing the function for recursion is the crux, remember to process one combo at a time.
"""
# Solution with comments
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz'}
        
        # The intuition is to form one combination at a time, append it to result when the combination is ready
        # Process one idx at a time in your input digit.
        # When a combo is done, append it to results.
        # Otherwise, read the next digit letters and append it to element one by one and each time check if you have valid ans.
        # Pop the top most letter in the end to make way for another letter in the for loop.
        def comb(idx, element):
            if idx == len(digits):
                result.append(element)
                return
            else:
                letters = hm[int(digits[idx])]
                for l in letters:
                    element += l
                    comb(idx+1, element)
                    element = element[:-1]
    
        result = []
        comb(0, "")
        return [] if result == [""] else result