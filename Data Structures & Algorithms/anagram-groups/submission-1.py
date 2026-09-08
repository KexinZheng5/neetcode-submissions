from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            # get string character count
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in d:
                res[d[count]].append(s)
            else:
                res.append([s])
                d[count] = len(res) - 1
        return res