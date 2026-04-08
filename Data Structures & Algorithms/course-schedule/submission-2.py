class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={i:[] for i in range(numCourses)}
        for ind1, ind2 in prerequisites:
            prereq[ind1].append(ind2)
        visiting=set()
        def df(i):
            if i in visiting:
                return False
            if prereq[i]==[]:
                return True
            visiting.add(i)
            for j in prereq[i]:
                if not df(j):
                    return False
            visiting.remove(i)
            prereq[i]=[]
            return True
        for i in range(numCourses):
            if not df(i):
                return False
        return True