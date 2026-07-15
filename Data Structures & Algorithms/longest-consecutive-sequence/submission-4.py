class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in nums:
                result = 1
                while(i+result in numbers):
                    result += 1
                if longest < result:
                    longest = result
        return longest


        