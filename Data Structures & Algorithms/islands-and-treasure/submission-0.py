class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        prev = []
        count = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    prev.append((i+1,j))
                    prev.append((i-1,j))
                    prev.append((i,j+1))
                    prev.append((i,j-1))

        while prev:
            cur = []
            for i, j in prev:
                # validate index
                if i > -1 and j > -1 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 2147483647:
                    grid[i][j] = count
                    cur.append((i+1,j))
                    cur.append((i-1,j))
                    cur.append((i,j+1))
                    cur.append((i,j-1))
            count += 1
            prev = cur