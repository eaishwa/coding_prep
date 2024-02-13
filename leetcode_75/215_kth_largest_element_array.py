"""
215. Kth largest element in an array
https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75
What is the question?
Given an unsorted array, find kth largest element without using sort algorithms.

Final algorithm followed:
1. Use min heap and always maintain only top k largest elements in the array
2. After processing all the elements, return the root of min heap.

Summary of common mistakes/tricks:
Something that exceeds time limit is to find max value of array k times, each time removing the max element in the array.
"""
# Solution with comments
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time limit exceeded
        # Go through array k times
        # Determine the largest element each time
        # delete it from the array
        # O(n*k) runtime
        # Another approach is to sort it on O(nlogn) time.

        # Min heap always maintains min ele in root
        # Push upto k elements in the min heap
        # From the K+1th element, insert it and then pop the min element
        # This means you are only maintaining the top k largest elements in the heap
        # Maintain the size of the heap to be k
        # root of the heap will be the kth largest element
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]