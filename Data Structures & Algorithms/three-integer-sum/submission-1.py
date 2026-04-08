class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=set()
        for a in range(len(nums)-2):
            left=a+1
            right=len(nums)-1
            while left<right:
                total=nums[a]+nums[left]+nums[right]
                if total > 0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    res.add((nums[a],nums[left],nums[right]))
                    left+=1
                    right-=1
        return list(res)
        # res=set()
        # ls=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return [list(t) for t in res]