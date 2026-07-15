class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                placeholder = stack.pop()
                stack.append(stack.pop() - placeholder)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                placeholder = stack.pop()
                stack.append(int(stack.pop() / placeholder))
            else:
                stack.append(int(i))
        return stack[-1]