class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        prev = None

        print(nums)
        res = []
        while i < len(nums) - 2:
            if nums[i] == prev:
                i += 1
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        temp = nums[l]
                        while l < r and nums[l] == temp:
                            l += 1
                    elif total < 0:
                        l += 1
                    else:
                        r -= 1
                prev = nums[i]
                i += 1
        
        return res