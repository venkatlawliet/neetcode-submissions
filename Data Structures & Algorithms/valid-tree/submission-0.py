class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        sofa={i:[] for i in range(n)}
        for k,v in edges:
            sofa[k].append(v)
            sofa[v].append(k)
        visited=set()
        def df(i):
            if i in visited:
                return
            visited.add(i)
            for j in sofa[i]:
                df(j)
        df(0)
        return len(visited)==n