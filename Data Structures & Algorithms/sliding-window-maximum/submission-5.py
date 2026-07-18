class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()
        l = r = 0

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()
            
            if (r-l + 1) == k:
                result.append(nums[queue[0]])
                l += 1
            
            r+=1
        
        return result
            
            


