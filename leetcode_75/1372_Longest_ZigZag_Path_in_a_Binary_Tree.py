"""
1372. Longest ZigZag path in a binary tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given a binary tree, find the longest zigzag path in it!

Final algorithm followed:
1. Use a single dfs to compute all path sizes.
2. You anyway visit every node, when you do so, start a new path from that node as well

Summary of common mistakes/tricks:
Having 2 dfs and not knowing how to use one dfs for it
"""
# Solution with comments
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        # maintain node, current_direction and num_paths
        def zigzag(node, curr_dir, num_paths):
            # if valid node, update answer
            if node:
                self.ans = max(self.ans, num_paths)
                # move in curr_dir with 1 additional num_nodes
                # and move in another direction with a brand new path 
                if curr_dir == 'left':
                    zigzag(node.left, 'right', num_paths+1)
                    zigzag(node.right, 'left', 0)
                else:
                    zigzag(node.right, 'left', num_paths+1)
                    zigzag(node.left, 'right', 0)
    
        zigzag(root, 'left', 0)
        zigzag(root, 'right', 0)
        return self.ans