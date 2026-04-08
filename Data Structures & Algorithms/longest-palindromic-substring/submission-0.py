class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        cont=0
        def check(l,r):
            nonlocal res, cont
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>cont:
                    res=s[l:r+1]
                    cont=(r-l)+1
                l-=1
                r+=1
        for i in range(len(s)):
            check(i,i)
        for i in range(len(s)):
            check(i,i+1)
        return res