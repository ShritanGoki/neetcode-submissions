class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        output = [-1] * len(queries)

        for i in range(len(queries)):
            query = queries[i]
            minLen = float("inf")
            for interval in intervals:
                if query >= interval[0] and query<=interval[1]:
                    minLen = min(minLen, interval[1] - interval[0] + 1)
            if minLen != float("inf"):
                output[i] = minLen 
        
        return output
