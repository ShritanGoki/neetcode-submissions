class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countList = {}
        ordered = [[] for i in range(len(nums) + 1)]

        for i in nums:
            countList[i] = 1 + countList.get(i,0)
        for i, n in countList.items():
            ordered[n].append(i)

        result = []
        for i in range(len(nums), 0, -1):
            for j in ordered[i]:
                result.append(j)
                if len(result) == k:
                    return result
            