class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=Counter(nums)
        l=sorted(l.items(),key=lambda item: item[1],reverse=True)
        return [t[0] for t in l[:k]]
        # ls=[]
        # for i in l:
        #     if l[i]>=k:
        #         ls.append(i)
        # return ls