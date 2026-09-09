class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        last_ind = {}
        while r < len(s):
            # repeated
            if s[r] in last_ind:
                # remove duplicate
                l = max(last_ind[s[r]] + 1, l)
            last_ind[s[r]] = r
            r += 1
            res = max(res, r - l)
        
        return res