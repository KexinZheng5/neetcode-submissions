class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        square = [0] * 9

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    n = int(board[i][j]) - 1
                    if (1 << n) & row[i] or (1 << n) & col[j] or (1 << n) & square[(i // 3) * 3 + j // 3]:
                        return False
                    row[i] |= (1 << n)
                    col[j] |= (1 << n)
                    square[(i // 3) * 3 + j // 3] |= (1 << n)
        
        return True