# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            nodes = stack.pop()
            if nodes[0] and nodes[1]:
                if nodes[0].val != nodes[1].val:
                    return False
                stack.append((nodes[0].left, nodes[1].left))
                stack.append((nodes[0].right, nodes[1].right))
            else:
                if nodes[0] or nodes[1]:
                    return False

        return True