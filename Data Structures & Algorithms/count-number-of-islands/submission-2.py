class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r_lim = len(grid)
        c_lim = len(grid[0])
        count = 0
        #implement DFS solution
        def dfs(a, b, visited):
            
            if a >= r_lim or b >= c_lim or a < 0 or b < 0:
                return

            neighbours = [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]

            
            if (a, b) not in visited and grid[a][b] != "0" :
                grid[a][b] = "0"
                visited.add((a, b))
            else:
                return 
            
            for neighbour in neighbours:
                dfs(neighbour[0], neighbour[1], visited)
        
        
        for r in range(len(grid)):

            for c in range(len(grid[0])):

                node = grid[r][c]
                if node == "1":
                    count += 1
                    dfs(r, c, set())

        return count


        