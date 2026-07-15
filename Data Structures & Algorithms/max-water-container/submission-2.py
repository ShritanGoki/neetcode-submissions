class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1

        while (l<r):
            height = min(heights[l], heights[r])
            area = height * (r-l)
            largest = max(largest, area)
            if heights[l] > heights[r]:
                r -=1
            else:
                l += 1    

        return largest