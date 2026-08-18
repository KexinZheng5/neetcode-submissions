# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, minimum, maximum = q.popleft()
            if node.val >= maximum or node.val <= minimum:
                return False
            if node.right:
                q.append((node.right, node.val, maximum))
            if node.left:
                q.append((node.left, minimum, node.val))
            
        return True