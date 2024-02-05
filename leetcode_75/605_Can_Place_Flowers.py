"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
You have a long flowerbed where plants are potted. You cannot have two pots adjacent to each other.
You are give n new plants to pot, return True if you can pot all of them, else False.

Final algorithm followed:
1. Address base cases. Use greedy approach of planting whenever you find a valid spot.
2. Iterate through the flowerbed, check if there are plants to pot.
3. See if neighboring spots are free.
3. If yes, plant in the current spot by decreasing n by 1 and flipping flowerbed[i] to 1.
4. If no, keep moving until you reach the end of the flowerbed.
5. Address edge cases of first and last spot on the flowerbed inside your for loop.
Time Complexity - O(n), Space Complexity - O(n)

Summary of common mistakes/tricks:


Other resources / videos to help understand this question better: 
NA
"""
# Solution with comments
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans,i = 0,0
        # base cases
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n <= 1) or (n == 0):
                return True
            else:
                return False
        # Greedy approach, go through the flowerbed and plant when neighbors are free
        for i in range(len(flowerbed)):
            # If done with all plants, return True
            if n == 0:
                return True
            # if current spot is free
            if flowerbed[i] == 0:
                # if first or last spot and the neighbors are free
                if (i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i-1] == 0):
                    n = n-1
                    flowerbed[i] = 1
                # if not 1st or last spot
                else:
                    # if left and right neighbors are empty
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n = n-1
                        flowerbed[i] = 1
        # n might have gotten 0 and for loop condition could have gotten over
        # so check once again!
        return False if n!=0 else True