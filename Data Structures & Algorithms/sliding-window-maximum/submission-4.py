import heapq as heap
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i in range(k):
            heap.heappush_max(h, (nums[i], i))
        res = [heap.nlargest(1, h)[0][0]]

        for i in range(k, len(nums)):
            heap.heappush_max(h, (nums[i], i))
            while heap.nlargest(1, h)[0][1] < i - k + 1:
                heap.heappop_max(h)
            res.append(heap.nlargest(1, h)[0][0])

        return res