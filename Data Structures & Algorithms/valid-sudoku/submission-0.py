class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    n = board[i][j]
                    if n in row[i] or n in col[j] or n in square[(i // 3) * 3 + j // 3]:
                        return False
                    row[i].add(n)
                    col[j].add(n)
                    square[(i // 3) * 3 + j // 3].add(n)
        
        return True