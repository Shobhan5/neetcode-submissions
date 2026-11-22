class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i not in d.keys():
                d[i] = 1 
            else:
                d[i] += 1 
        e = d.items()
        w = sorted(e, key = lambda x: -x[1])
        l = []
        for elem in w:
            l.append(elem[0])
        
        return l[:k]
        