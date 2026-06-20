class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        count = ""
        temp = ""
        for c in s:
            if isinstance(count, str):
                if c == "#":
                    count = int(count)
                    if count == 0:
                        res.append("")
                        count = ""
                else:
                    count += c
            else:
                temp += c
                count -= 1
                if count == 0:
                    res.append(temp)
                    count = ""
                    temp = ""

        return res