class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=nums[0]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if target>nums[mid] or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target>nums[right] or target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
        #     if nums[mid]==target:
        #         return mid
        #     if nums[mid]>target:
        #         if nums[left]<target:
        #             left=mid+1
        #         else:
        #             right=mid
        #     else:
        #         left=mid+1
        # return -1
        # # low=0
        # # high=len(nums)-1
        # # while low<high:
        # #     mid=(low+high)//2
        # #     if nums[mid]==target:
        # #         return mid
        # #     if target>nums[mid]:
        # #         if nums[high]>target:
        # #             low=mid+1
        # #         else:
        # #     else:
                
        # #         target>nums[mid] and target>nums[high]:
        # #         low=mid+1
        # #     elif target<nums[mid] and target>nums[low]:
        # #         high=mid
        # #     else:
        # #         return -1

        # #     if nums[mid]<nums[high] and nums[mid]<target:
        # #         low=mid+1
        # #     elif nums[mid]>nums[high] and nums[mid]>target:
        # #         low=mid+1
        # #     elif nums[mid]==target:
        # #         return mid
        # # return -1

