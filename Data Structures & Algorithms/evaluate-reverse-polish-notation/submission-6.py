class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                temp = stack.pop()
                stack.append(stack.pop()-temp)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                temp = stack.pop()
                stack.append(int(stack.pop()/temp))
            else:
                stack.append(int(token))
        return stack.pop()