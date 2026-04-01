class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r_lim = len(grid)
        c_lim = len(grid[0])
        count = 0
        #implement DFS solution
        def dfs(a, b):
            
            if a >= r_lim or b >= c_lim or a < 0 or b < 0 or grid[a][b] == "0":
                return

            grid[a][b] = "0"

            dfs(a, b+1)
            dfs(a, b-1)
            dfs(a-1, b)
            dfs(a+1, b)
        
        
        for r in range(len(grid)):

            for c in range(len(grid[0])):

                node = grid[r][c]
                if node == "1":
                    count += 1
                    dfs(r, c)

        return count


        