# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque([(root, root.val)])

        while q:
            node, max_val = q.popleft()
            if node:
                if node.val >= max_val:
                    count += 1
                q.append((node.left, max(max_val, node.val)))
                q.append((node.right, max(max_val, node.val)))
        
        return count
