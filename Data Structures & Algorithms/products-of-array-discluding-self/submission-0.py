class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for i in range(len(nums))]
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        prefix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=prefix*res[i]
            prefix*=nums[i]
        return res
        # total=1
        # zeroes=0
        # for i in nums:
        #     if i==0:
        #         zeroes+=1
        #     else:
        #         total*=i
        # ls=[]
        # for j in nums:
        #     if zeroes>1:
        #         ls.append(0)
        #     elif zeroes==1:
        #         if j==0:
        #             ls.append(total)
        #         else:
        #             ls.append(0)
        #     else:
        #         ls.append(total//j)
        # return ls