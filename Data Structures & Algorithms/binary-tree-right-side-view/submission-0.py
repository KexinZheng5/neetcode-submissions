# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightNode = None
            lenq = len(q)

            for i in range(lenq):
                temp = q.popleft()
                if temp:
                    if not rightNode:
                        rightNode = temp
                    q.append(temp.right)
                    q.append(temp.left)
            
            if rightNode:
                res.append(rightNode.val)
        return res