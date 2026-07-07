class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        d = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                q.append(s[i])
            elif len(q) == 0 or d[s[i]] != q.pop():
                return False
        
        return len(q) == 0
