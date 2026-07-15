class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, col = len(board), len(board[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r<0 or c<0 or 
                r>=rows or c>=col or
                board[r][c] != word[i]
                or (r,c) in path):
                return False

            path.add((r,c))
            i += 1
            res = dfs(r-1,c,i) or dfs(r,c-1,i) or dfs(r+1,c,i) or dfs(r,c+1,i)
            path.remove((r,c))

            return res
        
        for r in range(rows):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        
        return False
        
        

                
