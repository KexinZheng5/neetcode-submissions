class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countt = {} # count of characters in t
        counts = {} # count of characters in substr of s

        for c in t:
            countt[c] = countt.get(c, 0) + 1

        l, r = 0, 0
        res = ""
        match = 0

        while r < len(s):
            if countt.get(s[r], 0) > counts.get(s[r], 0):
                counts[s[r]] = counts.get(s[r], 0) + 1
                match += 1
                # matching substring
                if match == len(t):
                    # try shortening the substring
                    while l <= r:
                        #print(s[l], counts[s[l]])
                        if counts[s[l]] > countt.get(s[l], 0):
                            counts[s[l]] -= 1
                            l += 1
                        else:
                            break
                    if res == "" or len(res) > len(s[l:r+1]):
                        res = s[l:r+1]
                    counts[s[l]] -= 1
                    l += 1
                    match -= 1
            else:
                counts[s[r]] = counts.get(s[r], 0) + 1
            r += 1
        
        return res