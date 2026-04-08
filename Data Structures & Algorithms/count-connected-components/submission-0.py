class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        fill={i:[] for i in range(n)}
        count=0
        for i,j in edges:
            fill[i].append(j)
            fill[j].append(i)
        visited=set()
        def df(node):
            if node in visited:
                return
            visited.add(node)
            for j in fill[node]:
                df(j)
            
        for i in range(n):
            if i not in visited:
                count+=1
                df(i)
        return count
        