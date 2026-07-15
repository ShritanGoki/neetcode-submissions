class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for i in numbers:
            if(i - 1) not in numbers:
                result = 1
                while ((i + 1) in numbers):
                    result +=1
                    i+=1
                if result > longest:
                    longest = result
        return longest  
            

