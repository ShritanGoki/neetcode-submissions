class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range (len(nums)):
            s.add(nums[i])
        if len(s) == len(nums):
            return False
        return True
                    