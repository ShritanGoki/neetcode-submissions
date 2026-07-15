class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text2 > text1:
            text1, text2 = text2, text1
        prevRow = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            row = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    row[j] = 1 + prevRow[j-1]
                else:
                    row[j] = max(row[j-1], prevRow[j])
            prevRow = row
                
        return row[-1]
                
                    



         