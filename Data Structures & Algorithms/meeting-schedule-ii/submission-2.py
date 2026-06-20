"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        starts = []
        ends = []

        for event in intervals:
            starts.append(event.start)
            ends.append(event.end)
        
        starts.sort()
        ends.sort()

        i = 0
        j = 0
        active = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                active += 1
                i += 1
            else:
                active -= 1
                j += 1
            count = max(active, count)

        return count
