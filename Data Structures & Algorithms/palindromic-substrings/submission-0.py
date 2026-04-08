class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if len(set(s))==n:
            return n
        count=0
        def df(l,r):
            nonlocal count
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        for i in range(n):
            df(i,i)
            df(i,i+1)
        return count
        