class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, b = 0, len(nums) - 1
        i = 0

        while i <= b:
            if nums[i] == 0:
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
                r += 1
            elif nums[i] == 2:
                temp = nums[b]
                nums[b] = nums[i]
                nums[i] = temp
                b -= 1
                i -= 1
            i += 1