class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxf = 0
        res = 0

        counter = {}

        while r < len(s):
            # update counter
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(counter[s[r]], maxf)

            while (r-l+1) - maxf > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res