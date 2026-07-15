class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, n, in enumerate(temperatures):
            while(stack and n>stack[-1][1]):
                index, temp = stack.pop()

                result[index] = i - index
            stack.append([i, n])
        return result