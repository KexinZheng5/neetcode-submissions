class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # land found
                if grid[i][j] == '1':
                    # perform dfs until reaching water
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = '0'
                        for d in directions:
                            new_x = x + d[0]
                            new_y = y + d[1]
                            if new_x > -1 and new_y > -1 \
                            and new_x < len(grid) and new_y < len(grid[0]) \
                            and grid[new_x][new_y] == '1':
                                stack.append((new_x, new_y))
                    count += 1
        
        return count