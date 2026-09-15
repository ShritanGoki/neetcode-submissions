class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            place = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = place
        
        return rob2



