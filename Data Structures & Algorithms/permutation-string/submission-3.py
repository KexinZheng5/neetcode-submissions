class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        count1 = [0] * 26
        count2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        while r < len(s2):
            ind = ord(s2[r]) - ord('a')
            if count1[ind] == 0:
                count2 = [0] * 26
                r += 1
                l = r
            elif count1[ind] - count2[ind] > 0:
                count2[ind] += 1
                r += 1
                if r - l == len(s1):
                    return True
            else:
                while l <= r:
                    if s2[l] == s2[r]:
                        l += 1
                        break
                    count2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
                r += 1
            #print(l, r)
                
        return False

                        
                        
