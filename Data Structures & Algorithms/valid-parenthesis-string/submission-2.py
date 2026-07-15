class Solution:
    def checkValidString(self, s: str) -> bool:
        lowParen = 0
        highParen = 0

        for c in s:
            if c == "(":
                highParen += 1
                lowParen += 1
            
            if c == ")":
                highParen -= 1
                lowParen -= 1
            
            if c == "*":
                lowParen -= 1
                highParen += 1
            
            lowParen = max(0, lowParen)
            if highParen < 0:
                return False
            
        return lowParen == 0