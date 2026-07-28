class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        return [n for (n,f) in c.most_common(k)]

