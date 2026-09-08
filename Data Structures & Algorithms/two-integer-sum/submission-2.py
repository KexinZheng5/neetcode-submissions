class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in indices:
                return [indices[n], i]
            indices[nums[i]] = i
            