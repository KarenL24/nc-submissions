class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        mheap = []
        for n in freqs.keys():
            heapq.heappush(mheap, (freqs[n], n))
            if len(mheap) > k:
                heapq.heappop(mheap)

        res = []
        while mheap:
            res.append(heapq.heappop(mheap)[1])
        return res
        