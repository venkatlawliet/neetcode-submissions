class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS=len(heights),len(heights[0])
        rs,cs=set(),set()
        def df(r,c,visit,prevHeight):
            if ((r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or heights[r][c]<prevHeight):
                return
            visit.add((r,c))
            df(r-1,c,visit,heights[r][c])
            df(r+1,c,visit,heights[r][c])
            df(r,c-1,visit,heights[r][c])
            df(r,c+1,visit,heights[r][c])
        for c in range(COLS):      
            df(0,c,rs,heights[0][c])
            df(ROWS-1,c,cs,heights[ROWS-1][c])
        for r in range(ROWS):
            df(r,0,rs,heights[r][0])
            df(r,COLS-1,cs,heights[r][COLS-1])
        res=[]
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in rs and (i,j) in cs:
                    res.append([i,j])
        return res