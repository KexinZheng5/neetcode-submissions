import heapq as heap
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []

        for i in range(len(nums)):
            heap.heappush(h, (-nums[i], i))
            if i >= k-1:
                while h[0][1] < i - k + 1:
                    heap.heappop(h)
                res.append(-h[0][0])

        return res