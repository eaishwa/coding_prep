"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given equations, values and queries in array format with variables. Evaluate the answer for the queries.

Final algorithm followed:
1. The intuition is to keep variables as nodes and weights of edges as values in graph. Rever direction values to be stored as reciprocals.
2. Traverse the graph from source to destination node, multiplying weights in the fwd direction along the way.
3. Create adj list with both direction info in from the equations and values.
4. Traverse from src to dest, using dfs, however handle backtracking correctly.

Summary of common mistakes/tricks:
A common mistake is to keep only one variable for the answer and not having the indicator variable.
The indicator variable helps stop when we have found the answer, otherwise we keep going on and on returning wrong answers!
"""
# Solution with comments
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        # create an adj list capturing both directions
        for i in range(len(equations)):
            num, den = equations[i][0], equations[i][1]
            if num not in adj:
                adj[num] = [(den, values[i])]
            elif num in adj:
                adj[num].append((den, values[i]))
            
            if den not in adj:
                adj[den] = [(num, 1/values[i])]
            elif den in adj:
                adj[den].append((num, 1/values[i]))
    
        answers = []
        
        def traverse(curr, dest, adj, visited, ans):
            # add curr node to visited
            visited.add(curr)
            # use this indicator variable to know if we reached answer
            ret = -1
            # for all neighbors of curr node
            for n in adj[curr]:
                # if we spot the destination node, return answer
                if n[0] == dest:
                    return ans * n[1]
                else:
                    # if node not visited yet
                    if n[0] not in visited:
                        # traverse from this neighbor to destination
                        ret = traverse(n[0], dest, adj, visited, ans * n[1])
                        # if answer is found, stop traversal and return answer
                        if ret != -1:
                            break
            return ret
# For each query, traverse from source and keep multiplying the weights until you reach destination
        for q in queries:
            # address base cases
            if q[0] not in adj or q[1] not in adj:
                answers.append(-1)
            elif q[0] == q[1]:
                answers.append(1)
            else:
                visited = set()
                answers.append(traverse(q[0], q[1], adj, visited, 1))
        return answers