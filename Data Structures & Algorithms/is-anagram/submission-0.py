class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        freq1 = {}
        freq2 = {}
        if n != m:
            return False
        
        for i in range(n):
            freq1[s[i]] = freq1.get(s[i],0) + 1
        for j in range(m):
            freq2[t[j]] = freq2.get(t[j],0) + 1

        if freq1 == freq2:
            return True
        else:
            return False