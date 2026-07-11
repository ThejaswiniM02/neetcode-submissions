class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = []
        for s in strs:
            n = str(len(s))
            new_string.append(n + "#"+ s)
        return "".join(new_string)
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                l = int(s[i:j])
            i = j+1
            st = s[i:i+l]
            ans.append(st)
            i = i + l
        return ans

