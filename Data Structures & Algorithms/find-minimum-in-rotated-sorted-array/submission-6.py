class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            ln = m-1 if m-1 > -1 else len(nums) - 1
            rn = m+1 if m+1 < len(nums) else 0

            if nums[m] < nums[rn] and nums[m] < nums[ln]:
                return nums[m]
            elif nums[l] < nums[r] or nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        
        return nums[r]