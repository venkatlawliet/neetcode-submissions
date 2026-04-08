class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di=defaultdict(list)
        for s in strs:
            ar=[0 for i in range(26)]
            for ch in s:
                ar[ord(ch)-ord('a')]+=1
            di[tuple(ar)].append(s)
        return list(di.values())