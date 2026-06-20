class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l, r = 0, 0
        length = 0

        while r < len(s):
            if s[r] not in count:
                count.add(s[r])
            else:
                length = max(length, r-l)
                while s[l] != s[r]:
                    count.remove(s[l])
                    l += 1
                l += 1
            r += 1
        
        return max(length, r-l)