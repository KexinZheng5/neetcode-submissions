# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        depth = {None : 0}
        while stack:
            node = stack[-1]
            if node.right and node.right not in depth:
                stack.append(node.right)
            elif node.left and node.left not in depth:
                stack.append(node.left)
            else:
                stack.pop()

                depth[node] = 1 + max(depth[node.left], depth[node.right])

                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
        
        return abs(depth[root.left] - depth[root.right]) < 2
            
                