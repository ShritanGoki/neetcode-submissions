class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range (len(nums)):
            if (nums[i] > 0):
                break
            
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l = i+1
            r = len(nums) -1

            while (l<r):
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while (l<r) and  nums[l-1] == nums[l]:
                        l += 1
        return result