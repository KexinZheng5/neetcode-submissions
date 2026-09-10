class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_prefix = 0
        sums = {}
        res = 0

        for i in range(len(nums)):
            # calculate current prefix sum
            cur_prefix = nums[i] + prev_prefix

            #print(cur_prefix, sums)
            # check for previous submatrix that can be reduced to equal to k
            if cur_prefix - k in sums:
                res += sums[cur_prefix - k]
            if cur_prefix == k:
                res += 1

            # update
            sums.setdefault(cur_prefix, 0)
            sums[cur_prefix] += 1
            prev_prefix = cur_prefix

        return res