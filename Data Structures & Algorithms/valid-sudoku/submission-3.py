class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = defaultdict(set)
        row = defaultdict(set)
        column = defaultdict(set)

        for i in range (9):
            for j in range (9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in column[j]:
                    return False
                if board[i][j] in square[i//3, j//3]:
                    return False
                
                column[j].add(board[i][j])
                row[i].add(board[i][j])
                square[tuple([i//3, j//3])].add(board[i][j])
            
        return True
                
        