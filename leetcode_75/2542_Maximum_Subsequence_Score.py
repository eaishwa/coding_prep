"""
2542. Maximum Subsequence Score
https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Read the link

Final algorithm followed:
1. Sort the arrays based on nums2 desc order.
2. Fix the min idx of nums2, maintain k-1 largest elements of nums1 in min heap
3. Track the answer for each fixed min idx and return the max answer.

Summary of common mistakes/tricks:
A common mistake is to not consider max k-1 elements but keep a fixed window of k elements moving as you iterate through min idx.
"""
# Solution with comments
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sort the 2 arrays based on 2nd array desc order, store them as pairs
        # start from kth pair, everytime assuming the corresponding nums2 to be the min idx
        # put all k-1 nums1 elements into a min heap
        # every time you move the min idx element, pop from heap and push current nums1 element to heap
        # We always maintain largest k-1 elements in the min heap + the kth element which is fixed for each iteration

        pairs = [(a,b) for a,b in zip(nums1,nums2)]
        pairs.sort(key=lambda x: -x[1])
        min_ptr = k-1
        heap = []
        heap_sum = 0

        for i in range(k):
            heapq.heappush(heap, pairs[i][0])
            heap_sum += pairs[i][0]
        
        ans = heap_sum * pairs[min_ptr][1]

        for i in range(min_ptr+1, len(pairs)):
            heap_sum -= heapq.heappop(heap)
            # fixed kth element
            heapq.heappush(heap, pairs[i][0])
            heap_sum += pairs[i][0]
            ans = max(ans, heap_sum * pairs[i][1])
        
        return ans