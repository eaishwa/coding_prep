"""
2462. Total Cost to Hire K Workers
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given costs to hire workers, number of workers to hire and number of workers to consider in each session,
hire low cost worker in each session, return min cost.

Final algorithm followed:
1. Use 2 min heaps, for the first m workers and the last m workers
2. Keep popping from the low cost heap and add to heap if the ptrs haven't crossed each other.
3. Run the above k times.

Summary of common mistakes/tricks:
No need to exit the loop after 2 ptrs pass each other, just that you don't need to add them to heap anymore.
"""
# Solution with comments
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        # initialize ptrs to keep adding into heaps
        p1, p2 = candidates, n-1-candidates
        # initialize heaps
        h1, h2 = costs[:candidates], costs[max(candidates, n-candidates):]
        heapq.heapify(h1)
        heapq.heapify(h2)
        cost = 0

        for i in range(k):
            # if less cost worker is found in h1, hire them
            if not h2 or h1 and h1[0] <= h2[0]:
                cost += heapq.heappop(h1)
                # if p1 has not crossed p2, then push to the heap
                if p1 <= p2:
                    heapq.heappush(h1, costs[p1])
                    p1 += 1
            else:
                # if less cost worker is in h2, hire them
                cost += heapq.heappop(h2)
                # if p1 has not crossed p2, then push to heap
                if p1 <= p2:
                    heapq.heappush(h2, costs[p2])
                    p2 -= 1
        return cost