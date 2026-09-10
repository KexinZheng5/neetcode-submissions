"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # double dfs for original and cloned graph
        # branching / adding children from the parent's end 
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old_to_new[cur].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]