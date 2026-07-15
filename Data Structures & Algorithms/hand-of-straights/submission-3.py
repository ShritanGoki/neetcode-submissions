class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for i in hand:
            count[i] = count.get(i, 0) + 1

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for i in range (start, start + groupSize):
                if i not in minH:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True




        

