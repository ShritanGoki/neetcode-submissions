class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countList = {}
        for num in nums:
            countList[num] = countList.get(num, 0) + 1
        
        frequency = [[] for _ in range(len(nums) + 1)]
        for num, count in countList.items():
            frequency[count].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in frequency[i]:
                if len(res) == k:
                    return res
                res.append(num)

        
        return res


