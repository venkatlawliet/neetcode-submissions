class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2=0,0
        for i in nums[1:]:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp
        first=rob2
        rob1,rob2=0,0
        for i in nums[:-1]:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp
        second=rob2
        return max(nums[0],first, second)
