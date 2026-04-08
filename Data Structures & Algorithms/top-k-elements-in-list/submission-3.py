class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # l=Counter(nums)
        # l=sorted(l.items(),key=lambda item: item[1],reverse=True)
        # return [t[0] for t in l[:k]]
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        l=list(sorted(count.items(), key=lambda item: item[1], reverse=True))
        ls=[]
        for i in l[:k]:
            ls.append(i[0])
        return ls