class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_prefix = nums[0]
        prev_min = min(0, nums[0])
        res = nums[0]

        for i in range(1, len(nums)):
            cur_prefix = prev_prefix + nums[i]
            res = max(res, cur_prefix, cur_prefix - prev_min)
            prev_min = min(prev_min, cur_prefix)
            prev_prefix = cur_prefix
            #print(cur_prefix, prev_min)
        
        return res
