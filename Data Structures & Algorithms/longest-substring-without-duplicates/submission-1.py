class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        existed = set()
        while r < len(s):
            # repeated
            if s[r] in existed:
                # remove duplicate
                while s[r] in existed and l <= r:
                    existed.remove(s[l])
                    l += 1
            existed.add(s[r])
            r += 1
            res = max(res, r - l)
        
        return res