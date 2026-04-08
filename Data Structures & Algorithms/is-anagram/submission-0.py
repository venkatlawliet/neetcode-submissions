class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st=Counter(s)
        tt=Counter(t)
        if st==tt:
            return True
        return False

