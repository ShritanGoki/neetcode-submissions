class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while (l<=r):
            speed = int((l+r)/2)
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p/speed))
            
            if totalTime <= h:
                r = speed - 1
                result = speed
            elif totalTime > h:
                l = speed + 1
        
        return result

