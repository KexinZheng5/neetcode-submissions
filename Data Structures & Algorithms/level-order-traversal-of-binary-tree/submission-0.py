# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        prev = [root]
        cur = []
        res = []

        while prev:
            temp = []
            for node in prev:
                if node:
                    temp.append(node.val)
                    cur.append(node.left)
                    cur.append(node.right)
            if temp:
                res.append(temp)
            prev = cur
            cur = []
        
        return res