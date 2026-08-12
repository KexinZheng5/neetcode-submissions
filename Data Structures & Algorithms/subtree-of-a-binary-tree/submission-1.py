# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def zfunc(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i < r:
                z[i] = min(r-i+1, z[i-l])
            while z[i] + i < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s_root = self.serialize(root)
        s_subroot = self.serialize(subRoot)
        full = s_subroot + "|" + s_root
        res = self.zfunc(full)
        sublen = len(s_subroot)

        for i in range(sublen + 1, len(full)):
            if res[i] == sublen:
                return True
        
        return False