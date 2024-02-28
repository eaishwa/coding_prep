"""
38. Count and Say
https://leetcode.com/problems/count-and-say/

What is the question?
Count and say is a sequence, for each step look at the CS(prev number) and form current CS. Given a number return its CS.

Final algorithm followed:
1. Use bottom up DP solution, with predetermined base case for 1.
2. Write down logic for counting and saying, using a nested for loop.
3. Keep storing results and return the right answer.

Summary of common mistakes/tricks:
Counting could be a little tricky!
"""
# Solution with comments
class Solution:
    def countAndSay(self, n: int) -> str:
        # Use bottom up DP solution
        # Initialize 1
        result = ['1']
        # For each number, look up previous number
        for i in range(n):
            # start with the first digit of prev number
            curr = result[i][0]
            # count it
            count = 1
            ans = ""
            # for each digit in prev number
            for j in result[i][1:]:
                # if it is same as prev digit, increment count
                if j == curr:
                    count += 1
                # when you encounter different digit
                else:
                    # put together your answer
                    ans = ans + str(count) + str(curr)
                    # reset current digit
                    curr = j
                    # count it
                    count = 1
            # you've arrived at the end of all digits, so finalize answer
            ans = ans + str(count) + str(curr)
            # append into result
            result.append(ans)
        # return answer for this question
        return result[n-1]