class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        
        current = 2
        prev = 1
        
        for i in range(3, n+1):  
            temp = current
            current += prev
            prev = temp

        return current
            
