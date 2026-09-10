class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        sums = {0 : 1}
        res = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            res += sums.get(cur_sum - k, 0)
            sums.setdefault(cur_sum, 0)
            sums[cur_sum] += 1

        return res