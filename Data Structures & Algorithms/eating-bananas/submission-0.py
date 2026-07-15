class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while (l<=r):
            k = int((l+r)/2)
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/k)
            if totalTime <= h:
                r = k - 1
                res = k
            else:
                l = k+1
        return res

        