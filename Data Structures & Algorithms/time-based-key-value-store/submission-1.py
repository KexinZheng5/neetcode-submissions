class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, [])
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        l, r = 0, len(self.d[key]) - 1
        while l <= r:
            m = (l+r) // 2
            if timestamp == self.d[key][m][0]:
                return self.d[key][m][1]
            elif timestamp > self.d[key][m][0]:
                l = m + 1
            else:
                r = m - 1
        
        if self.d[key][r][0] < timestamp:
            return self.d[key][r][1]
        return ""