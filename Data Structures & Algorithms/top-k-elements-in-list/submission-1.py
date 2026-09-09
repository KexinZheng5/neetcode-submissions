class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of frequency -> hashtable
        # sort the frequency -> bucket sort
        count = {}
        bucket = [[] for i in range(len(nums))]

        for n in nums:
            count.setdefault(n, 0)
            count[n] += 1
        for n in count.keys():
            bucket[count[n]-1].append(n)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res