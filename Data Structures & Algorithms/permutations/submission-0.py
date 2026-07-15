class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        res = []
        for p in permutations:
            for i in range(len(p) + 1):
                copy_p = p.copy()
                copy_p.insert(i, nums[0])
                res.append(copy_p)
            
        return res
            

        