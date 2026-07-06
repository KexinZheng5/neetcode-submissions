class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for s in s1:
            d.setdefault(s, 0)
            d[s] += 1
        
        l = 0
        r = 0

        while r < len(s2):
            if s2[r] not in d:
                while l < r:
                    d[s2[l]] += 1
                    l += 1
                l = r + 1
            elif d[s2[r]] == 0:
                while l < r and s2[l] != s2[r]:
                    d[s2[l]] += 1
                    l += 1
                l += 1
            else:
                d[s2[r]] -= 1
                if r - l + 1 == len(s1):
                    return True
            r += 1
        
        return False