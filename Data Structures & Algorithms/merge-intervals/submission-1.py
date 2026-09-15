class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        
        while i < len(intervals):
            start_i, end_i = intervals[i]
            i += 1
            while i < len(intervals) and intervals[i][0] <= end_i:
                end_i = max(end_i, intervals[i][1])
                i += 1
            res.append([start_i, end_i])
        
        return res