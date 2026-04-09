class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        tot=0
        rest=amount
        i=len(coins)-1
        while i>=0:
            if coins[i]<=rest:
                tot+=1
                rest=rest-coins[i]
            else:
                i-=1
        return tot if tot != -1 and rest==0 else -1