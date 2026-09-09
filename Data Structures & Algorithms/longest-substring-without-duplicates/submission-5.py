class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        last_ind = {}

        for r in range(len(s)):
            # repeated
            if s[r] in last_ind:
                # remove duplicate
                l = max(last_ind[s[r]] + 1, l)
            last_ind[s[r]] = r
            res = max(res, r - l + 1)
        
        return res