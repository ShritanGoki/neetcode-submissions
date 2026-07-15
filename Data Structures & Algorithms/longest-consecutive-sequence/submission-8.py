class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numbers = set(nums)

        for i in nums:
            if i-1 not in numbers:
                streak = 1
                while i + streak in numbers:
                    streak += 1
                longest = max(longest, streak)
        
        return longest

            



            

