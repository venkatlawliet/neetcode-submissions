class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        se=set()
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[left])
                left+=1
            se.add(s[i])
            max_length=max(max_length,i-left+1)
        return max_length
        # s=list(s)
        # left=0
        # right=0
        # window=set()
        # max_length=0
        # while right<len(s):
        #     if s[right] not in window:
        #         window.add(s[right])
        #         right+=1
        #         max_length=max(max_length,right-left)
        #     else:
        #         window.remove(s[left])
        #         left+=1
        # return max_length