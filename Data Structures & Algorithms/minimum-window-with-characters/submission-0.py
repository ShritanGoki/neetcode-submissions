class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, shortest = [-1,1], float('inf')

        countNew = {}
        l = 0
        for r in range(len(s)):
            countNew[s[r]] = countNew.get(s[r], 0) + 1
            
            if countNew[s[r]] == countT.get(s[r], 0):
                have += 1
            
            while have == need:
                if (r-l+1) < shortest:
                    res = [l, r]
                    shortest = (r-l+1)
                countNew[s[l]] -= 1
                if countNew[s[l]] < countT.get(s[l], 0):
                    have -= 1
                l+= 1
            
        l, r = res
        return s[l:r+1] if shortest != float('inf') else ""

