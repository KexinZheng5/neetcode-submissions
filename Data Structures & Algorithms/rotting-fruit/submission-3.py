class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting = set()
        fresh = 0
        day = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotting.add((i, j))

        while rotting and fresh > 0:
            cur_rotting = set()
            for i, j in rotting:
                for d in directions:
                    x, y = i + d[0], j + d[1]

                    if x > -1 and y > -1 \
                    and x < len(grid) and y < len(grid[0]) \
                    and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        cur_rotting.add((x, y))
            rotting = cur_rotting
            day += 1
        
        return day if fresh == 0 else -1
        

