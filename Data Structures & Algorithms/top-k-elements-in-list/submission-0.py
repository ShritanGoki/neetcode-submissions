class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countList = {}
        countOrder = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            countList[i] = 1 + countList.get(i, 0)
        for i, x in countList.items():
            countOrder[x].append(i)

        result = []
        for i in range(len(countOrder) - 1, 0, -1):
            for n in countOrder[i]:
                result.append(n)
                if len(result) == k:
                    return result

