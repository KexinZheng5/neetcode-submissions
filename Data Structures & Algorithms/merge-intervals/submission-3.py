class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # greedy approach - works for small begining interval boundary ONLY! (otherwise too expensive)
        max_start = max(s for s, _ in intervals)
        mp = [0] * (max_start + 1)
        res = []

        for s, e in intervals:
            mp[s] = max(mp[s], e + 1)
        
        i = 0
        cur_interval = None

        while i < len(mp):
            if mp[i] > 0:
                # new interval - initiation
                if not cur_interval:
                    cur_interval = [i, mp[i]]
                # merge
                elif cur_interval[1] > i:
                    cur_interval[1] = max(cur_interval[1], mp[i])
                else:
                    res.append([cur_interval[0], cur_interval[1]-1])
                    cur_interval = [i, mp[i]]
            i += 1

        if cur_interval:
            res.append([cur_interval[0], cur_interval[1]-1])

        return res