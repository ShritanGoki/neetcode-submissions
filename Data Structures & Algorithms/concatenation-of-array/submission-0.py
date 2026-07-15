class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length, length + length):
            nums.append(nums[i-length])
        
        return nums