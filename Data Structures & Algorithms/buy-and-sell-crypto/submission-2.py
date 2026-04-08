class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        ls=[]
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            if mini!=prices[i]:
                # profit=prices[i]-mini
                ls.append(prices[i]-mini)
        if len(ls)>0:
            return max(ls)
        else:
            return 0
        # left=0
        # right=len(prices)-1
        # ls=[]
        # while left<right:
        #     if prices[left]>prices[right]:
        #         right-=1
        #     else:
        #         diff=prices[right]-prices[left]
        #         ls.append(diff)
        #         left+=1
        # if len(ls)>0:
        #     return max(ls)
        # else:
        #     return 0