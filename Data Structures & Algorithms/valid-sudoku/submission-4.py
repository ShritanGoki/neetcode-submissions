class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        countColumn = defaultdict(set)
        countRow = defaultdict(set)
        countSquare = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in countColumn[c]:
                    return False
                if board[r][c] in countRow[r]:
                    return False
                
                if board[r][c] in countSquare[r//3, c//3]:
                    return False
                
                countColumn[c].add(board[r][c])
                countRow[r].add(board[r][c])
                countSquare[tuple([r//3, c//3])].add(board[r][c])
            
        return True

                