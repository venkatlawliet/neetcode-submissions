class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                leng=1
                curr=i
                while curr+1 in nums:
                    leng+=1
                    curr+=1
                longest=max(longest, leng)
        return longest
        # nums=sorted(set(nums))
        # ls=[]
        # i=0
        # while i<len(nums):
        #     z=i
        #     while i+1<len(nums) and nums[i]+1==nums[i+1]:
        #         i+=1
        #     ls.append(nums[z:i+1])
        #     i+=1
        # return max(len(i) for i in ls)
