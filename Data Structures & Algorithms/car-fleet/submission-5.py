class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered = [[p,s] for p,s in zip(position, speed)]
        ordered.sort(reverse = True)
        stack = []

        for p, s in ordered:
            time = (target - p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)
                


