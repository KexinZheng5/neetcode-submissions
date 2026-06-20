class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - 97] += 1
            # Use tuple as key and convert values to list
            d.setdefault(tuple(key), []).append(s)
        
        return list(d.values())