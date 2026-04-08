class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col=len(grid),len(grid[0])
        visited=set()
        island=0
        def df(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]=='0' or (r,c) in visited:
                return
            visited.add((r,c))
            df(r,c+1)
            df(r,c-1)
            df(r+1,c)
            df(r-1,c)
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visited:
                    df(r,c)
                    island+=1
        return island
        