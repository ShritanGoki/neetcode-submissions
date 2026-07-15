class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in pair:
                if stack and pair[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
        
        