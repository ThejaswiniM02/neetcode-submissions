class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                freq1[s[i]] = freq1.get(s[i],0) + 1
            for j in range(len(t)):
                freq2[t[j]] = freq2.get(t[j],0) + 1
        
        if freq1 == freq2:
            return True
        else:
            return False