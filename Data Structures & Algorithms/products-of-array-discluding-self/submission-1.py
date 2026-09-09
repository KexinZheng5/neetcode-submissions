class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]

        # store prefix
        for i in range(1, len(nums)):
            res.append(nums[i-1] * res[i-1])

        # multiply by suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res