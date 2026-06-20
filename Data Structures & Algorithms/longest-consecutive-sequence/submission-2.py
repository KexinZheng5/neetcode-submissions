from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0

        for n in nums:
            if not count[n]:
                count[n] = count[n-1] + count[n+1] + 1
                count[n - count[n-1]] = count[n]
                count[n + count[n+1]] = count[n]
                res = max(count[n], res)
        
        return res