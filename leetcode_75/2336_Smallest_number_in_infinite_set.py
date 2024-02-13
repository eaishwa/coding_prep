"""
2336. Smallest number in Infinite Set
https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given an infinite set of positive numbers, implement popsmallest() and addback() methods.

Final algorithm followed:
1. Use minheap and a set to track what elements were added.

Summary of common mistakes/tricks:
Do not try to implement minheap, use out of box API and address the functions defined in the problem.
"""
# Solution with comments
class SmallestInfiniteSet:

    def __init__(self):
        self.minheap = []
        # contains elements that are in heap added explicitly again
        self.set = set()
        # denotes current top element
        self.curr_top = 1

    def popSmallest(self) -> int:
        # if minheap has elements, then we have the smallest element in this
        # this is because we add back element only when it is not present already
        # curr_top will be greater than minheap elements, hence this one takes precedence
        if len(self.minheap) > 0:
            self.set.remove(self.minheap[0])
            ans = heapq.heappop(self.minheap)            
        else:
            ans = self.curr_top
            self.curr_top += 1
        return ans


    def addBack(self, num: int) -> None:
        # Any element greater than curr_top or available in set is already in minheap
        if num >= self.curr_top or num in self.set:
            return
        self.set.add(num)
        heapq.heappush(self.minheap, num)