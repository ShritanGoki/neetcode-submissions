class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, count in count.items():
            freq[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                if k>0:
                    result.append(num)
                    k -= 1
                else:
                    return result
        
        return result

            

