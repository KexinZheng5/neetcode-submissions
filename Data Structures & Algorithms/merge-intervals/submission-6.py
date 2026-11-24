class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # bucket sort
        starts = [-1] * 1001
        res = []

        for s, e in intervals:
            starts[s] = max(starts[s], e)
        
        cur = None
        s = 0
        while s < 1001:
            if cur:
                if s <= cur[1]:
                    cur[1] = max(cur[1], starts[s])
                else:
                    res.append(cur)
                    cur = [s, starts[s]] if starts[s] != -1 else None
            elif starts[s] > -1:
                cur = [s, starts[s]]
            s += 1
        
        if cur:
            res.append(cur)
        
        return res
