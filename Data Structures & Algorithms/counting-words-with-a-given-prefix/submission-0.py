class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        length = len(pref)

        for w in words:
            if len(w) >= len(pref) and pref == w[:length]:
                count+=1
        
        return count
        