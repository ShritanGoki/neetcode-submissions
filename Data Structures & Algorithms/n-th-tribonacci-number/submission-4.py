class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0

        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(3, n+1):
            place = t2
            t2 += t1+t0
            t0 = t1
            t1 = place
        
        return t2