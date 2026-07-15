class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rown = len(matrix)
        coln = len(matrix[0])

        l,r = 0, rown*coln -1

        while (l<=r):
            m = l + ((r-l)//2)
            row = m//coln
            col = m%coln
            if(target<matrix[row][col]):
                r = m-1
            elif(target>matrix[row][col]):
                l = m+1
            elif (target==matrix[row][col]):
                return True
        return False 