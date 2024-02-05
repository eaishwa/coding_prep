"""
443. String Compression
https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Final algorithm followed:
1. Initialize 2 ptrs i, j starting at the first letter of the string. Maintain an answer string.
2. Move j until new character is encountered, calculated number of old characters and append it to answer.
3. Move i to j and repeat step 2 until i reaches end of string.
4. Put the answer back into the original array and return length of it.
"""
# Solution with comments
class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j=0,0
        l = len(chars)
        if l==1:
            return 1
        s = ""
        while i < l:
            # loop until chars are same
            while j < l and chars[i] == chars[j]:
                j = j+1
            # when new char is encountered
            if j-i > 1:
                s = s + chars[i] + str(j-i)
            else:
                s = s + chars[i]
            i = j

        chars.clear()
        chars.extend(x for x in s)
        return len(s)