"""
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/description/

What is the question?
Find out if the graph is bipartite.

Final algorithm followed:
Check comments

Summary of common mistakes/tricks:

"""
# Solution with comments
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # start bfs from a node and assign a certain color to it
        # switch between 2 colors at each layer in the tree
        # if you encounter an adjacent node already belonging to current color, then graph is not bipartite
        # run bfs for all nodes, as the graph is not guaranteed to be connected
        visited = {}
        def bfs(i):
            if i in visited:
                return True
            que = [i]
            visited[i] = 1
            while que:
                node = que.pop()
                curr_color = visited[node]
                for child in graph[node]:
                    if child not in visited:
                        visited[child] = -curr_color
                        que.append(child)
                    elif visited[child] == curr_color:
                        return False
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True