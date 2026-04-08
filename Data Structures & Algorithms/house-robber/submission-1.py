class Solution:
    def rob(self, nums: List[int]) -> int:
        su={}
        def df(i):
            if i>=len(nums):
                return 0
            if i in su:
                return su[i]
            dngy=nums[i]+df(i+2)
            skip=df(i+1)
            su[i]=max(dngy,skip)
            return su[i]
        return df(0)
        # su=[]
        # def df(i,j):
        #     temp=j
        #     val=nums[i]
        #     while i<temp:
        #         val+=nums[temp]
        #         temp+=2
        #     su.append(val)
        #     df(i,j+1)
        # df(0,2)


        # ct1,ct2=0,0
        # for i in range(0,len(nums),2):
        #     ct1+=nums[i]
        # for j in range(1, len(nums), 2):
        #     ct2+=nums[j]
        # return max(ct1,ct2)
        