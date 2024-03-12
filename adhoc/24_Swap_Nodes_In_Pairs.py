"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/description/

What is the question?
Swap nodes in linked list in place.

Final algorithm followed:
1. 3 ptr approach to seal all the links!

Summary of common mistakes/tricks:
Do not go into weeds, just focus on how to seal the links.
"""
# Solution with comments
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # travel in pairs to keep swapping nodes
        # what is hard here is to know that when we swap A and B,
        # we need to link B back to the node prior to A
        # start with a dummy before the head
        # have 2 ptrs pointing to first and second nodes
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            fnode, snode = head, head.next
            # link 2nd node to the prior node of previous pair
            prev_node.next = snode
            # link fnode to its swapped next
            fnode.next = snode.next
            # link snode to fnode and complete the swap
            snode.next = fnode

            # fnode is gonna be the prior node to the next pair
            prev_node = fnode
            # fnode.next is the next pair's first node
            head = fnode.next
        return dummy.next