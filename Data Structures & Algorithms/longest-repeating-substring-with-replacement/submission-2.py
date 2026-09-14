class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 1

        count = [0] * 26
        max_count = 0

        for r in range(len(s)):
            ind = ord(s[r]) - ord('A')
            count[ind] += 1
            max_count = max(max_count, count[ind])

            while r - l + 1 - max_count > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res