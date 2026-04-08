class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        se={"(":")","{":"}","[":"]"}
        for i in s:
            if i in se:
                stack.append(i)
            else:
                if not stack:
                    return False
                if se[stack[-1]]!=i:
                    return False
                else:
                    stack.pop()
        return not stack