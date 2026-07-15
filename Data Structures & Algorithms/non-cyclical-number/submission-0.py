class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        #could also use slow and fast points really simple implementation dont care tho
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

        

    def sumOfSquares(self, n: int) -> int:
        sumN = 0
        while n:
            sumN += (n % 10) ** 2
            n = n // 10

        return sumN
