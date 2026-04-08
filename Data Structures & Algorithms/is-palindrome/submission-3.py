class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r"[\s?',.:]","",s)
        s=str(s).lower()
        s1=s[::-1]
        if s==s1:
            return True
        return False