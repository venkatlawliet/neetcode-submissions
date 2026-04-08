class Solution:
    def climbStairs(self, n: int) -> int:
        one, two=1,1
        for i in range(n-1):
            one,two=one+two,one
        return one
        arr=[-1]*(n+1)
        def df(node):
            if node ==n:
                return 1
            elif node>n:
                return 0
            elif arr[node]!=-1:
                return arr[node]
            return df(node+1)+df(node+2)
        return df(0)