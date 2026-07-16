class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {"(":")", "{":"}", "[":"]"}

        for c in s:
            if c in paren:
                stack.append(c)
            else:
                if stack and paren[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack

        
        