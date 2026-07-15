class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        countColumn = defaultdict(set)
        countRow = defaultdict(set)
        countSquare = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue

                if board[x][y] in countRow[x]:
                    return False
                else:
                    countRow[x].add(board[x][y])

                if board[x][y] in countColumn[y]:
                    return False
                else:
                    countColumn[y].add(board[x][y])
                
                if board[x][y] in countColumn[x//3, y//3]:
                    return False
                else:
                    countColumn[(tuple([x//3, y//3]))].add(board[x][y])

        return True