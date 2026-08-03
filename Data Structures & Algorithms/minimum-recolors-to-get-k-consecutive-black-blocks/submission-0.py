class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        for i in range(k):
            if blocks[i] == "W":
                countW += 1
        
        res = countW
        for i in range(k, len(blocks)):
            if blocks[i-k] == "W":
                countW-=1
            if blocks[i] == "W":
                countW+=1
            res = min(countW, res)
        
        return res