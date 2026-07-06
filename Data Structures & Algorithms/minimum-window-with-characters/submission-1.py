from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        match = 0
        res = ""

        d = Counter(t)

        while r < len(s):
            # character present
            if s[r] in d:
                if d[s[r]] > 0:
                    match += 1
                d[s[r]] -= 1
                r += 1
                # attempt to shink window if everything match
                if match == len(t):
                    #print(l, r)
                    while l < r:
                        print(l)
                        if s[l] in d:
                            if d[s[l]] == 0:
                                break
                            else: 
                                d[s[l]] += 1
                        l += 1
                    if len(res) == 0 or len(res) > r-l:
                        res = s[l:r]
            # no match
            else:
                if l == r:
                    l = r + 1
                r += 1
        
        return res