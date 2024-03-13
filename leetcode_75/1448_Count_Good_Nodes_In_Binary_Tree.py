"""
1448. Count Good Nodes in a Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Good nodes are those that did not have a node greater than it in the path from root. Count such nodes.

Final algorithm followed:
1. Use DFS, track max node val along the path
2. When you encounter good node, count it and update max node val
3. Search left and right subtrees

Summary of common mistakes/tricks:
"""
# Solution with comments
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        # Use dfs as you wanna trace a path from root to each node
        # maintain the max node value at every stage
        def dfs(node, maxx):
            if not node:
                return
            # if you encounter a good node, increment good and update maxx
            elif node.val >= maxx:
                self.good+=1
                maxx = node.val
            # search left
            dfs(node.left, maxx)
            # search right
            dfs(node.right, maxx)

        dfs(root,root.val)
        return self.good